#!/bin/bash

set -e      # Exit on error

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo -e "Building bios.z80:\n"
mkdir -p out
zasm -uyw bios.z80 -o out/bios.rom
echo bios.rom... done!
cp retroz-bios-inc.header out/retroz-bios-inc.z80
echo -e "\n; +++ global symbols +++\n" >> out/retroz-bios-inc.z80
./export.py < out/bios.lst | sort >> out/retroz-bios-inc.z80
echo -e "bios-inc.z80... done!"
echo All done! Output files are in ./out enjoy!
echo To call bios subroutines, include out/retroz-bios-inc.z80 in your source files.
