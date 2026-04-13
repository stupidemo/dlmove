# dlmove/config.py

import yaml
from pathlib import Path

def load_config(config_path: str) -> dict:
    # expanduser() is needed because pathlib doesn't understand ~
    path = Path(config_path).expanduser().resolve()

    if not path.exists():
        print(f"Error: config not found -> {path}")
        raise SystemExit(1)
    
    with open(path, "r") as file:
        data = yaml.safe_load(file)
    
    validate_config(data)
    return data


def validate_config(data: dict) -> None:
    # make sure the config has everything we actually need
    required_keys = ["downloads_dir", "destination_dir", "extensions"]

    for key in required_keys:
        if key not in data:
            print(f"Error: field '{key}' is not in config")
            raise SystemExit(1)
    # extensions must be a dict like {mp3: [Music], pdf: [Documents, PDFs]}    
    if not isinstance(data["extensions"], dict):
        print("Error: 'extensions' should be a dictionary")
        raise SystemExit(1)
    
    # each extension maps to a list of subfolders (can be empty)    
    for ext, folders in data["extensions"].items():
        if not isinstance(folders, list):
            print(f"Error: value for 'ext' should be a list")
            raise SystemExit(1)