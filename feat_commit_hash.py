import sys

import os
import json
from pathlib import Path
from typing import List

VISOR_DIR = os.path.join(
  os.path.dirname(os.path.realpath(__file__)), 'new_visor')
VISOR_INFO_UPDATE_COMIT_KEY = 'ComitHash'
VISOR_INFO_NAME = 'info.json'

def get_visor_dir_name(change_files : List[str]) -> List[str]:

  visor_dir = []

  for path in change_files:

    check_path = Path(path).resolve()
    parent = check_path.parent
    if not parent.is_dir():
      continue
    visor_name = parent.parts[-1]
    if not (visor_name in visor_dir):
      visor_dir.append(visor_name)

  return visor_dir

def feat_comit_hash(comit_hash: str, visor_name: List[str]):

  for visor in visor_name:
    info_path = os.path.join(VISOR_DIR, visor, VISOR_INFO_NAME)
    if os.path.exists(info_path):
      with open(os.path.join(info_path), mode='r') as info:
        visor_info = json.load(info)

      visor_info[VISOR_INFO_UPDATE_COMIT_KEY] = comit_hash
      with open(os.path.join(info_path), mode='w') as visor_json:
        json.dump(
          visor_info,
          visor_json, indent=2, ensure_ascii=False)

def main(commit_hash: str, change_files: List[str]) -> None:
  feat_comit_hash(
    commit_hash,
    get_visor_dir_name(change_files))


if __name__ == "__main__":
  commit_hash = sys.argv[1]
  change_files = sys.argv[2:]
  print(f"commit_hash: {commit_hash}")
  print(f"change_files : {change_files}")
  main(commit_hash, change_files)