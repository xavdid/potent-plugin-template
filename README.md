# potent-plugin-template

A template for writing [potent](https://github.com/xavdid/potent) plugins. This provides a single example operation, `EchoOp`.

There's full documentation in the main README: https://github.com/xavdid/potent#authoring-plugins.

> [!TIP]
> To auto-generate the documentation below, run `uv run -- potent docs generate README.md`.

<!-- BEGIN:OPERATIONS -->

### Available Operations

| Slug                             | Requires Config? |
| -------------------------------- | ---------------- |
| [`potent-example.echo`](#EchoOp) | ✅ Reqiured      |

### EchoOp

An example operation that echoes user-defined text.

**Slug**: `potent-example.echo`

#### Config

| name   | type  | description      | default (if optional) |
| ------ | ----- | ---------------- | --------------------- |
| `text` | `str` | the text to echo |                       |

<!-- END:OPERATIONS -->
