import threading
import tkinter
from threading import Lock

from compression import reduce_dem_all, recode
from src.DirMapper import DirMapper
from src.DirsSettings import DirsSettings
from src.FTPAwareDirMapper import FTAwareDirMapper
from src.ProgressBarUpdatingLogger import ProgressBarUpdatingLogger


class JobRunner:

    def __init__(self):
        self._t_worker = None
        self._work_is_done = False

    def run_all(self, jobs):
        if not self._t_worker or self._work_is_done:
            print("threading")
            if self._work_is_done:
                self._t_worker.join()

            self._t_worker = threading.Thread(target=self._run_all, kwargs={
                "jobs": jobs
            })
            self._t_worker.start()
        print("returning")

    @property
    def not_working(self):
        return self._work_is_done

    def _run_all(self, jobs):
        print("_run_all")
        settings = DirsSettings('settings.json').get_settings()
        d_map = DirMapper(settings)

        # Filter only those jobs for which target doesn't exist.
        d_map = [x for x in d_map.get_dir_mappings() if not x[1].exists()]
        for i, d in enumerate(d_map):
            logger = ProgressBarUpdatingLogger(jobs[i].gauge.update_gauge)
            recode(str(d[0]), str(d[1]), d[2], logger)

        self._work_is_done = True

