import typer
from .core import settings # type: ignore
import httpx

__version__ = "0.0.1"

app = typer.Typer(
    help="Help text placeholder"
)
settings_app = typer.Typer()
app.add_typer(settings_app, name="settings")

funcs_names = ["list_providers", "provider_info"]

for func_name in funcs_names:
    func = getattr(settings, func_name)
    settings_app.command(name=func_name)(func)

def version_callback(value: bool):
    if value:
        typer.echo(f"Placeholder header\nVersion 0.0.1\nRelease date: 20/01/2026")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None, 
        "--version", 
        callback=version_callback, 
        is_eager=True,
        help="Help text placeholder"
    )
):
    pass

@app.command()
def upload(
        file: str,
        provider: str = typer.Argument(None, help="Provider (default from config)"),
):
    if provider:
        try:
            from .runtime.internal import is_provider_supported
            provider_supported = is_provider_supported(provider)
            print(provider_supported)
        except ValueError as e:
            typer.echo(e)
    elif provider is None:
        try:
            from .runtime.internal import get_default_provider
            provider = get_default_provider()
            print(provider)
        except ValueError as e:
            typer.echo(e)
    if provider == "uguu.se":
        try:
            from .core.upload import upload_pomf
            response = upload_pomf(file, provider)
            typer.echo(response)

        except ValueError as e:
            typer.echo(e)