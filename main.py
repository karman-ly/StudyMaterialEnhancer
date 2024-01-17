from dotenv import load_dotenv
from loguru import logger

import config
import enhancers
import extractors
import presentations
import utils


@logger.catch
def main():
    load_dotenv()
    utils.prepare_dirs()

    logger.info("Extracting images from pdf")
    images = extractors.pdf_to_images()
    logger.info("Reading instructions")
    instructions = extractors.read_instructions()

    data = []
    images_iter = list(enumerate(images, start=1))
    if config.RANGE:
        images_iter = images_iter[config.RANGE[0] - 1 : config.RANGE[1] - 1]
    for i, image in images_iter:
        if i in config.EXCLUDE_SLIDES:
            logger.info(f"Slide {i}: Excluded")
            continue
        try:
            text, text_regenerated = enhancers.explain_image(image, instructions, i)
            enhancers.text_to_speech(text, i, text_regenerated)
            data.append((i, text))
        except Exception as e:
            logger.error(f"❌ Error while processing slide {i}:\n{e}")
        else:
            logger.info(f"✅ Successfully processed slide {i}")

    presentations.to_obsidian_md(data)
    logger.info(f"✅ Successfully created obsidian presenation guide")
    logger.info("🎉📖 Enjoy your learning!")


if __name__ == "__main__":
    main()
