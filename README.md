## Hilfsskripte

### 1. Verzeichnisse nach Datum sortieren

Verschiebt Verzeichnisse der Form `JJJJ.MM.TT` oder `TT.MM.JJJJ` in die Struktur `JJJJ/MM/`.

**Skript:** [move_date_dirs.py](move_date_dirs.py)

**Verwendung:**
```bash
python move_date_dirs.py
python move_date_dirs.py --dry-run
python move_date_dirs.py /pfad/zum/ordner
```

### 2. Dateien nach Datum sortieren

Verschiebt Dateien der Form YYYY-MM-DD_... (z. B. 2026-02-05_Theresa_Finn__...) in die Struktur JJJJ/MM/.

**Skript:** [move_date_files.py](move_date_files.py)

**Verwendung:**
```bash
python move_date_files.py
python move_date_files.py --dry-run
python move_date_files.py /pfad/zum/ordner
```

### 3. Leere Verzeichnisse löschen

Löscht rekursiv alle leeren Verzeichnisse.

**Skript:** [delete_empty_dirs.py](delete_empty_dirs.py)

**Verwendung:**
```bash
python delete_empty_dirs.py
python delete_empty_dirs.py --dry-run
python delete_empty_dirs.py /pfad/zum/ordner
```


