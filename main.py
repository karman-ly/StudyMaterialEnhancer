from dotenv import load_dotenv
from loguru import logger

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
    for i, image in enumerate(images):
        try:
            text = enhancers.explain_image(image, instructions, i)
            enhancers.text_to_speech(text, i)
            data.append(text)
        except Exception as e:
            logger.error(f"❌ Error while processing slide {i}:\n\n{e}")
        else:
            logger.info(f"✅ Successfully processed slide {i}")

    presentations.to_obsidian_md(data)
    logger.info(f"✅ Successfully created obsidian presenation guide")
    logger.info("🎉📖 Enjoy your learning!")


if __name__ == "__main__":
    main()
