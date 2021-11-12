import json
import pathlib
from dataclasses import dataclass, asdict, field
from hashlib import sha1
from typing import Any, cast

import bs4
import sqlite_utils


HUMBLEBUNDLE_URL = "https://www.humblebundle.com"
BUNDLES_URL = HUMBLEBUNDLE_URL + "/bundles"
BUNDLES_TABLE = "bundles"
BUNDLES_FTS_COLUMNS = ["name", "description"]
ITEMS_TABLE = "items"
ITEMS_FTS_COLUMNS = ["name", "author", "publisher", "description"]


@dataclass
class Item:
    id: str
    type: str
    name: str
    edition: str
    author: str
    publisher: str
    description: str


@dataclass
class Bundle:
    id: str
    url: str
    category: str
    name: str
    start_date: str
    end_date: str
    description: str
    items: list[Item] = field(default_factory=list)

    def asdict(self) -> dict[str, Any]:
        return asdict(self)


def load_bundles(db_path: pathlib.Path, bundles: list[Bundle]) -> None:
    db = _open_database(db_path)
    _insert_bundles_and_items(db, bundles)


# TODO: Optimize from sqlite-utils cli is more effective, why?
# TODO: Make optimize a new cli command
#
# def optimize(db_path: pathlib.Path) -> None:
#    db = _open_database(db_path)
#    fts_tables = db.table_names(fts4=True)
#    fts_tables.extend(db.table_names(fts5=True))
#    for table in fts_tables:
#        t = cast(sqlite_utils.db.Table, db[table])
#        t.optimize()
#
#    db = _open_database(db_path)
#    db.vacuum()  # type: ignore


def _open_database(db_path: pathlib.Path) -> sqlite_utils.db.Database:
    db = sqlite_utils.Database(db_path)
    return db


def _insert_bundles_and_items(
    db: sqlite_utils.db.Database, bundles: list[Bundle]
) -> None:

    bundles_table = db.table(
        BUNDLES_TABLE,
        pk="id",
        alter=True,
        replace=True,
    )
    items_table = db.table(
        ITEMS_TABLE,
        pk="id",
        alter=True,
        replace=True,
    )

    bundles_table = cast(sqlite_utils.db.Table, bundles_table)
    items_table = cast(sqlite_utils.db.Table, items_table)

    for bundle in bundles:
        bundle_rows = bundle.asdict()
        item_rows = bundle_rows.pop("items")
        bundles_table.insert(bundle_rows).m2m(items_table, item_rows)

    bundles_table.enable_fts(
        BUNDLES_FTS_COLUMNS, tokenize="porter", create_triggers=True, replace=True
    )
    items_table.enable_fts(
        ITEMS_FTS_COLUMNS, tokenize="porter", create_triggers=True, replace=True
    )


def extract_bundles(http_client: Any, bundles_url: str) -> list[Bundle]:
    html = _get_htlm(http_client, bundles_url)
    bundles_data = _extract_bundles(html)
    bundles = _transform_bundles(bundles_data)

    for bundle in bundles:
        html = _get_htlm(http_client, HUMBLEBUNDLE_URL + bundle.url)
        items_data = _extract_items(html)
        items = _transform_items(items_data)
        bundle.items = items

    return bundles


def _get_htlm(http_client: Any, url: str) -> bytes:
    response = http_client.get(url)
    response.raise_for_status()
    html = cast(bytes, response.content)
    return html


def _extract_bundles(bundles_html: bytes) -> list[dict[str, Any]]:
    soup = bs4.BeautifulSoup(bundles_html, "html.parser")
    tag = cast(bs4.element.Tag, soup.find(id="landingPage-json-data"))
    script = cast(bs4.element.Script, tag.string)
    d = json.loads(script)
    data = d.get("data") or dict()
    bundles_data = []
    for category in data.keys():
        for section in data[category]["mosaic"]:
            bundles_data.extend(section["products"])
    return bundles_data


def _extract_items(items_html: bytes) -> list[dict[str, Any]]:
    soup = bs4.BeautifulSoup(items_html, "html.parser")
    tag = cast(bs4.element.Tag, soup.find(id="webpack-bundle-page-data"))
    script = cast(bs4.element.Script, tag.string)
    d = json.loads(script)
    data = d.get("bundleData").get("tier_item_data") or dict()
    items_data = list(data.values())
    return items_data


def _transform_bundles(bundles_data: list[dict[str, Any]]) -> list[Bundle]:
    bundles = []
    for bundle in bundles_data:

        name = bundle["tile_short_name"]
        start_date = bundle["start_date|datetime"]
        id_hash = sha1(name.encode() + start_date.encode()).hexdigest()  # noqa: S303

        short_description = bundle["short_marketing_blurb"]
        long_description = bundle["detailed_marketing_blurb"]
        description = f"{short_description} - {long_description}"

        b = Bundle(
            url=bundle["product_url"],
            category=bundle["tile_stamp"],
            name=name,
            start_date=start_date,
            end_date=bundle["end_date|datetime"],
            id=id_hash,
            description=description,
        )
        bundles.append(b)
    return bundles


def _transform_items(items_data: list[dict[str, Any]]) -> list[Item]:
    items = []
    for item in items_data:
        if not _is_item(item):
            continue

        author = ""
        if item["developers"]:
            author = item["developers"][0].get("developer-name")
            if not author:
                author = item["developers"][0].get("developer-url")

        publisher = ""
        if item["publishers"]:
            publisher = item["publishers"][0].get("publisher-name")

        name = item["human_name"]
        id_hash = sha1(name.encode() + author.encode()).hexdigest()  # noqa: S303

        i = Item(
            type=item["item_content_type"],
            author=author,
            name=name,
            publisher=publisher,
            description=item["description_text"],
            edition=item["callout"],
            id=id_hash,
            # TODO: filter out edition
            # parse with soup and extract useful part
            # <span class="callout-msrp">MSRP: $29.99<br>
            #    <span>Add on for&nbsp;Corel Painter 2021</span></span>
        )
        items.append(i)
    return items


def _is_item(item: dict[str, Any]) -> bool:
    return True if item["item_content_type"] else False
