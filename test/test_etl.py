import pathlib
from typing import Callable, Any, cast

import pytest
import sqlite_utils

from humblebundle_to_sqlite import etl


@pytest.mark.acceptance
def test_load_bundles(tmp_path: pathlib.Path) -> None:
    db_path = tmp_path / "test.db"
    bundles_url = etl.BUNDLES_URL
    http_client = FakeHttpClient()

    bundles = etl.extract_bundles(http_client=http_client, bundles_url=bundles_url)
    etl.load_bundles(db_path=db_path, bundles=bundles)

    db = sqlite_utils.Database(db_path)
    tables = db.table_names()
    bundles_from_db = list(db[etl.BUNDLES_TABLE].rows)
    items_from_db = list(db[etl.ITEMS_TABLE].rows)
    assert etl.BUNDLES_TABLE in tables
    assert etl.ITEMS_TABLE in tables
    assert bundles_from_db
    assert items_from_db


class FakeResponse:
    def __init__(self, content: bytes) -> None:
        self.content = content

    def raise_for_status(self) -> None:
        pass


class FakeHttpClient:
    def get(self, url: str) -> FakeResponse:
        if url.endswith("/bundles"):
            content = get_bundles_html()
        if "/books/" in url:
            content = get_book_items_html()
        if "/games/" in url:
            content = get_game_items_html()
        if "/software/" in url:
            content = get_software_items_html()
        return FakeResponse(content)


def get_bundles_html() -> bytes:
    """Source: https://www.humblebundle.com/bundles

    This snapshot contains 10 bundles from categories books, games and software.
    """
    p = pathlib.Path(__file__).parent / "humblebundle.com.bundles.html"
    html = p.read_bytes()
    return html


def get_book_items_html() -> bytes:
    """Source: https://www.humblebundle.com/books/infrastructure-and-ops-oreilly-books

    This snapshot contains 15 book items + 1 charity of 1 bundle.
    """
    p = pathlib.Path(__file__).parent / "humblebundle.com.items.books.html"
    html = p.read_bytes()
    return html


def get_book_items_html_bad() -> bytes:
    """Source: https://www.humblebundle.com/books/fan-faves-and-new-hits-dynamite-2021-books

    This snapshot contains 46 book items + ? charity of 1 bundle.
    """
    p = pathlib.Path(__file__).parent / "humblebundle.com.items.books.bad.html"
    html = p.read_bytes()
    return html


def get_game_items_html() -> bytes:
    """Source: https://www.humblebundle.com/games/play-pink-best-asmodee-digital

    This snapshot contains 25 game items + 1 charity of 1 bundle.
    """
    p = pathlib.Path(__file__).parent / "humblebundle.com.items.games.html"
    html = p.read_bytes()
    return html


def get_software_items_html() -> bytes:
    """Source: https://www.humblebundle.com/software/javascript-software

    This snapshot contains 14 software items + 2 charities of 1 bundle.
    """
    p = pathlib.Path(__file__).parent / "humblebundle.com.items.software.html"
    html = p.read_bytes()
    return html


def get_bundles() -> list[etl.Bundle]:
    html = get_bundles_html()
    bundles_data = etl._extract_bundles(html)
    bundles = etl._transform_bundles(bundles_data)

    for bundle in bundles:
        if bundle.category == "books":
            bundle.items = get_book_items()
        if bundle.category == "games":
            bundle.items = get_game_items()
        if bundle.category == "software":
            bundle.items = get_software_items()
    return bundles


def get_book_items() -> list[etl.Item]:
    html = get_book_items_html()
    items_data = etl._extract_items(html)
    items = etl._transform_items(items_data)
    return items


def get_game_items() -> list[etl.Item]:
    html = get_game_items_html()
    items_data = etl._extract_items(html)
    items = etl._transform_items(items_data)
    return items


def get_software_items() -> list[etl.Item]:
    html = get_software_items_html()
    items_data = etl._extract_items(html)
    items = etl._transform_items(items_data)
    return items


