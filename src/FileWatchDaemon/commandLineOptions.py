import argparse


class ParseArgs(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        super().__init__("File watcher for videoConverter.")
        self.populate_options()

    def populate_options(self):
        self.add_argument("--dport", type=int, nargs=1, required=True,
                          help="Destination port to connect back to.")
        self.add_argument("--destination", type=str, nargs=1,
                          default="localhost", help="Destination to connect back to.")


if __name__ == "__main__":
    p = ParseArgs()
    p.parse_args()
