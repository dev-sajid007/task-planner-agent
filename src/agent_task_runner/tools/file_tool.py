from pathlib import Path


class FileTool:

    def create_file(self, path: str, content: str = "") -> str:
        file_path = Path(path)

        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)

        return f"Created file: {file_path}"