# PDF Data Extractor

This project extracts data from a PDF file using OpenAI's API and maps it to a predefined JSON schema.

## Project Structure

```
pdf_extractor/
│
├── config/
│   └── config.py
│
├── data/
│   └── schema.json
│
├── src/
│   ├── __init__.py
│   ├── pdf_utils.py
│   ├── openai_utils.py
│   └── mapper.py
│
├── generate_sample_pdf.py
├── main.py
├── Pipfile
├── Pipfile.lock
├── ruff.toml
└── README.md
```

## Setup

### Prerequisites

1. **Python 3.9 or higher**: Ensure you have Python 3.9+ installed.
2. **Pipenv**: Ensure you have `pipenv` installed.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pdf_extractor.git
   cd pdf_extractor
   ```

2. Install dependencies using `pipenv`:

   ```bash
   pipenv install
   pipenv install reportlab  # For generating the sample PDF
   pipenv install --dev ruff  # For linting
   ```

3. Set up the OpenAI API key:

   - Create a `.env` file in the root directory and add your OpenAI API key:

     ```
     OPEN_API_KEY=your-openai-api-key
     ```

### Generate Sample PDF

Generate a sample PDF with test data to use for extraction:

```bash
pipenv run python generate_sample_pdf.py
```

### Running the Code

To extract data from the PDF and map it to the JSON schema:

```bash
pipenv run python main.py
```

### Linting with Ruff

To check your code for linting errors with `ruff`, run:

```bash
pipenv run ruff check .
```

To automatically fix linting errors with `ruff`, run:

```bash
pipenv run ruff --fix .
```

## How It Works

1. **Configuration**: The `config/config.py` file loads configuration settings and the OpenAI API key from environment variables.

2. **PDF Generation**: The `generate_sample_pdf.py` script generates a sample PDF with email addresses, dates, and phone numbers.

3. **PDF Text Extraction**: The `src/pdf_utils.py` file contains the `extract_text_from_pdf` function, which extracts text from the PDF.

4. **Data Extraction Using OpenAI**: The `src/openai_utils.py` file contains the `extract_data_with_openai` function, which uses OpenAI's API to extract data from the extracted text based on predefined prompts.

5. **Mapping Data to JSON Schema**: The `src/mapper.py` file contains the `load_json_schema` and `map_to_json_schema` functions, which load the JSON schema and map the extracted data to the schema.

6. **Main Script**: The `main.py` script orchestrates the entire process: it loads the JSON schema, extracts text from the PDF, uses OpenAI's API to extract data, maps the data to the JSON schema, and prints the mapped data as JSON.

## Example Output

After running `main.py`, the output should be a JSON object containing the extracted email addresses, dates, and phone numbers from the sample PDF:

```json
{
    "email": [
        "example1@example.com",
        "example2@example.com"
    ],
    "date": [
        "01/01/2023",
        "02/02/2023"
    ],
    "phone": [
        "(123) 456-7890",
        "(987) 654-3210"
    ]
}
```

