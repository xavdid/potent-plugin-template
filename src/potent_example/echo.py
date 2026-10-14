from pathlib import Path
from typing import Literal, override

from potent import BaseConfig, BaseOperation, OperationResult


class EchoOp(BaseOperation):
    """
    An example operation that echoes user-defined text.
    """

    class OpConfig(BaseConfig):
        text: str
        """
        the text to echo
        """

    slug: Literal["potent-example.echo"] = "potent-example.echo"
    config: OpConfig

    @override
    def run(self, directory: Path) -> OperationResult:
        cmd = ["echo", self.config.text]
        return self.exec_cmd_with_result(directory, cmd)

    @property
    @override
    def summary(self) -> str:
        return f"echo ({self.config.text})"
