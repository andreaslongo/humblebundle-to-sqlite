from setuptools import setup, find_packages


setup(
    name="humblebundle-to-sqlite",
    description="Load data from humblebundle.com into a SQLite database.",
    author="Andreas Longo",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": ["humblebundle-to-sqlite=humblebundle_to_sqlite.cli:cli"],
    },
    install_requires=[
        "beautifulsoup4==4.10.0",
        "httpx==0.20.0",
        "sqlite-utils==3.17.1",
        "typer==0.4.0",
    ],
)
