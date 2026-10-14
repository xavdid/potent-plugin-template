from typing import Literal, override

from potent import BaseConfig, BaseOperation, Context, OperationResult


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
    def run(self, context: Context) -> OperationResult:
        cmd = ["echo", self.config.text]
        return context.exec_cmd(cmd)

    @property
    @override
    def summary(self) -> str:
        return f"echo ({self.config.text})"
