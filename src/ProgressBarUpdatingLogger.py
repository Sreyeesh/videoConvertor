from proglog import TqdmProgressBarLogger, ProgressBarLogger


class ProgressBarUpdatingLogger(ProgressBarLogger):
    
    def __init__(self, update_gauge_cb, *args, **kwargs):

        super(ProgressBarUpdatingLogger, self).__init__(
            min_time_interval=0.5,
            *args, **kwargs)
        self.update_gauge_cb = update_gauge_cb
        self.total = None

    def bars_callback(self, bar, attr, value, old_value=None):
        print(f"Updating bar: {bar}, attr: {attr}, value: {value}, old_value: {old_value}")
        if attr == "total":
            self.total = value
        else:
            self.update_gauge_cb((value / self.total) * 100)

    def callback(self, **changes):
        # Every time the logger is updated, this function is called with
        # the `changes` dictionnary of the form `parameter: new value`.
        for (parameter, new_value) in changes.items():
            print(f"{parameter}: {new_value}")



