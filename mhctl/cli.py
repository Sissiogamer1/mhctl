import typer
from mhctl.core import settings # type: ignore

__version__ = "0.0.0.2"

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
        typer.echo(f"Placeholder header\nVersion 0.0.0.2\nRelease date: 22/12/2025")
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

#@app.command()
#def func():
#    print