def test_extract_bundles_data_from_bundles_html() -> None:
    html = get_bundles_html()
    bundles_data = etl._extract_bundles(html)
    assert bundles_data
    assert len(bundles_data) == 10


def test_transform_bundles_from_bundles_data() -> None:
    html = get_bundles_html()
    bundles_data = etl._extract_bundles(html)
    bundles = etl._transform_bundles(bundles_data)
    assert len(bundles) == 10


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (get_book_items_html, 15 + 1),
        (get_game_items_html, 25 + 1),
        (get_software_items_html, 14 + 2),
    ],
)
def test_extract_items_data_from_items_html(
    test_input: Callable[[], bytes], expected: int
) -> None:
    html = test_input()
    items_data = etl._extract_items(html)
    assert items_data
    assert len(items_data) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (get_book_items_html, 15),
        (get_game_items_html, 25),
        (get_software_items_html, 14),
        (get_book_items_html_bad, 46),
    ],
)
def test_transform_items_from_items_data(
    test_input: Callable[[], bytes], expected: int
) -> None:
    html = test_input()
    items_data = etl._extract_items(html)
    items = etl._transform_items(items_data)
    assert len(items) == expected


def test_load_bundles_into_db(expected_bundles: list[dict[str, Any]]) -> None:
    db = sqlite_utils.Database(memory=True)
    bundles = get_bundles()
    # items = get_book_items()

    etl._insert_bundles_and_items(db, bundles)

    tables = db.table_names()
    assert etl.BUNDLES_TABLE in tables

    bundles_from_db = list(db[etl.BUNDLES_TABLE].rows)
    assert bundles_from_db == expected_bundles


def test_load_items_into_db(expected_items: list[dict[str, Any]]) -> None:
    db = sqlite_utils.Database(memory=True)
    bundles = get_bundles()

    etl._insert_bundles_and_items(db, bundles)

    tables = db.table_names()
    assert etl.ITEMS_TABLE in tables

    items_from_db = list(db[etl.ITEMS_TABLE].rows)
    assert items_from_db == expected_items


def test_load_bundles_and_items_into_db_twice() -> None:
    db = sqlite_utils.Database(memory=True)
    bundles = get_bundles()

    etl._insert_bundles_and_items(db, bundles)
    etl._insert_bundles_and_items(db, bundles)

    bundles_from_db = list(db[etl.BUNDLES_TABLE].rows)
    items_from_db = list(db[etl.ITEMS_TABLE].rows)
    assert len(bundles_from_db) == 10
    assert len(items_from_db) == 15 + 25 + 14


def test_fulltext_search_tables() -> None:
    db = sqlite_utils.Database(memory=True)
    bundles = get_bundles()
    etl._insert_bundles_and_items(db, bundles)

    bundles_table = cast(sqlite_utils.db.Table, db.table(etl.BUNDLES_TABLE))
    items_table = cast(sqlite_utils.db.Table, db.table(etl.ITEMS_TABLE))

    assert bundles_table.detect_fts()
    assert items_table.detect_fts()


def test_fulltext_search_tables_fts5() -> None:
    db = sqlite_utils.Database(memory=True)
    bundles = get_bundles()
    etl._insert_bundles_and_items(db, bundles)

    fts_tables = db.table_names(fts5=True)

    assert "bundles_fts" in fts_tables
    assert "items_fts" in fts_tables


def test_fulltext_search_results() -> None:
    db = sqlite_utils.Database(memory=True)
    bundles = get_bundles()
    etl._insert_bundles_and_items(db, bundles)
    bundles_table = cast(sqlite_utils.db.Table, db.table(etl.BUNDLES_TABLE))
    items_table = cast(sqlite_utils.db.Table, db.table(etl.ITEMS_TABLE))

    bundles_results = list(bundles_table.search("Learn"))
    items_results = list(items_table.search("Learn"))

    assert len(bundles_results) == 4
    assert len(items_results) == 30
