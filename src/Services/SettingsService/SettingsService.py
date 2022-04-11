
import json
from pathlib import Path
from typing import Dict

from src.Services.BaseService import BaseService
from src.Services.Exeptions import InvalidPath


class SettingsService(BaseService):

    def __init__(self, settings_path: Path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if settings_path.exists():
            fh = open(settings_path)
            self.settings = json.load(fh)
            fh.close()
        else:
            raise InvalidPath(f"Settings file {str(settings_path)} doesn't exist.")

    def get(self) -> Dict:
        return self.settings
