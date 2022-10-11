import sys
import json
import pathlib
import shutil

LICENSE_FILE = 'LICENSE.md'
OUT_FOLDER = 'new_visor'
IDLE_FILE = 'idle.png'
INFO_FILE = 'info.json'

def main(target_path : str, comit_hash : str = '')-> None:

  convart_target_dir = pathlib.Path(target_path)

  out_path = pathlib.Path(__file__).parent.joinpath(OUT_FOLDER)

  for old_visor_path in convart_target_dir.iterdir():

    if not old_visor_path.is_dir():
      continue

    author = old_visor_path.name

    visor_data = []
    license_path = None

    for old_visor_data in old_visor_path.iterdir():

      file = old_visor_data.name
      if file == LICENSE_FILE:
        license_path = old_visor_data
        continue

      visor_data.append((file[:-4], old_visor_data))

    if license_path is None:
      print('ERROR:LICENSE missing')
      continue

    for visor_name, source_path in visor_data:

      print(f'Convert visor:{visor_name}')

      visor_out_path = out_path.joinpath(visor_name)

      if visor_out_path.exists():
        shutil.rmtree(visor_out_path)

      visor_out_path.mkdir(parents=True)

      shutil.copy(source_path, visor_out_path.joinpath(IDLE_FILE))
      shutil.copy(license_path, visor_out_path.joinpath(LICENSE_FILE))

      with open(visor_out_path.joinpath(INFO_FILE), mode='w') as visor_json:
        json.dump(
          {
            'Author':author,
            'Name':visor_name,
            'LeftIdle':False,
            'Shader':False,
            'BehindHat':False,
            'ComitHash':comit_hash
          },
          visor_json, indent=2, ensure_ascii=False)

if __name__ == "__main__":

  arg = sys.argv

  comit_hash = ''
  if (len(arg) == 3):
    comit_hash = arg[2]
  main(arg[1], comit_hash)