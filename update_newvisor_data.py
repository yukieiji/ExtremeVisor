import os
import json
from pylightxl import readxl

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

VISOR_IN_FILE = os.path.join(WORKING_DIR, 'VisorTransData.xlsx')
VISOR_FOLDER = os.path.join(WORKING_DIR, 'new_visor')
VISOR_OUT_FILE = os.path.join(WORKING_DIR, 'new_visor', 'visorTransData.json')
VISOR_DATA_FILE = os.path.join(WORKING_DIR, 'new_visor', 'visorData.json')

VISOR_LICENSE = 'LICENSE.md'
VISOR_DATA_DATA_KEY = 'data'
VISOR_DATA_UPDATE_COMIT_KEY = 'updateComitHash'

def stringToJson(filename : str, outputFile : str) -> None:

  wb = readxl(filename)

  xlsx_data = {}

  for name in wb.ws_names:

    sheat = wb.ws(name)

    row, col = sheat.size

    # 行を回す
    for i in range(2, row + 1):

      data = {}

      # i行目の1列目はキー
      key = sheat.index(i, 1)
      if key == "":
        continue

      # i行目j列がデータ、jは2以上であり2が0(英語)である
      for j in range(2, col + 1):
          cell_data = sheat.index(i, j)

          if type(cell_data) != str or cell_data == "":
            continue

          # I hate excel why did I do this to myself
          data[str(j - 2)] = cell_data.replace("\r", "").replace("_x000D_", "").replace("\\n", "\n")

      if data != {}:
        xlsx_data[key] = data

  with open(outputFile, "w") as f:
    json.dump(xlsx_data, f, indent=4)

def update_visor_data()-> None:

  visor_dir = os.listdir(VISOR_FOLDER)

  visor_dir.remove('visorTransData.json')
  visor_dir.remove('visorData.json')

  visor_dir.sort()

  with open(os.path.join(VISOR_DATA_FILE), mode='w') as visor_json:
    json.dump(
      {VISOR_DATA_DATA_KEY:visor_dir, VISOR_DATA_UPDATE_COMIT_KEY:""},
      visor_json, indent=2, ensure_ascii=False)

def main()-> None:
  update_visor_data()
  stringToJson(VISOR_IN_FILE, VISOR_OUT_FILE)

if __name__ == "__main__":
  main()