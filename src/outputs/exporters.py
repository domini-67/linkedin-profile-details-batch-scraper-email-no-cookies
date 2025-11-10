thonimport json
from pathlib import Path

class JSONExporter:
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def save(self, data):
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        with self.filepath.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)