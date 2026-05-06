import requests
from rich.console import Console
from rich.table import Table

console = Console()

def track_ip(ip):
    try:
        console.print(f"[yellow]Scanning Target IP: {ip}...[/yellow]")
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719").json()
        
        if res['status'] == 'fail':
            console.print("[bold red]IP not found or invalid![/bold red]")
            return

        table = Table(title=f"IP Intel: {ip}", border_style="magenta")
        table.add_column("Data Points", style="bold white")
        table.add_column("Result", style="yellow")

        table.add_row("Country", f"{res['country']} ({res['countryCode']})")
        table.add_row("Region/City", f"{res['regionName']}, {res['city']}")
        table.add_row("ISP", res['isp'])
        table.add_row("Organization", res['org'])
        table.add_row("Lat/Lon", f"{res['lat']}, {res['lon']}")
        table.add_row("Maps", f"https://www.google.com/maps?q={res['lat']},{res['lon']}")
        
        console.print(table)
    except Exception as e:
        console.print(f"[bold red]System Error: {e}[/bold red]")
