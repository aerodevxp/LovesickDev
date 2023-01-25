printstr:
	push ax
	push bx

	mov ah, 0x0e ; Moving to upper part of A register
	.Loop:
		cmp [bx], byte 0													; conditional statement - if [bx] is now 0 aka end of str
		je .Exit															; if true
			mov al, [bx] ;													; else
			int 0x10 ; Interrupting to print.
			inc bx
			jmp .Loop
	.Exit:
		mov al, 10
		int 0x10
		mov al, 13
		int 0x10
		pop ax
		pop bx
		ret ; *return*
