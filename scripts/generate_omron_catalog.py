#!/usr/bin/env python3
"""
Generate Omron catalog JSON from CSV file.

This script reads the Omron-10k.csv file (semicolon-separated with comma decimals)
and produces a JSON catalog file with all article information.
"""

import csv
import json
import sys
from pathlib import Path


def parse_price(price_str):
    """
    Convert price string with comma decimal to float.
    
    Args:
        price_str: Price string with comma as decimal separator (e.g., "45,99")
        
    Returns:
        float: Parsed price value
        
    Raises:
        ValueError: If the price string is invalid or empty
    """
    if not price_str or not price_str.strip():
        raise ValueError("Price string is empty or None")
    
    try:
        return float(price_str.replace(',', '.'))
    except ValueError as e:
        raise ValueError(f"Invalid price format: '{price_str}'") from e


def read_omron_csv(csv_path):
    """
    Read and parse the Omron CSV file.
    
    Args:
        csv_path: Path to the CSV file
        
    Returns:
        list: List of dictionaries containing article data
        
    Raises:
        ValueError: If CSV is missing required columns or has invalid data
    """
    articles = []
    required_columns = {'articleId', 'alias', 'price'}
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        # Use semicolon as delimiter
        reader = csv.DictReader(csvfile, delimiter=';')
        
        # Validate that required columns exist
        if not reader.fieldnames:
            raise ValueError("CSV file is empty or has no header")
        
        missing_columns = required_columns - set(reader.fieldnames)
        if missing_columns:
            raise ValueError(f"CSV is missing required columns: {', '.join(missing_columns)}")
        
        for row_num, row in enumerate(reader, start=2):  # start=2 accounts for header row
            # Skip empty rows (handle None values safely)
            if not any(row.values()) or all(not v or not v.strip() for v in row.values()):
                continue
            
            # Validate required fields are present
            if not row.get('articleId', '').strip():
                print(f"Warning: Skipping row {row_num} - missing articleId")
                continue
            if not row.get('alias', '').strip():
                print(f"Warning: Skipping row {row_num} - missing alias")
                continue
            if not row.get('price', '').strip():
                print(f"Warning: Skipping row {row_num} - missing price")
                continue
            
            try:
                # Parse each row into the required schema
                article = {
                    "articleId": row['articleId'].strip(),
                    "alias": row['alias'].strip(),
                    "price": parse_price(row['price'].strip())
                }
                articles.append(article)
            except ValueError as e:
                print(f"Warning: Skipping row {row_num} - {e}")
                continue
    
    return articles


def generate_catalog(csv_path, output_path):
    """
    Generate the JSON catalog from the CSV file.
    
    Args:
        csv_path: Path to the input CSV file (str or Path)
        output_path: Path to the output JSON file (str or Path)
    """
    # Convert to Path objects for consistency
    csv_path = Path(csv_path)
    output_path = Path(output_path)
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Read and parse CSV
    print(f"Reading CSV file: {csv_path}")
    articles = read_omron_csv(csv_path)
    print(f"Parsed {len(articles)} articles")
    
    # Write JSON output
    print(f"Writing JSON catalog: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(articles, jsonfile, indent=2, ensure_ascii=False)
    
    print(f"Successfully generated catalog with {len(articles)} articles")


def main():
    """Main entry point for the script."""
    # Get the repository root directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    # Define input and output paths
    csv_path = repo_root / 'Omron-10k.csv'
    output_path = repo_root / 'output' / 'omron_catalog_all.json'
    
    # Check if CSV file exists
    if not csv_path.exists():
        print(f"Error: CSV file not found at {csv_path}", file=sys.stderr)
        sys.exit(1)
    
    # Generate the catalog
    try:
        generate_catalog(csv_path, output_path)
    except Exception as e:
        print(f"Error generating catalog: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
