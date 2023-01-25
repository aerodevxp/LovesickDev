; Welcome to my very first bootloader ^^!
; Made by ComboDev - January 2022
; =============
[org 0x7c00]

mov [BOOT_DISK], dl ; Moving dl, variable of disk booted from.

mov bp, 0x7c00
mov sp, bp

mov bx, newstr
call printstr

call readdisk

jmp PROGRAM_SPACE

%include "print.asm"
%include "diskread.asm"

newstr:
	db 'Welcome!', 0

times 510-($-$$) db 0 ; Filling bytes left to fill - A boot loader HAS TO BE 512 bytes!
dw 0xaa55 ; At the end