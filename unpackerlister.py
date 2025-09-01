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

    confirm_delete = input("Sollen entpackte RARs und bestimmte Dateien gelöscht werden? (j/n): ").lower() == 'j'


    for filename in os.listdir(base_path):
        if filename.lower().endswith('.rar'):
            rar_path = os.path.join(base_path, filename)
            try:
                with rarfile.RarFile(rar_path) as rf:
                    rf.extractall(base_path)
                if confirm_delete:
                    os.remove(rar_path)  # RAR nach Entpacken löschen
                    print(f"Entpackt und gelöscht: {filename}")
                else:
                    print(f"Entpackt, aber nicht gelöscht: {filename}")
            except Exception as e:
                print(f"Fehler beim Entpacken von {filename}: {e}")


    ydr_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith('.ydr'):
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

 
    keep_files = {'1_proplist.txt', '2_propfav.txt'}
    delete_extensions = {'.ydr', '.png', '.dds', '.jpg', '.jpeg'}

    if confirm_delete:
        for filename in os.listdir(base_path):
            if filename in keep_files:
                continue
            file_path = os.path.join(base_path, filename)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                if ext.lower() in delete_extensions:
                    try:
                        os.remove(file_path)
                        print(f"Gelöscht: {filename}")
                    except Exception as e:
                        print(f"Fehler beim Löschen von {filename}: {e}")
            elif os.path.isdir(file_path):
                try:
                    shutil.rmtree(file_path)
                    print(f"Ordner gelöscht: {filename}")
                except Exception as e:
                    print(f"Fehler beim Löschen des Ordners {filename}: {e}")
    else:
        print("Keine Dateien gelöscht (Bestätigung verweigert).")


if __name__ == "__main__":
    run_and_process_files()