import config


def to_obsidian_md(data_enumerated: list[(int, str)]):
    res = []

    for i, text in data_enumerated:
        slide_text = [
            f"# Slide {i}",
            f"```audio-player\n[[{i}.mp3]]\n```",
            f"![[{i}.jpg]]",
            text,
        ]

        res.append("\n\n".join(slide_text))

    with open(config.OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(res))
