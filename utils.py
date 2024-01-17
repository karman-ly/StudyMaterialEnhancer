import os

import config


def prepare_dirs():
    for config_dir in [
        config.BASE_DIR,
        config.INPUT_DIR,
        config.OUTPUT_DIR,
        config.AUDIO_OUTPUT_DIR,
        config.TEXT_OUTPUT_DIR,
        config.IMAGES_OUTPUT_DIR,
    ]:
        os.makedirs(config_dir, exist_ok=True)
