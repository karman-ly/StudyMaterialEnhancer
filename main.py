from converters import convert
from enhancers import enhance
from presentations import present
from dotenv import load_dotenv


def main():
    load_dotenv()
    material = convert()
    enhanced_material = enhance(material)
    present(enhanced_material)


if __name__ == "__main__":
    main()
