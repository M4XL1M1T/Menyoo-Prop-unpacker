import os
import sys
import rarfile
import zipfile
import shutil

rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"


def unpack_archives_and_generate_list():
    folder = 'put your props or zipped files here'
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(script_dir, folder)
    return base_path


def run_and_process_files():
    base_path = unpack_archives_and_generate_list()

    confirm_delete = input("Do you want to extract RAR and ZIP files? (y/n): ").lower() == 'y'

    for filename in os.listdir(base_path):
        lower = filename.lower()
        if lower.endswith('.rar') or lower.endswith('.zip'):
            file_path = os.path.join(base_path, filename)
            try:
                if lower.endswith('.rar'):
                    with rarfile.RarFile(file_path) as rf:
                        rf.extractall(base_path)
                else:
                    with zipfile.ZipFile(file_path) as zf:
                        zf.extractall(base_path)
                if confirm_delete:
                    os.remove(file_path)
                    print(f"Extracted and deleted: {filename}")
                else:
                    print(f"Extracted, but not deleted: {filename}")
            except Exception as e:
                print(f"Error extracting {filename}: {e}")


    ydr_files = []
    ydr_set = set()
    props_dir = os.path.join(base_path, 'props')
    os.makedirs(props_dir, exist_ok=True)
    for root, dirs, files in os.walk(base_path):
        if os.path.abspath(root) == os.path.abspath(props_dir):
            continue
        for file in files:
            if file.lower().endswith('.ydr'):
                src_path = os.path.join(root, file)
                dst_path = os.path.join(props_dir, file)
                propname = os.path.splitext(file)[0]
                if propname in ydr_set:
                    print(f"Skipping duplicate prop name: {propname}")
                    try:
                        if os.path.abspath(src_path) != os.path.abspath(dst_path) and os.path.exists(src_path):
                            os.remove(src_path)
                    except Exception:
                        pass
                    continue
                try:
                    if os.path.abspath(src_path) != os.path.abspath(dst_path):
                        if os.path.exists(dst_path):
                            print(f"Destination already exists for {file}; skipping move.")
                        else:
                            shutil.move(src_path, dst_path)
                            print(f"Moved: {file} -> props")
                    else:
                        print(f"Already in props: {file}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")
                ydr_set.add(propname)
                ydr_files.append(propname)

    xml_header = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    xml_header += '<CMapTypes>\n'
    xml_header += '  <extensions/>\n'
    xml_header += '  <archetypes>\n'

    item_template = (
        '    <Item type="CBaseArchetypeDef">\n'
        '      <lodDist value="500.00000000"/>\n'
        '      <flags value="32"/>\n'
        '      <specialAttribute value="0"/>\n'
        '      <bbMin x="0.00000000" y="0.00000000" z="0.00000000"/>\n'
        '      <bbMax x="0.00000000" y="0.00000000" z="0.00000000"/>\n'
        '      <bsCentre x="0.00000000" y="0.00000000" z="0.00000000"/>\n'
        '      <bsRadius value="0.00000000"/>\n'
        '      <hdTextureDist value="5.00000000"/>\n'
        '      <name>{propname}</name>\n'
        '      <textureDictionary>{propname}</textureDictionary>\n'
        '      <clipDictionary/>\n'
        '      <drawableDictionary/>\n'
        '      <physicsDictionary>{propname}</physicsDictionary>\n'
        '      <assetType>ASSET_TYPE_DRAWABLE</assetType>\n'
        '      <assetName>{propname}</assetName>\n'
        '      <extensions/>\n'
        '    </Item>\n'
    )

    xml_footer = '  </archetypes>\n'
    xml_footer += '  <name>0x2FB8F27A</name>\n'
    xml_footer += '  <dependencies/>\n'
    xml_footer += '  <compositeEntityTypes/>\n'
    xml_footer += '</CMapTypes>\n'

    with open(os.path.join(base_path, 'def_props.ytyp.xml'), 'w', encoding='utf-8') as out:
        out.write(xml_header)
        for propname in ydr_files:
            out.write(item_template.format(propname=propname))
        out.write(xml_footer)


    propfav_path = os.path.join(base_path, 'FavouriteProps.xml')
    with open(propfav_path, 'w', encoding='utf-8') as fav_out:
        for propname in ydr_files:
            fav_out.write(f'<PropModel modelName="{propname}" modelHash="" />\n')


if __name__ == "__main__":

    run_and_process_files()
