import threading

from ttkbootstrap import SUCCESS
from ttkbootstrap.toast import ToastNotification

from src.Compression import recode
from src.DirsSettings import DirsSettings
from src.FTAwareDirMapper import FTAwareDirMapper
from src.Auxialiry import get_settings_json_path
from src.ProgressBarUpdatingLogger import ProgressBarUpdatingLogger


class JobRunner:

    def __init__(self):
        self._t_worker = None
        self._work_is_done = False

    def run_all(self, jobs):
        if not self._t_worker or self._work_is_done:
            if self._work_is_done:
                self._t_worker.join()

            self._t_worker = threading.Thread(target=self._run_all, kwargs={
                "jobs": jobs
            })
            self._t_worker.start()

    @property
    def not_working(self):
        return self._work_is_done

    def _run_all(self, jobs):
        settings = DirsSettings(get_settings_json_path()).get_settings()
        d_map = FTAwareDirMapper(settings)

        # Filter only those jobs for which target doesn't exist.
        d_map = [x for x in d_map.get_dir_mappings() if not x[1].exists()]
        for i, d in enumerate(d_map):
            logger = ProgressBarUpdatingLogger(jobs[i].gauge.update_gauge, bars=("t",))
            recode(str(d[0]), str(d[1]), d[2], logger)
            jobs[i].gauge.configure(bootstyle=SUCCESS)

        self._work_is_done = True
        show_completion_notification()


def show_completion_notification():
    toast = ToastNotification(
        title="VideoConvertor is ready.",
        message="Wee! VideoConvertor has completed all of it's tasks.",
        duration=15000
    )
    toast.show_toast()
