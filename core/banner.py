import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_banner():
    banner_text = """
    ███████╗██████╗ ██╗   ██╗      ███████╗
    ██╔════╝██╔══██╗╚██╗ ██╔╝      ██╔════╝
    ███████╗██████╔╝ ╚████╔╝ █████╗█████╗  
    ╚════██║██╔═══╝   ╚██╔╝  ╚════╝██╔══╝  
    ███████║██║        ██║         ███████╗
    ╚══════╝╚═╝        ╚═╝         ╚══════╝
    [ Open Source Intelligence Framework ]
    """
    panel = Panel(
        Text(banner_text, style="bold cyan"),
        subtitle="[bold white]V2.0 - Powered by SPY-E / 123Tool[/bold white]",
        border_style="bright_blue"
    )
    console.print(panel)

def loading_animation():
    with console.status("[bold green]Initializing SPYE-OSINT Modules...") as status:
        time.sleep(1.5)
