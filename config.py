from pathlib import Path

BASE_DIR = Path(r"C:\dev\obsidian-vault\papsan\Projects\Study Material")

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_FILE = INPUT_DIR / "presentation.pdf"
INSTRUCTIONS_FILE = INPUT_DIR / "instructions.md"

OUTPUT_FILE = OUTPUT_DIR / INPUT_FILE.with_suffix(".md").name
AUDIO_OUTPUT_DIR = OUTPUT_DIR / "audio"
TEXT_OUTPUT_DIR = OUTPUT_DIR / "text"
IMAGES_OUTPUT_DIR = OUTPUT_DIR / "images"

REGENERATE = False
RANGE = (3, 10)
EXCLUDE_SLIDES = []

IMAGE_RESOLUTION = None
VOICE = "onyx"
MAX_TOKENS = 2500
SEED = 34
