from pathlib import Path
from shutil import copyfile
from subprocess import run as run_command
from tempfile import TemporaryDirectory

import httpx
from typer import Typer

app = Typer()


@app.command()
def copy_from_src():
    """Copy updated files from src to logto_admin."""
    copyfile("./src/token_manager.py", "./logto_admin/token_manager.py")


@app.command()
def generate(url: str):
    """
    Generate Logto Admin API client.

    This will overwrite the existing client.
    """

    # fetch the openapi spec
    openapi_resp = httpx.get(url)
    openapi_resp.raise_for_status()

    with TemporaryDirectory() as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        openapi_temp_path = temp_dir / "openapi.json"

        # save the openapi spec
        with open(openapi_temp_path, "wb") as f:
            f.write(openapi_resp.content)

        # generate the client
        run_command(
            [
                "openapi-python-client",
                "generate",
                "--meta=none",
                "--output-path=logto_admin",
                "--overwrite",
                "--path",
                str(openapi_temp_path),
                "--config",
                "./src/config.yaml",
                "--custom-template-path=./src/templates",
            ],
            check=False,
        )

    with open("./logto_admin/py.typed", "w", encoding="utf-8") as f:
        f.write("# Marker file for PEP 561")

    copy_from_src()


if __name__ == "__main__":
    app()
