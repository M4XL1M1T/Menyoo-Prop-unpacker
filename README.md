# 📦 Menyoo Prop Unpacker & Lister
# https://www.gta5-mods.com/tools/menyoo-prop-unpack-helper

A small Python tool that automatically extracts `.rar` archives, lists `.ydr` files, and generates two files from them:

- **def_props.ytyp.xml** → XML list of all props
- **FavouriteProps.xml** → Favorites list of all props


---

## 🚀 Features

- Extracts all `.rar` & `.zip` archives in the folder `put your props or zipped files here`
 - If you have individual props, you can also put them in the folder; they will be included as well.
 - Automatically creates:
  > `def_props.ytyp.xml` 
  > `FavouriteProps.xml`

## 🧐 How to Use
- Step 1. Download latest Release
- Step 2. Extract the rar file to a desired location.
- Step 3. Run the Unpacker.exe (don't use it yet! :D)
- Step 4. open the folder `put your props or zipped files here`
- Step 5. Put your .ZIP, .RAR or .YDR files in there
- Step 6. Go back to the Unpacker.exe and type `Y` to start the magic
- Step 7. Import the `def_props.ytyp.xml` to OpenIV to `mods\update\x64\dlcpacks\addonprops\dlc.rpf\props.rpf\` with `New` > `Import OpenFormats` > Click `OK` > Done
- Step 8. Put all the files from the Folder `Props` to OpenIV > `mods\update\x64\dlcpacks\addonprops\dlc.rpf\props.rpf\`
- Step 9. Don't forget to put the `FavouriteProps.xml` in your existing `FavouriteProps.xml` :D
 
## Update - 1.3
  -> I developed this program some time ago so I could work with it quickly; the other, widely used tool was unnecessary and really bad because you had to drag in each prop individually xD 
  
- I initially thought the prompt to delete files was necessary, but it was an unnecessary step, so I removed it. If you want to delete the files, simply empty the folder > Ctrl + A + DEL
- Fully Translated to English xD
- renamed folders and files to match the original files in menyoo and openiv
- Forgot to include zip files xD
