#!/usr/bin/env python3
"""
Verschiebt Verzeichnisse der Form:
  - JJJJ.MM.TT
  - TT.MM.JJJJ
in die Struktur JJJJ/MM/
"""

import re
import shutil
from pathlib import Path

# Zwei mögliche Formate
PATTERN_YMD = re.compile(r"^(\d{4})\.(\d{1,2})\.(\d{1,2})$")   # 2024.05.12
PATTERN_DMY = re.compile(r"^(\d{1,2})\.(\d{1,2})\.(\d{4})$")   # 12.05.2024


def parse_date_dir(name: str) -> tuple[str, str] | None:
    """
    Versucht den Verzeichnisnamen zu parsen.
    Gibt (Jahr, Monat) zurück oder None, wenn kein gültiges Format.
    """
    # Zuerst Jahr.Monat.Tag versuchen
    match = PATTERN_YMD.match(name)
    if match:
        year, month, _ = match.groups()
        return year, f"{int(month):02d}"

    # Dann Tag.Monat.Jahr versuchen
    match = PATTERN_DMY.match(name)
    if match:
        _, month, year = match.groups()
        return year, f"{int(month):02d}"

    return None


def move_date_dirs(root_dir: str | Path, dry_run: bool = False) -> None:
    root = Path(root_dir).resolve()

    if not root.is_dir():
        print(f"Fehler: '{root}' ist kein Verzeichnis.")
        return

    print(f"Durchsuche: {root}\n")

    moved = 0
    skipped = 0

    for entry in root.iterdir():
        if not entry.is_dir():
            continue

        parsed = parse_date_dir(entry.name)
        if not parsed:
            continue

        year, month = parsed
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
        description="Verschiebt Verzeichnisse der Form JJJJ.MM.TT oder TT.MM.JJJJ in JJJJ/MM/"
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
    move_date_dirs(args.verzeichnis, dry_run=args.dry_run)

