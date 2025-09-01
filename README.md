# 📦 Menyoo Prop Unpacker & Lister

Ein kleines Python-Tool, das `.rar`-Archive im Ordner **`propfiles`** automatisch entpackt, `.ydr`-Dateien auflistet und daraus zwei Dateien generiert:

- **1_proplist.txt** → XML-Liste aller Props  
- **2_propfav.txt** → Favoriten-Liste aller Props  

Optional kannst du entpackte Archive und Dateien nach Bestätigung automatisch löschen lassen.

---

## 🚀 Features

- Entpackt alle `.rar`-Archive mit **UnRAR**
- Findet alle `.ydr`-Dateien
- Erstellt automatisch:
  - `1_proplist.txt` (XML-Struktur)
  - `2_propfav.txt` (PropModel-Liste)
- Optionale Löschfunktion:
  - Entfernt `.rar`, `.ydr`, `.png`, `.dds`, `.jpg`, `.jpeg`
  - Löscht Ordner
  - Behalte nur die beiden Ergebnis-Dateien
- Ausgabe im Konsolenstil (Statusmeldungen)

---

## 📂 Ordnerstruktur

```text
Menyoo-Prop-unpacker-main/
│
├── unpackerlister.py   # Hauptskript
├── propfiles/          # .rar-Archive hier hineinlegen
└── dist/               # (optional) fertige EXE nach Build mit PyInstaller

⚠️ Hinweis zu Antivirus-Erkennungen

Einige Antivirenprogramme stufen die EXE als „Dropper“ ein.
Das liegt daran, dass das Tool Dateien entpackt und löscht.
Es handelt sich dabei um False Positives.

Tipps zur Reduzierung:

--noupx verwenden

EXE digital signieren (falls möglich)

oder alternativ Nuitka nutzen (statt PyInstaller)
