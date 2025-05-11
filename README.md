<img src="https://github.com/Rodea41/Cargill_bol_parser/blob/main/meat.webp" width="1000" height="400" />

# PDF Bill of Lading Parser


This Python utility is designed to extract structured data from PDF Bills of Lading (BOL) and export it to CSV format. The tool uses regular expressions to identify and parse key shipping information including lot numbers, order quantities, product codes, weights, and pallet IDs from PDF documents.

## Features

- **PDF Text Extraction**: Automatically reads and processes text from multi-page BOL PDFs
- **Data Parsing**: Extracts critical shipping information using regular expression pattern matching
- **Structured Output**: Organizes parsed data into a well-formatted CSV spreadsheet
- **Multi-Page Support**: Processes all pages in a PDF document with proper header handling

## Requirements

The script requires the following Python libraries:
- PyPDF2
- re (Regular Expressions, included in Python standard library)
- csv (included in Python standard library)

You can install the required external dependency using pip:

```bash
pip install PyPDF2
```

## How It Works

The script performs the following operations:

1. **PDF Processing**: Opens and reads the PDF document page by page
2. **Text Extraction**: Extracts raw text content from each page
3. **Pattern Matching**: Uses regular expressions to identify specific data patterns:
   - Lot numbers and product information
   - Pallet IDs
   - Gross and net weights
4. **Data Structuring**: Organizes extracted data into dictionaries
5. **CSV Export**: Writes the structured data to a CSV file with appropriate headers

## Key Functions

- `product_info()`: Extracts lot numbers, case quantities, product codes, and code dates
- `get_pallet_id()`: Identifies pallet IDs from the document
- `get_gross_weight()`: Extracts gross unit and shipping weights
- `get_net_weight()`: Extracts net unit and shipping weights
- `get_page_info()`: Processes a single page and writes data to CSV
- `main()`: Controls the overall execution flow

## Output Format

The script generates a CSV file named 'spreadsheet.csv' with the following columns:
- Lot #
- Case Orders
- Case Picked
- Product Code
- Code Date
- Gross Unit Weight
- Gross Shipping Weight
- Net Unit Weight
- Net Shipping Weight

## Usage

1. Ensure your PDF file is named "bol2.pdf" and placed in the same directory as the script
2. Run the script:

```bash
python app.py
```

3. The extracted data will be saved to 'spreadsheet.csv' in the same directory

## Customization

To process a different PDF file, modify the file path in the `get_page_info()` and `main()` functions:

```python
with open("your_file_name.pdf", "rb") as f:
    # Rest of the code
```

## Notes

- The script is designed for a specific BOL format and may require adjustments for different document layouts
- Ensure your PDF is text-based (not scanned) for proper text extraction
- The current implementation appends data to the CSV file; remove existing output files before rerunning to avoid duplication
