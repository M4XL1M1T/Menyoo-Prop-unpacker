# Anleitung zur Nutzung des Scripts

## 1. Python installieren
1. Lade die aktuelle Version von **Python 3.11 oder neuer** herunter:  
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. Während der Installation unbedingt den Haken bei **"Add Python to PATH"** setzen.  
3. Nach der Installation ein Terminal (Eingabeaufforderung) öffnen und testen:  
   ```bash
   python --version
   ```

## 2. Benötigte Abhängigkeiten installieren
Das Script benötigt zusätzliche Python-Pakete.  
Im Terminal im Projektordner ausführen:

```bash
pip install rarfile
```

> Hinweis: Das Script nutzt **WinRAR** zum Entpacken.  
> Stelle sicher, dass WinRAR installiert ist und sich die Datei `UnRAR.exe` im Pfad befindet:  
> `C:\Program Files\WinRAR\UnRAR.exe`

Falls WinRAR woanders installiert ist, den Pfad im Script anpassen:
```python
rarfile.UNRAR_TOOL = r"C:\Pfad\zu\UnRAR.exe"
```

## 3. Ordnerstruktur vorbereiten
Lege im gleichen Verzeichnis wie das Script einen Ordner `propfiles` an.  
Dort alle `.rar`-Archive ablegen, die verarbeitet werden sollen.

Beispiel:
```
Projektordner/
│
├─ main.py
├─ propfiles/
│   ├─ deineprops1.rar
│   ├─ deineprops2.rar
```

## 4. Script ausführen
Im Projektordner:
```bash
python main.py
```

- Es werden alle `.rar` im Ordner `propfiles` entpackt.  
- Aus den `.ydr`-Dateien werden zwei Listen erzeugt:  
  - **1_proplist.txt**  
  - **2_propfav.txt**  
- Optional können die `.rar` und andere Dateien nach dem Entpacken gelöscht werden (Abfrage im Script).  
