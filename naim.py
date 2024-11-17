from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel

console = Console()

# Game state
inventory = []
current_room = "Entrance"
game_over = False

# Room descriptions
rooms = {
  "Entrance": {
    "description": "You stand at the entrance of a dark, abandoned mansion. The door behind you creaks ominously.",
    "items": ["torch"],
    "exits": ["Hallway"]
  },
  "Hallway": {
    "description": "A long, narrow hallway stretches before you, with paintings of grim-faced ancestors lining the walls.",
    "items": [],
    "exits": ["Entrance", "Library", "Kitchen"]
  },
  "Library": {
    "description": "The library is filled with dusty old books. A large fireplace dominates one wall.",
    "items": ["book"],
    "exits": ["Hallway"]
  },
  "Kitchen": {
    "description": "The kitchen is cluttered with dirty dishes and rusty utensils. There's an odd smell lingering in the air.",
    "items": ["key"],
    "exits": ["Hallway"]
  },
  "Cellar": {
    "description": "The cellar is dark and damp. You can barely see anything without a light.",
    "items": ["treasure"],
    "exits": ["Kitchen"]
  }
}

def display_room(room):
  """Displays the current room description and items."""
  console.print(Panel.fit(f"[bold cyan]{room}[/bold cyan]", subtitle="Current Location"))
  console.print(Text(rooms[room]["description"], style="green"))
  
  if rooms[room]["items"]:
    console.print("\n[bold yellow]You see:[/bold yellow]")
    for item in rooms[room]["items"]:
      console.print(f"  - {item}")

  console.print("\n[bold magenta]Exits:[/bold magenta]")
  for exit in rooms[room]["exits"]:
    console.print(f"  - {exit}")

def handle_command(command):
  """Handles player commands."""
  global current_room, game_over
  words = command.lower().split()

  if "go" in words:
    for exit in rooms[current_room]["exits"]:
      if exit.lower() in words:
        current_room = exit
        display_room(current_room)
        return

    console.print("\n[red]You can't go that way![/red]")

  elif "take" in words:
    for item in rooms[current_room]["items"]:
      if item.lower() in words:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        console.print(f"\n[green]You picked up the {item}.[/green]")

        if item == "key" and "Cellar" not in rooms["Kitchen"]["exits"]:
          rooms["Kitchen"]["exits"].append("Cellar")
          console.print("\n[bold magenta]A hidden door to the Cellar has been revealed![/bold magenta]")
        
        if item == "treasure":
          console.print("\n[bold gold]Congratulations! You've found the hidden treasure! You win![/bold gold]")
          game_over = True
        return

    console.print("\n[red]There's nothing like that here![/red]")

  elif "inventory" in words or "items" in words:
    if inventory:
      console.print("\n[bold cyan]Your inventory contains:[/bold cyan]")
      for item in inventory:
        console.print(f"  - {item}")
    else:
      console.print("\n[bold cyan]Your inventory is empty.[/bold cyan]")

  else:
    console.print("\n[red]I don't understand that command.[/red]")

def main():
  console.print("[bold magenta]Welcome to the Mansion Adventure![/bold magenta]\n")
  display_room(current_room)

  while not game_over:
    command = Prompt.ask("\nWhat do you want to do?", default="look")
    handle_command(command)

  console.print("\n[bold green]Thank you for playing![/bold green]")

if __name__ == "__main__":
  main()