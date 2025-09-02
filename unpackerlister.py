import os
import sys
import rarfile
import shutil

rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"


def unpack_archives_and_generate_list():
    folder = 'propfiles'
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(script_dir, folder)
    return base_path


def run_and_process_files():
    base_path = unpack_archives_and_generate_list()

    confirm_delete = input("Willst du die RAR-Datein Entpacken (j/n): ").lower() == 'j'
    

    for filename in os.listdir(base_path):
        if filename.lower().endswith('.rar'):
            rar_path = os.path.join(base_path, filename)
            try:
                with rarfile.RarFile(rar_path) as rf:
                    rf.extractall(base_path)
                if confirm_delete:
                    os.remove(rar_path) 
                    print(f"Entpackt und gelöscht: {filename}")
                else:
                    print(f"Entpackt, aber nicht gelöscht: {filename}")
            except Exception as e:
                print(f"Fehler beim Entpacken von {filename}: {e}")


    ydr_files = []
    props_dir = os.path.join(base_path, 'props')
    os.makedirs(props_dir, exist_ok=True)
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith('.ydr'):
                src_path = os.path.join(root, file)
                dst_path = os.path.join(props_dir, file)
                try:
                    shutil.move(src_path, dst_path)
                    print(f"Verschoben: {file} -> props")
                except Exception as e:
                    print(f"Fehler beim Verschieben von {file}: {e}")
                ydr_files.append(os.path.splitext(file)[0])


    xml_template = '''<Item type="CBaseArchetypeDef">
  <lodDist value="500.00000000"/>
  <flags value="32"/>
  <specialAttribute value="0"/>
  <bbMin x="0.00000000" y="0.00000000" z="0.00000000"/>
  <bbMax x="0.00000000" y="0.00000000" z="0.00000000"/>
  <bsCentre x="0.00000000" y="0.00000000" z="0.00000000"/>
  <bsRadius value="0.00000000"/>
  <hdTextureDist value="5.00000000"/>
  <name>{propname}</name>
  <textureDictionary>{propname}</textureDictionary>
  <clipDictionary/>
  <drawableDictionary/>
  <physicsDictionary>{propname}</physicsDictionary>
  <assetType>ASSET_TYPE_DRAWABLE</assetType>
  <assetName>{propname}</assetName>
  <extensions/>
</Item>\n'''
    with open(os.path.join(base_path, '1_proplist.txt'), 'w', encoding='utf-8') as out:
        for propname in ydr_files:
            out.write(xml_template.format(propname=propname))


    propfav_path = os.path.join(base_path, '2_propfav.txt')
    with open(propfav_path, 'w', encoding='utf-8') as fav_out:
        for propname in ydr_files:
            fav_out.write(f'<PropModel modelName="{propname}" modelHash="" />\n')

    print(" ")
    print(" ")
    print("------------------------------------------------------")
    print(f"Du kannst nun die .ydr-Dateien nach OIV verschieben.")
    print("------------------------------------------------------")
    print(" ")
    print(" ")
    confirm_delete_ydr = input("Sollen die verschobenen .ydr-Dateien im props-Ordner gelöscht werden? (j/n): ").lower() == 'j'
    if confirm_delete_ydr:
        for file in os.listdir(props_dir):
            if file.lower().endswith('.ydr'):
                file_path = os.path.join(props_dir, file)
                try:
                    os.remove(file_path)
                    print(f"Gelöscht: {file}")
                except Exception as e:
                    print(f"Fehler beim Löschen von {file}: {e}")
    else:
        print(".ydr-Dateien im props-Ordner wurden nicht gelöscht.")


if __name__ == "__main__":
    run_and_process_files()
