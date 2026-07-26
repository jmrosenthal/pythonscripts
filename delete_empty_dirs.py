
#!/usr/bin/env python3
"""
Löscht rekursiv alle leeren Verzeichnisse.
"""

from pathlib import Path

def delete_empty_dirs(root_dir: str | Path, dry_run: bool = False) -> None:
    root = Path(root_dir).resolve()

    if not root.is_dir():
        print(f"Fehler: '{root}' ist kein Verzeichnis.")
        return

    print(f"Durchsuche: {root}\n")

    deleted = 0

    # Bottom-up gehen, damit Unterverzeichnisse zuerst gelöscht werden
    for dirpath in sorted(root.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if not dirpath.is_dir():
            continue

        # Prüfen, ob das Verzeichnis leer ist
        try:
            if any(dirpath.iterdir()):
                continue
        except PermissionError:
            print(f"  Keine Berechtigung: {dirpath}")
            continue

        if dry_run:
            print(f"  [DRY-RUN] würde löschen: {dirpath}")
        else:
            try:
                dirpath.rmdir()
                print(f"  Gelöscht: {dirpath}")
                deleted += 1
            except OSError as e:
                print(f"  Fehler beim Löschen von {dirpath}: {e}")

    print(f"\nFertig. Gelöschte Verzeichnisse: {deleted}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Löscht rekursiv alle leeren Verzeichnisse"
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
        help="Nur anzeigen, was gelöscht würde (nichts löschen)",
    )

    args = parser.parse_args()
    delete_empty_dirs(args.verzeichnis, dry_run=args.dry_run)

