# omron-transform

A tool for transforming Omron product data from CSV format to structured JSON catalog.

## Features

- Parse Omron product CSV files (semicolon-delimited with comma decimal format)
- Generate structured JSON catalog with article information
- Support for batch processing of different article IDs

## Quick Start

### Generate Catalog

Run the catalog generation script:

```bash
python3 scripts/generate_omron_catalog.py
```

This will:
1. Read the `Omron-10k.csv` file from the repository root
2. Parse all articles (articleId, alias, price)
3. Generate `output/omron_catalog_all.json` with structured data

### Input Format

The CSV file (`Omron-10k.csv`) should have:
- **Delimiter:** Semicolon (`;`)
- **Columns:** articleId, alias, price
- **Price format:** Comma (`,`) as decimal separator (e.g., `45,99`)
- **Encoding:** UTF-8

Example:
```csv
articleId;alias;price
OMR001;Omron E3Z-D82 Photoelectric Sensor;45,99
OMR002;Omron E3FA-DN11 Sensor;32,50
```

### Output Format

The generated JSON file contains an array of article objects:

```json
[
  {
    "articleId": "OMR001",
    "alias": "Omron E3Z-D82 Photoelectric Sensor",
    "price": 45.99
  }
]
```

## Batch Processing

For processing different batches of article IDs, see [BATCH_PROCESSING_PROMPT.md](BATCH_PROCESSING_PROMPT.md) for detailed instructions and reusable prompts.

## Project Structure

```
omron-transform/
├── Omron-10k.csv                    # Input CSV file with product data
├── scripts/
│   └── generate_omron_catalog.py    # Main catalog generation script
├── output/
│   └── omron_catalog_all.json       # Generated JSON catalog
├── BATCH_PROCESSING_PROMPT.md       # Reusable prompts for batch processing
└── README.md                        # This file
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)