# Reusable Prompt for Omron Catalog Generation

## Task: Generate Omron Catalog for a Different Batch of Article IDs

Use this prompt when you need to generate a catalog JSON file for a different batch of article IDs:

---

**Prompt:**

Generate an Omron catalog JSON file for the following article IDs: [LIST_YOUR_ARTICLE_IDS_HERE]

**Requirements:**
1. Update the `Omron-10k.csv` file with the new article data
2. Ensure the CSV format follows the existing structure:
   - Delimiter: semicolon (`;`)
   - Columns: articleId, alias, price
   - Price format: comma (`,`) as decimal separator (e.g., `45,99`)
3. Run the generation script: `python3 scripts/generate_omron_catalog.py`
4. Verify the output in `output/omron_catalog_all.json`

**Example CSV Format:**
```
articleId;alias;price
OMR011;New Product Name;99,99
OMR012;Another Product;150,50
```

**Example Usage:**
```bash
# After updating Omron-10k.csv with new article data
cd /path/to/omron-transform
python3 scripts/generate_omron_catalog.py
```

**Expected Output:**
- JSON file at `output/omron_catalog_all.json`
- Array of objects with schema:
  ```json
  {
    "articleId": "string",
    "alias": "string", 
    "price": number
  }
  ```

**Notes:**
- The script automatically handles comma-to-dot decimal conversion
- The script skips the CSV header row automatically
- Output directory is created automatically if it doesn't exist
- Prices are converted to float/number type in JSON

---

## Batch Processing Instructions

For processing multiple batches:

1. **Prepare your CSV:** Update `Omron-10k.csv` with your batch of articles
2. **Run the script:** Execute `python3 scripts/generate_omron_catalog.py`
3. **Review output:** Check `output/omron_catalog_all.json` for correctness
4. **Archive if needed:** Rename output file before processing next batch (e.g., `omron_catalog_batch1.json`)

## Troubleshooting

- **CSV not found:** Ensure `Omron-10k.csv` exists in the repository root
- **Price format errors:** Verify prices use comma (`,`) as decimal separator
- **Delimiter issues:** Ensure CSV uses semicolon (`;`) as delimiter
- **Encoding issues:** CSV should be UTF-8 encoded
