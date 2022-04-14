import json
from json import JSONDecodeError
from pathlib import Path
from typing import Dict, List


class DirsSettings:
    """Manage settings of input-/output-dirs.

    Reads and writes settings to-/from a json-file, and takes care, that in_dirs/out_dirs have
    absolute paths in the json-file.
    """

    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def _relative_to_absolute_path(path: Path):
        return Path().cwd() / path if not Path(path).is_absolute() else path

    def get_settings(self) -> List[Dict]:
        """Get settings.

        example:
        [{
            "in_dir": "in_dir",
            "out_dir": "out_dir",
            "out_ftype": "file_extension",
            "audio_brate": 256,  # kbps
            "video_brate": 400,  # also kbps
            "video_res": [1024, 768],  # Horizontal and vertical resolution
            "add_ext": "add_ext",  # Postfix for the filename excluding the file extension.
                                   # For example: file1.avi -> file1_youtube.mp4
            "name": "name"  # Encoding profile name.
        }]
        """
        try:
            with open(self.filename, 'r') as fh:
                entries = json.load(fh)
        except FileNotFoundError as e:
            return []
        return entries

    def save_new_entry(self, entry: Dict) -> List[Dict]:
        """Save new given entry.

        :return settings
        """
        # Convert paths in entry to absolute if they're not.
        entry["in_dir"] = str(DirsSettings._relative_to_absolute_path(entry["in_dir"]))
        entry["out_dir"] = str(DirsSettings._relative_to_absolute_path(entry["out_dir"]))

        settings = self.get_settings()
        if not entry in settings:
            settings.append(entry)
            with open(self.filename, 'w') as fh:
                json.dump(settings, fh, indent=2)
        return settings

    def save_settings(self, settings: List[Dict]) -> None:
        with open(self.filename, 'w') as fh:
            json.dump(settings, fh, indent=2)

    def delete_setup(self, name: str) -> bool:
        """Return True on success, False on fail."""

        settings = self.get_settings()
        try:
            index = [x.get("name") for x in settings].index(name)
        except ValueError as e:
            return False
        del settings[index]
        self.save_settings(settings)
        return True


