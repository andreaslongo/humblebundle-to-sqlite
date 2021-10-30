from typer.testing import CliRunner

from humblebundle_to_sqlite import __version__
from humblebundle_to_sqlite.cli import cli


runner = CliRunner()


def test_no_command() -> None:
    result = runner.invoke(cli, [])
    assert result.exit_code == 2
    assert "Error: Missing command" in result.stdout


def test_version() -> None:
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_bundles_no_arguments() -> None:
    result = runner.invoke(cli, ["bundles"])
    assert result.exit_code == 2
    assert "Error: Missing argument" in result.stdout
