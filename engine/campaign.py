from pathlib import Path
from datetime import datetime

FILE = Path(__file__).parent.parent / "memory" / "campaign.md"


def append(player_text: str, assistant_text: str):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE, "a", encoding="utf-8") as f:
        f.write("\n---\n\n")
        f.write(f"## {now}\n\n")
        f.write("### PLAYER\n\n")
        f.write(player_text.strip())
        f.write("\n\n")
        f.write("### CHATGPT\n\n")
        f.write(assistant_text.strip())
        f.write("\n")


def read():

    if not FILE.exists():
        return ""

    return FILE.read_text(encoding="utf-8")