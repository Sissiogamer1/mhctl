import typer
import inspect
from mhctl.core import settings # type: ignore

app = typer.Typer()
settings_app = typer.Typer()
app.add_typer(settings_app, name="settings")

funcs_names = ["list_providers", "provider_info"]

for func_name in funcs_names:
    func = getattr(settings, func_name)
    settings_app.command(name=func_name)(func)

#@app.command()
#def func():
#    print