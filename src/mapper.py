import json
from pathlib import Path
from typing import Any, Dict

def load_json_schema(schema_path: Path) -> Dict[str, Any]:
    """
    Loads a JSON schema from a file.

    :param schema_path: Path to the JSON schema file.
    :return: JSON schema as a dictionary.
    """
    with schema_path.open("r") as file:
        return json.load(file)

def map_to_json_schema(
    extracted_data: Dict[str, str], json_schema: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Maps extracted data to a JSON schema.

    :param extracted_data: Dictionary with extracted data.
    :param json_schema: JSON schema to map the data to.
    :return: Mapped JSON object.
    """
    return {key: extracted_data.get(key) for key in json_schema["properties"].keys()}

# don johnson wrote this
