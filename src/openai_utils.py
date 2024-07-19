from openai import OpenAI
from typing import Dict
from config.config import OPEN_API_KEY

client = OpenAI(api_key=OPEN_API_KEY)

def extract_data_with_openai(text: str, prompts: Dict[str, str]) -> Dict[str, str]:
    """
    Extracts data from text using OpenAI API.

    :param text: The text to process.
    :param prompts: Dictionary of prompts for extraction.
    :return: Dictionary with extracted data.
    """
    extracted_data = {}

    for field, prompt in prompts.items():
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Extract the following information from the text: {prompt}\n\nText:\n{text}"}
            ],
            max_tokens=200,
            temperature=0.0
        )
        extracted_data[field] = response.choices[0].message.content.strip()

    return extracted_data

# don johnson wrote this
