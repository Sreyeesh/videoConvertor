import argparse


class ParseArgs(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        super().__init__("File watcher for videoConverter.")
        self.populate_options()

    def populate_options(self):
        self.add_argument("--port", type=int, nargs=1, required=True,
                          help="Port to bind to.")
        self.add_argument("--interface", type=str, nargs=1,
                          default="localhost",
                          help="Interface to bind to. Defaults to loopback device.")


if __name__ == "__main__":
    p = ParseArgs()
    p.parse_args()
