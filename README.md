
# RetroZ-BIOS

Version 0.7.0 - 2020-06-24

A BIOS for the RetroZ Z80 computer project. This is a work in progress and
improves based on my other projects requirements. If you need some other
features feel free to ask in an issue or even better, fork and send a pull
request!

## Installation

Download the latest release from the [release section](https://github.com/formix/RetroZ-bios/releases).
If you are using SIO2 with serial line A control set to port 0, data 1 and
line B control to 2 and data to 3 then you are ready to go. Otherwise, you
will have to change those values in bios.z80 and recompile using [Megatokio's zasm](https://github.com/Megatokio/zasm).

Burn your ROM using minipro or any other EEPROM programmer. Make sure your ROM
chip is large enough to hold the program (8k should be enough).

## Usage

### Create a Project

1. Create a folder on your computer and copy the files `template-program.z80` and
`retroz-bios-inc.z80`.
2. Rename the `template-program.z80` file to match your project name or any other name you like.
3. Do your Code ;)
4. Assemble your program to a bin file.

### Upload to your Z80 computer

Connect to your Z80 computer using a VT100 compatible terminal. You should see
a small RetroZ bios header and a "Waiting for program..." prompt. Pressing any
key will not do anything since the terminal is waiting for a sequence of bytes
indicating a program is coming in to start.

To send your program, no fancy protocol is needed. Just upload the raw bin file
using your terminal program or in a separate console window by doing
`cat myprogram.bin > /dev/ttyUSB0` on Linux or `type myprogram.bin > COM1` in
a Windows/Dos prompt. Use your computer correct COM port or tty device
according to your environment. These values are provided as examples.

Note that if you plan to use the terminal option, make sure your computer
implements RTS/CTS hardware handshake or find a way to slow down the byte flow.

## RetroZ-BIOS Library Reference
