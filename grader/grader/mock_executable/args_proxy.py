script_template = '''#!/usr/bin/env python

import pickle
import sys


class ArgsProxy:
    """
    Class that acts as a proxy program
    and sends command line arguments
    """

    def __init__(self, pipe_path: str):
        self.pipe_path = pipe_path

    def send_arguments(self) -> None:
        """
        Sends the command line arguments
        into the pre-created named pipe.

        Saves all the args using pickle.
        """
        args = sys.argv[1:]
        with open(self.pipe_path, "wb") as pipe:
            pickle.dump(args, pipe)


if __name__ == "__main__":
    args_proxy = ArgsProxy(pipe_path="{pipe_path}")
    args_proxy.send_arguments()

'''

if __name__ == "__main__":
    eval(
        compile(
            script_template.format(pipe_path="example"),
            filename="<string>",
            mode="exec",
        )
    )
