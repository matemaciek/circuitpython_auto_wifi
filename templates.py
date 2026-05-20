import os
import re
import storage

EXTENSION = "tmpl"

def apply(filename, vars):
    was_ro = storage.getmount("/").readonly
    if was_ro:
        storage.remount("/", False)
    rex = []
    for k,v in vars.items():
        rex.append((re.compile("{{" + k + "}}"), v))
        
    with open(f"{filename}.{EXTENSION}") as in_file, open(f"{filename}", "w") as out_file:
        for line in in_file.readlines():
            for r, v in rex:
                line = r.sub(v, line)
            out_file.write(line)

    if was_ro:
        storage.remount("/", True)

def all(dir="/"):
    return [filename[:-(len(EXTENSION)+1)] for filename in os.listdir(dir) if filename.endswith(f".{EXTENSION}")]

def apply_all(vars):
    for t in all():
        apply(t, vars)
