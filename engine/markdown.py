from pathlib import Path

MEMORY_DIR = Path(__file__).parent.parent / "memory"


def get_path(filename: str) -> Path:
    return MEMORY_DIR / filename


def load(filename: str) -> dict:
    path = get_path(filename)

    if not path.exists():
        return {}

    sections = {}
    current = None
    buffer = []

    for line in path.read_text(encoding="utf-8").splitlines():

        if line.startswith("# "):
            continue

        if line.startswith("## "):

            if current is not None:
                sections[current] = "\n".join(buffer).strip()

            current = line[3:].strip()
            buffer = []

        elif current is not None:
            buffer.append(line)

    if current is not None:
        sections[current] = "\n".join(buffer).strip()

    return sections


def save(filename: str, sections: dict):

    path = get_path(filename)

    title = path.stem.replace("_", " ").title()

    lines = [f"# {title}", ""]

    for key, value in sections.items():

        lines.append(f"## {key}")
        lines.append("")

        if value:
            lines.append(value)

        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")