import sys, re
from typing import TextIO

def refactor_aff(aff: TextIO, old_flag: str, new_flag: str):
  lines = aff.readlines()
  for i, line in enumerate(lines):
    if line:
      e = line.split(" ")
      if re.match("^PFX$|^SFX$", e[0]) and e[1] == old_flag:
        e[1] = new_flag
        lines[i] = " ".join(e)
  aff.truncate(0)
  aff.seek(0)
  aff.writelines(lines)
  aff.close()

def refactor_dic(dic: TextIO, old_flag: str, new_flag: str):
  lines = dic.readlines()
  for i, line in enumerate(lines):
    if i != 0 and line:
      e = line.split(" ")
      if re.match(".*/.*" + old_flag + ".*", e[0]):
        entry = e[0].split("/")
        e[0] = "/".join((entry[0], entry[1].replace(old_flag, new_flag)))
        lines[i] = " ".join(e)
  dic.truncate(0)
  dic.seek(0)
  dic.writelines(lines)
  dic.close()

def usage():
  print("flag_refactorization.py aff_path dic_path old_flag new_flag")
  sys.exit(1)

def main():
  if len(sys.argv) != 5:
    usage()
  refactor_aff(open(sys.argv[1], "r+"), sys.argv[3], sys.argv[4])
  refactor_dic(open(sys.argv[2], "r+"), sys.argv[3], sys.argv[4])

if __name__ == "__main__":
  main()
