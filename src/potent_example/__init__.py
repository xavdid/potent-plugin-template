from potent import BaseOperation

from potent_example.echo import EchoOp

# this is the list that pyproject.toml points at
operations: list[type[BaseOperation]] = [
    EchoOp,
]
