nasm bootloader.asm -f bin -o bootloader.bin

nasm extprogram.asm -f elf64 -o extprogram.o

nasm binaries.asm -f elf64 -o binaries.o

wsl $WSLENV/x86_64-elf-gcc -Ttext 0x8000 -ffreestanding -mno-red-zone -m64 -c "kernel.cpp" -o "kernel.o"

wsl $WSLENV/x86_64-elf-ld -T "link.ld"

copy /b bootloader.bin+kernel.bin bootloader.flp
pause