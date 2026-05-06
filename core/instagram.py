import instaloader
from rich.console import Console
from rich.table import Table

console = Console()

def track_instagram(username):
    loader = instaloader.Instaloader()
    try:
        console.print(f"[yellow]Fetching Instagram Intelligence for: @{username}...[/yellow]")
        profile = instaloader.Profile.from_username(loader.context, username)

        table = Table(title=f"IG Profile: {profile.username}", border_style="green")
        table.add_column("Attribute", style="bold white")
        table.add_column("Detail", style="blue")

        table.add_row("Full Name", profile.full_name)
        table.add_row("User ID", str(profile.userid))
        table.add_row("Biography", profile.biography if profile.biography else "-")
        table.add_row("Followers", f"[bold green]{profile.followers}[/bold green]")
        table.add_row("Following", str(profile.followees))
        table.add_row("Posts", str(profile.mediacount))
        table.add_row("Account Type", "Business" if profile.is_business_account else "Personal")
        table.add_row("Private", "[red]Yes[/red]" if profile.is_private else "[green]No[/green]")
        table.add_row("Verified", "[cyan]Verified[/cyan]" if profile.is_verified else "No")
        table.add_row("Profile URL", profile.profile_pic_url)

        console.print(table)
    except instaloader.exceptions.ProfileNotExistsException:
        console.print("[bold red]ERROR: Akun Instagram tidak ditemukan![/bold red]")
    except Exception as e:
        console.print(f"[bold red]Instagram Error: {e}[/bold red]")
