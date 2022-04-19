import enum
from pathlib import Path
from typing import Dict, List, Hashable, Callable, Tuple

from .DirMapper import DirMapper


class FileType(enum.IntFlag):
    Video = 1
    Audio = 2
    Image = 4


class FTAwareDirMapper(DirMapper):

    def __init__(self, dir_settings: List[Dict]):
        super(FTAwareDirMapper, self).__init__(dir_settings)

    def get_dir_mappings(self, ft: FileType = FileType.Video) -> List[Tuple[Path, Path, Dict]]:
        """Filter only ft filetypes from source files and do what superclass method does.

        :argument ft is an IntFlag enum. To select several filetypes do bitwise or.
                  For example obj.get_dir_mappings(FileType.Video | Filetype.Image)
        """
        ret = super(FTAwareDirMapper, self).get_dir_mappings()
        if ft & FileType.Video:
            ret += filter(lambda x: FTAwareDirMapper.is_video_file(str(x[0])), ret)
        if ft & FileType.Audio:
            ret += filter(lambda x: FTAwareDirMapper.is_audio_file(str(x[0])), ret)
        if ft & FileType.Image:
            ret += filter(lambda x: FTAwareDirMapper.is_image_file(str(x[0])), ret)
        return ret

    @staticmethod
    def is_video_file(filename: str) -> bool:
        parts = filename.split()
        if parts[-1].lower() in ["avi", "mov", "mp4", "wmv", "mkv", "webm"]:
            return True
        return False

    @staticmethod
    def is_audio_file(filename: str) -> bool:
        parts = filename.split()
        if parts[-1].lower() in ["mp3", "wav", "ogg"]:
            return True
        return False

    @staticmethod
    def is_image_file(filename: str):
        parts = filename.split()
        if parts[-1].lower in ["jpg", "png", "gif", "apng", "bmp", "raw", "tiff", "psd",
                               "cr2", "exr"]:
            return True
        return False
