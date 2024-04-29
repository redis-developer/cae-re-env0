import typer

from .commands.env0 import create_env, get_env
from .commands.redis_ent import create_bdbs
from .console import console
from .env import Env

cli = typer.Typer()
cli.command()(create_env)
cli.command()(get_env)
cli.command()(create_bdbs)


def run_cli():
    if not Env.check():
        console.rule(
            ":warning: [bold red]Set required environment variables[/bold red]"
        )
        cli().help()
        exit(1)

    cli()


if __name__ == "__main__":
    run_cli()
