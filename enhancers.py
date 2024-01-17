import base64
from dataclasses import dataclass
from pathlib import Path
from typing import Self
from openai import OpenAI

import config


def get_client() -> OpenAI:
    return OpenAI()


@dataclass
class ImageData:
    url: str

    @classmethod
    def from_file(cls, file_path: Path) -> Self:
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return cls(f"data:image/jpg;base64,{encoded}")

    def as_dict(self) -> dict[str, str]:
        return {"type": "image_url", "image_url": {"url": self.url}}


@dataclass
class TextData:
    text: str

    def as_dict(self) -> dict[str, str]:
        return {"type": "text", "text": self.text}


def explain_image(data: ImageData) -> str:
    response = get_client().chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    data.as_dict()
                ],
            }
        ],
        max_tokens=300,
    )
    print(response)

    return response.choices[0].message.content


def text_to_speech(text: str, output_file):
    response = get_client().audio.speech.create(
        model="tts-1",
        voice=config.VOICE,
        input=text
    )
    response.stream_to_file(output_file)


def enhance(images: list[ImageData]) -> list[str]:
    text = explain_image(images[0])
    text_to_speech(text, config.OUTPUT_DIR / "audio" / "0.mp3")
    return [text]
