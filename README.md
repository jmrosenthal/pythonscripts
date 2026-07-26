# pythonscripts

## Verzeichnis-Verschiebe-Skript: move_date_dirs.py

Verschiebt Verzeichnisse der Form **`JJJJ.MM.TT`** oder **`TT.MM.JJJJ`**  
in die Struktur **`JJJJ/MM/`**.

### Unterstützte Formate

| Verzeichnisname | Zielverzeichnis |
|-----------------|-----------------|
| `2024.05.12`    | `2024/05/`      |
| `12.05.2024`    | `2024/05/`      |
| `2023.1.5`      | `2023/01/`      |
| `5.1.2023`      | `2023/01/`      |
| `1999.12.31`    | `1999/12/`      |
| `31.12.1999`    | `1999/12/`      |

### Im aktuellen Verzeichnis ausführen
```python move_date_dirs.py```

### Bestimmtes Verzeichnis angeben
```python move_date_dirs.py /pfad/zum/ordner```

### Erstmal nur anschauen, was passieren würde
```python move_date_dirs.py /pfad/zum/ordner --dry-run```



