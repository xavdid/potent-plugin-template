from typing import ClassVar, Literal, override

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

        name: str
        """
        Used to differentiate between multiple instances of this operation
        """

        ignored_fields_for_compare: ClassVar[set[str]] = {"name"}

    slug: Literal["potent-plugin-example.echo"] = "potent-plugin-example.echo"
    config: OpConfig

    @override
    def run(self, context: Context) -> OperationResult:
        cmd = ["echo", self.config.text]
        return context.exec_cmd(cmd)

    @property
    @override
    def summary(self) -> str:
        return f"echo ({self.config.name})"
