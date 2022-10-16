import shutil as sh
import os

def move_file_to_path(dirpath, name, final_path):
    try:
        file = os.path.join(dirpath, name)
        sh.move(file, final_path)
    except Exception as e:
        print("error"+str(e))
    else:
        print("\n"+file+"\n")


origin_path = r'/media/johnpc/Salvado info 2021/'
final_path = r'/home/johnpc/Documentos/'
path_pdf = final_path+'pdf'
path_img = final_path+'img'
path_iso = final_path+'iso'
path_rar = final_path+'rar'

for dirpath, dirnames, filenames in os.walk(origin_path):
    for name in filenames:
        if name.endswith('.pdf'):
            move_file_to_path(dirpath, name, path_pdf)
        elif name.endswith('.png') or name.endswith('.jpg') or name.endswith('.jpeg'):
            move_file_to_path(dirpath, name, path_img)
        elif name.endswith('.iso'):
            move_file_to_path(dirpath, name, path_iso)
        elif name.endswith('.rar'):
            move_file_to_path(dirpath, name, path_rar)
