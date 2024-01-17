import config


def to_obsidian_md(data: list[str]):
    res = []

    for i, text in enumerate(data):
        slide_text = [
            f"# Slide {i}",
            f"![[{i}.jpg]]",
            text,
            f"```audio-player\n[[{i}.mp3]]\n```",
        ]

        res.append("\n\n".join(slide_text))

    with open(config.OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(res))
