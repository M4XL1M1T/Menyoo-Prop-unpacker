# Props Unpacker

Mit diesem Tool kannst du .rar-Dateien aus dem Ordner `propfiles` automatisch entpacken und alle `.ydr`-Dateien in eine Liste im XML-Format schreiben.

## Voraussetzungen
- Windows-Betriebssystem
- WinRAR installiert (für das Entpacken der .rar-Dateien)
- Python > https://www.python.org/downloads/release/python-31211/

## Nutzung
1. Lege alle .rar-Dateien, die du entpacken möchtest, in den Ordner `propfiles`.
2. Starte die Datei `unpackerlister.py` (Python muss installiert sein)
3. Das Tool führt die Batch-Datei zum Entpacken aus, löscht die .rar-Dateien und erstellt eine Datei `proplist.txt` mit allen gefundenen `.ydr`-Dateien im richtigen Format.

### Alternativ: Batch-Datei direkt nutzen
Du kannst auch die Batch-Datei `unpack_rar.bat` im Ordner `propfiles` ausführen, um nur die .rar-Dateien zu entpacken.

## Weitergabe
Um das Tool ohne Python zu nutzen, kannst du mit PyInstaller eine EXE erstellen:

```
pip install pyinstaller
pyinstaller --onefile unpackerlister.py
```
Die EXE findest du im Ordner `dist`.

## Hinweise
- WinRAR muss installiert und unter `C:\Program Files\WinRAR\WinRAR.exe` erreichbar sein falls es nicht dort installiert ist ändert einfach den pfad "C:\Program Files\WinRAR\" zu eurem.
- Die .ydr-Dateien können in beliebigen Unterordnern von `propfiles` liegen.
- Die generierte `proplist.txt` enthält alle Props im gewünschten XML-Format.
- einzelne props findet er ebenfalls.
