 #!/usr/bin/env python3
"""
Verschiebt Dateien der Form YYYY-MM-DD_...
in die Struktur JJJJ/MM/
"""

import re
import shutil
from pathlib import Path

# Erwartetes Format am Anfang des Dateinamens: 2026-02-05_
PATTERN = re.compile(r"^(\d{4})-(\d{2})-(\d{2})_")


def move_date_files(root_dir: str | Path, dry_run: bool = False) -> None:
    root = Path(root_dir).resolve()

    if not root.is_dir():
        print(f"Fehler: '{root}' ist kein Verzeichnis.")
        return

    print(f"Durchsuche: {root}\n")

    moved = 0
    skipped = 0

    for entry in root.iterdir():
        if not entry.is_file():
            continue

        match = PATTERN.match(entry.name)
        if not match:
            continue

        year, month, _ = match.groups()
        target_dir = root / year / month
        target_path = target_dir / entry.name

        if target_path.exists():
            print(f"  Übersprungen (Ziel existiert bereits): {entry.name}")
            skipped += 1
            continue

        if dry_run:
            print(f"  [DRY-RUN] würde verschieben: {entry.name}  →  {year}/{month}/")
        else:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(entry), str(target_path))
            print(f"  Verschoben: {entry.name}  →  {year}/{month}/")

        moved += 1

    print(f"\nFertig. Verschoben: {moved}, Übersprungen: {skipped}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Verschiebt Dateien der Form YYYY-MM-DD_... in JJJJ/MM/"
    )
    parser.add_argument(
        "verzeichnis",
        nargs="?",
        default=".",
        help="Zu durchsuchendes Verzeichnis (Standard: aktuelles Verzeichnis)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Nur anzeigen, was gemacht würde (nichts verschieben)",
    )

    args = parser.parse_args()
    move_date_files(args.verzeichnis, dry_run=args.dry_run)
  
