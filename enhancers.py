import base64
from dataclasses import dataclass
from pathlib import Path
from typing import Self


@dataclass
class ImageData:
    url: str

    @classmethod
    def from_file(cls, file_path: Path) -> Self:
        with open(file_path, "rb") as f:
            return cls(base64.b64encode(f.read()).decode("utf-8"))

    def as_dict(self) -> dict[str, str]:
        return {"type": "image_url", "image_url": {"url": self.url}}


@dataclass
class TextData:
    text: str

    def as_dict(self) -> dict[str, str]:
        return {"type": "text", "text": self.text}


def explain_image(data: ImageData) -> str:
    pass


def text_to_speech(data: TextData):
    pass
