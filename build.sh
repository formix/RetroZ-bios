#!/bin/bash

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo -e "Building bios.z80:\n"
zasm -uyw bios.z80
mkdir -p out
mv bios.rom out
echo bios.rom... done!
mv bios.lst out
echo bios.lst... done!
./export.py < out/bios.lst | sort > out/bios-inc.z80
echo -e "bios-inc.z80... done!"
echo All done! Output files are in ./out enjoy!
echo To call bios functions, include out/bios-inc.z80 in your assemler files.
