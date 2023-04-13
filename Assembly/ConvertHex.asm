.386
data    segment use16
block   db  100h dup(0)
data    ends

stack   segment stack use16
        db  100h dup('S')
stack   ends

code    segment use16
assume  cs:code, ds:data
begin:
        mov ax, data
        mov ds, ax
        mov di, 0
input_next:
        mov ah, 1
        int 21h
        cmp al, 0Dh
        je  input_done
        mov [di], al
        inc di
        jmp input_next
input_done:
        mov si, 0
        mov bx, 4
        call str_to_hex
        mov di, 4
        call word_to_str
        jmp exit

;--------------------------------
;convert the string in ds:[si] to hex number
;restore the hex number to ax
str_to_hex:
        ret

;--------------------------------
;convert the hex number in ax to 4 chars
;restore the 4 bytes to ds:[di]
word_to_str:
        call byte_to_str
        mov ah, al
        add di, 2
        call byte_to_str
        ret

;convert the hex number in ah to 2 chars
;restore the 2 bytes to ds:[di]
byte_to_str:
        ;restore the high 4 bit to bh
        mov bh, ah
        shr bh, 4
        call hex_to_char
        ;restore the low 4 bit to bh
        mov bh, ah
        shl bh, 4
        shr bh, 4
        inc di
        call hex_to_char
        dec di
        ret

;convert the hex number in bh to char
;restore the byte to ds:[di]
hex_to_char:
        cmp bh, 9h
        ja  is_alpha
        jmp is_num
is_alpha:
        add bh, 37h ;A=65, 10+55=65
        mov ds:[di], bh
        ret
is_num:
        add bh, 30h ;0=48, 0+48=48
        mov ds:[di], bh
        ret
;--------------------------------

exit:
        mov ah, 01h
        int 21h
        mov al, 00h
        mov ah, 4Ch
        int 21h
code    ends
        end  begin
