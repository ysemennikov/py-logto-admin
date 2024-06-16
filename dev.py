from shutil import copyfile
from subprocess import run as run_command

from jinja2 import Environment, FileSystemLoader
from typer import Typer

app = Typer()
j2_env = Environment(loader=FileSystemLoader("./src"))


@app.command()
def copy_from_src():
    """Copy updated files from src to logto_admin."""
    copyfile("./src/token_manager.py", "./logto_admin/token_manager.py")

    with open("./logto_admin/__init__.py", "w", encoding="utf-8") as f:
        f.write(j2_env.get_template("__init__.jinja").render())


@app.command()
def generate(url: str):
    """
    Generate Logto Admin API client.

    This will overwrite the existing client.
    """

    run_command(
        [
            "openapi-python-client",
            "generate",
            "--meta=none",
            "--output-path=logto_admin",
            "--overwrite",
            "--url",
            url,
            "--config",
            "./src/config.yaml",
        ],
        check=False,
    )
    copy_from_src()


if __name__ == "__main__":
    app()
