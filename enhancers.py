import base64
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Self

import openai
from loguru import logger

import config


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


def explain_image_call(data: ImageData, instructions: TextData) -> str:
    response = openai.chat.completions.create(
        seed=config.SEED,
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    instructions.as_dict(),
                    data.as_dict(),
                ],
            }
        ],
        max_tokens=config.MAX_TOKENS,
    )

    return response.choices[0].message.content


def text_to_speech_call(text: str, filename: str):
    response = openai.audio.speech.create(model="tts-1", voice=config.VOICE, input=text)
    response.stream_to_file(config.AUDIO_OUTPUT_DIR / filename)


def explain_image(image: ImageData, instructions: TextData, i: int) -> (str, bool):
    if os.path.exists(config.TEXT_OUTPUT_DIR / f"{i}.md") and not config.REGENERATE:
        logger.info(f"Slide {i}: Found saved text explanation, reusing...")
        with open(config.TEXT_OUTPUT_DIR / f"{i}.md", encoding="utf-8") as f:
            return f.read(), False
    else:
        logger.info(f"Slide {i}: 🤖 Explaining...")
        text = explain_image_call(image, instructions)
        with open(config.TEXT_OUTPUT_DIR / f"{i}.md", "w", encoding="utf-8") as f:
            f.write(text)

        return text, True


def text_to_speech(text: str, i: int, text_regenerated: bool = False):
    if (
        os.path.exists(config.AUDIO_OUTPUT_DIR / f"{i}.mp3")
        and not config.REGENERATE
        and not text_regenerated
    ):
        logger.info(f"Slide {i}: Found saved audio explanation, reusing...")
    else:
        logger.info(f"Slide {i}: 🤖 Reading...")
        text_to_speech_call(text, f"{i}.mp3")
