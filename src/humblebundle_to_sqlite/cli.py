import pathlib

import httpx
import typer

from humblebundle_to_sqlite import __version__
from humblebundle_to_sqlite import etl


DB_PATH_DEFAULT = typer.Argument(
    ...,
    file_okay=True,
    dir_okay=False,
    allow_dash=False,
    writable=True,
    help="Path to SQLite database",
)


cli = typer.Typer(help="Load data from humblebundle.com into a SQLite database")


@cli.command()
def bundles(db_path: pathlib.Path = DB_PATH_DEFAULT) -> None:
    """Load bundles data from current offers"""

    bundles_url = etl.BUNDLES_URL
    http_client = httpx

    with typer.progressbar(
        length=100,
    ) as p:

        p.label = "Extracting bundles"
        p.update(5)
        bundles = etl.extract_bundles(http_client=http_client, bundles_url=bundles_url)

        p.label = "Loading bundles"
        p.update(50)
        etl.load_bundles(db_path=db_path, bundles=bundles)

        p.update(45)


@cli.command()
def version() -> None:
    """Show version"""
    typer.echo(f"humblebundle-to-sqlite version {__version__}")
    raise typer.Exit()
