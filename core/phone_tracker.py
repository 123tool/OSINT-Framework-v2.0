import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from rich.table import Table
from rich.console import Console

console = Console()

def track_phone(number):
    try:
        # Auto-fix jika user lupa masukin '+'
        if not number.startswith('+'):
            number = "+" + number
            
        parsed = phonenumbers.parse(number)
        
        if not phonenumbers.is_valid_number(parsed):
            console.print("[bold red]ERROR: Nomor tidak valid![/bold red]")
            return

        table = Table(title=f"Results for {number}", border_style="cyan")
        table.add_column("Information", style="bold white")
        table.add_column("Value", style="green")

        table.add_row("Location", geocoder.description_for_number(parsed, "id"))
        table.add_row("Carrier / ISP", carrier.name_for_number(parsed, "en"))
        table.add_row("Timezone", str(timezone.time_zones_for_number(parsed)))
        table.add_row("International Format", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
        table.add_row("Type", "Mobile" if phonenumbers.number_type(parsed) == 1 else "Fixed Line/Other")
        table.add_row("WA Link", f"https://wa.me/{number.replace('+', '')}")

        console.print(table)
    except Exception as e:
        console.print(f"[bold red]Failed to track: {e}[/bold red]")
