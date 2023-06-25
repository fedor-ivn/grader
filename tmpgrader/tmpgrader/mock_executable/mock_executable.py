from mock_executable.pipe import MockExecutablePipe
from mock_executable.pipe_session import PipeSession
import os
import args_proxy


class MockExecutable:
    def __init__(self, name: str, pipes_path: str):
        self.name = name
        self.pipe_path = f"{pipes_path}/{name}"
        self.pipe = MockExecutablePipe(self.pipe_path)

    def create(self) -> PipeSession:
        with open(self.name, "w") as executable:
            executable.write(
                args_proxy.script_template.format(
                    pipe_path=self.pipe_path
                )
            )

        os.chmod(self.name, 0o755)
        env_path_list: list[str] = os.environ["PATH"].split(
            os.pathsep
        )

        cwd = os.getcwd()
        if cwd not in env_path_list:
            os.environ["PATH"] = os.pathsep.join(
                [cwd] + env_path_list
            )
        return self.pipe.create()
