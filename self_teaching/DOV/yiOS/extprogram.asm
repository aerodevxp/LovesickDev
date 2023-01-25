[bits 16]
jmp enterprotectedmode

%include "gdt.asm"
%include "print.asm"
enterprotectedmode:
	call enableA20
	cli
	lgdt [gdt_descriptor]
	mov eax, cr0
	or eax, 1
	mov cr0, eax
	jmp codeseg:startprotectedmode

enableA20:
	in al, 0x92
	or al, 2
	out 0x92, al
	ret

[bits 32]
%include "CPUID.asm" ; compiled in 32-bits mode
%include "simplepaging.asm"


startprotectedmode:
	mov ax, dataseg
	mov ds, ax
	mov ss, ax
	mov es, ax
	mov fs, ax
	mov gs, ax

	mov [0xb8000], byte 'H'
	mov [0xb8002], byte 'e'
	mov [0xb8004], byte 'l'
	mov [0xb8006], byte 'l'
	mov [0xb8008], byte 'o'
	mov [0xb800a], byte ' '
	mov [0xb800c], byte 'W'
	mov [0xb800e], byte 'o'
	mov [0xb8010], byte 'r'
	mov [0xb8012], byte 'l'
	mov [0xb8014], byte 'd'
	

	call detectCPUid
	call detectlongmode
	call setupidentitypaging
	call editgdt
	jmp codeseg:start64bit

[bits 64]
[extern _start]

%include "idt.asm"

start64bit:
	;mov edi, 0xb8000 ; video memory text address and incrementing this after each repeat
	;mov rax, 0x5f205f205f205f20
	;mov ecx, 500 ; repeating last lines
	;rep stosq
	call _start
	jmp $

times 2048-($-$$) db 0