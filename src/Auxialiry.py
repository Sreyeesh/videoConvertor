from pathlib import Path
import os


def get_settings_json_path():
    env = os.getenv("SETTINGS_JSON_PATH")
    if env:
        return Path(env)
    else:
        return Path(os.path.expanduser("~/.vc_settings.json"))
