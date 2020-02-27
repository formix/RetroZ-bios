#!/usr/bin/python3

import os.path
import sys



SYMBOLS_DELIM = "; +++ global symbols +++"


def main():
    exf = sys.argv[1] if len(sys.argv) > 1 else "exported_labels.txt"
    exported_labels = load_exported_labels(exf)
    labels = get_label_addrs(sys.stdin, exported_labels, SYMBOLS_DELIM)
    for label in labels:
        name = label["name"]
        address = label["address"]
        print(name, end="")
        print(' ' * (32 - len(name)), end="")
        print("EQU     ", end="")
        print(address)


# Returns the set of labels from the exported_labels_path file.
def load_exported_labels(exported_labels_path):
    if not os.path.isfile(exported_labels_path):
        eprint(f"WARNING: The file '{exported_labels_path}' does not exist. ", end="")
        eprint("All labels from the symbol section will be generated.")
        return set()
    with open(exported_labels_path) as labels_file:
        return set([label.strip() for label in labels_file])


# Print at error stream.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# Returns a generator of label-address pairs from a .lst file. A label 
# definition is an object of {name, address} pairs. exported_labels is a set
# that contains a subset of labels to export. If the set is empty, return all
# label-address pairs after the delimiter marker in the lst_file. Expects the
# lst_file to be generated from zasm.
# Scans for the delimiter before producting label definitions.
def get_label_addrs(lst_file, exported_labels, delimiter):
    for line in lst_file: # Skips all lines before the symbols delimiter
        if line.startswith(delimiter):
            break
    for line in lst_file: # Start generating label definitions.
        if '=' in line:
            segments = line.split('=')
            label = { 
                "name" : segments[0].strip(), 
                "address" : segments[1].strip() 
            }
            if len(exported_labels) == 0 or label["name"] in exported_labels:
                yield label



if __name__ == "__main__":
    main()
