
class Filetypes:

    @staticmethod
    def is_video_file(filename: str) -> bool:
        parts = filename.split()
        if parts[-1].lower() in ["avi", "mov", "mp4", "wmv", "mkv", "webm"]:
            return True
        return False

    @staticmethod
    def is_image_file(filename: str):
        parts = filename.split()
        if parts[-1].lower in ["jpg", "png", "gif", "apng", "bmp", "raw", "tiff", "psd",
                               "cr2", "exr"]:
            return True
        return False
