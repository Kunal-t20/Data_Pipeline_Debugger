from pathlib import Path
from typing import List,Optional

SUPPORTED_EXT = [".md",".txt"]

def load_file(file_path: str) -> Optional[str]:

    path=Path(file_path)

    if not path.exists():
        return f"File not found: {file_path}"

    try:
        text = path.read_text(encoding="utf-8")
        return text.strip()
    except Exception as e:
        return f"Error reading file: {e}"

    
def load_all_doc(folder_path: str) -> List[str]:

    path = Path(folder_path)

    if not path.exists():
        return []

    documents = []

    for file in path.iterdir():

        if file.suffix in SUPPORTED_EXT:

            content = load_file(str(file))

            if content and not content.startswith("File not found"):
                documents.append(content)

    return documents