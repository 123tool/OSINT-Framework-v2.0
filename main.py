import sys
import os
from rich.console import Console
from core.banner import print_banner, loading_animation
from core.phone_tracker import track_phone
from core.ip_tracker import track_ip
from core.instagram import track_instagram

console = Console()

def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print_banner()
        
        console.print("\n[bold cyan]Main Menu:[/bold cyan]")
        console.print(" [1] [white]Phone Tracker[/white]")
        console.print(" [2] [white]IP Intelligence[/white]")
        console.print(" [3] [white]Instagram Scraper[/white]")
        console.print(" [0] [red]Exit / Quit[/red]")
        
        choice = console.input("\n[bold yellow]SPYE-OSINT[/bold yellow] > ")

        if choice == "1":
            num = console.input("[bold white]Enter Number (e.g. 628xxx): [/bold white]")
            track_phone(num)
            console.input("\n[dim]Press Enter to return...[/dim]")
        
        elif choice == "2":
            ip = console.input("[bold white]Enter Target IP: [/bold white]")
            track_ip(ip)
            console.input("\n[dim]Press Enter to return...[/dim]")

        elif choice == "3":
            user = console.input("[bold white]Enter IG Username: [/bold white]")
            track_instagram(user)
            console.input("\n[dim]Press Enter to return...[/dim]")

        elif choice == "0":
            console.print("[bold red]Shutting down SPYE-OSINT... Goodbye![/bold red]")
            sys.exit()
            
        else:
            console.print("[bold red]Invalid option![/bold red]")
            import time
            time.sleep(1)

if __name__ == "__main__":
    try:
        loading_animation()
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interrupted by user. Exiting...[/bold red]")
        sys.exit()
