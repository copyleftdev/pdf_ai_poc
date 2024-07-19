import json
from src.pdf_utils import extract_text_from_pdf
from src.openai_utils import extract_data_with_openai
from src.mapper import load_json_schema, map_to_json_schema
from config.config import PDF_PATH, SCHEMA_PATH

def main():
    json_schema = load_json_schema(SCHEMA_PATH)


    extraction_prompts = {
        "email": "Extract email addresses",
        "date": "Extract dates",
        "phone": "Extract phone numbers",
    }


    pdf_text = extract_text_from_pdf(PDF_PATH)


    extracted_data = extract_data_with_openai(pdf_text, extraction_prompts)

    mapped_data = map_to_json_schema(extracted_data, json_schema)

    print(json.dumps(mapped_data, indent=4))

if __name__ == "__main__":
    main()
