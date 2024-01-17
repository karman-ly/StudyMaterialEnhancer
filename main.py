import adapters
import enhancers
import presentations
from dotenv import load_dotenv


def main():
    material = adapters.pdf_to_images()
    enhanced_material = enhancers.enhance_material(material)
    presentations.to_obsidian_md(enhanced_material)


if __name__ == "__main__":
    load_dotenv()
    main()
