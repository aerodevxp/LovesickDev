
PROGRAM_SPACE equ 0x8000 

readdisk:
	mov bx, diskreadloadstr
	call printstr

	mov ah, 0x02 ; BIOS function to read disk
	mov bx, PROGRAM_SPACE
	mov al, 32
	mov dl, [BOOT_DISK]
	mov ch, 0x00
	mov dh, 0x00
	mov cl, 0x02 ; Sector 2

	int 0x13

	jc diskreadfailure
	
	ret

BOOT_DISK:
	db 0

diskreaderrorstr:
	db 'Disk Read Failure. yOS cannot continue launching.',0
diskreadloadstr:
	db 'Reading Disk...',0

diskreadfailure:
	mov bx, diskreaderrorstr
	call printstr
	jmp $