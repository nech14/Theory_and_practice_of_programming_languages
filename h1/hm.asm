
section .text
global main

extern printf



%macro pushd 0
    push rax
    push rbx
    push rcx
    push rdx
%endmacro

%macro popd 0
    pop rdx
    pop rcx
    pop rbx
    pop rax
%endmacro


%macro getLenMas 3
    pushd
    
    mov eax, %1 ; len mas
    mov ebx, %2 ; count bytes

    mov edx, 0
    
    div ebx

    mov %3, eax ; cout buf 

    popd
    
%endmacro


%macro addMas 3
    pushd

    mov ebx, 4  ; count bytes
    mov edx, 0
    mov eax, %1

    getLenMas %1, ebx, esi
    
    mov ecx, esi
    lea ebx, %2
    mov esi, 0
    repeat:
        add %3, [ebx]
        add ebx, 4
        loop repeat

    popd
%endmacro


%macro subMass 5
    pushd

    mov ebx, 0
    mov edx, 0

    lea ebx, %1
    lea edx, %2

    mov ecx, %4
    
    mov eax, 0

    mov esi, 0
    lea esi, buf


    subMassR:
        mov eax, [ebx]
        sub eax, [edx]
        add ebx, %5
        add edx, %5
        ;mov %3, eax
        mov [esi], eax
        add esi, %5

        loop subMassR
    
    mov %3, esi
    popd
%endmacro


%macro abs 1
    pushd

    mov ebx, %1
    changeSign:
        neg ebx
        js changeSign

    mov %1, ebx

    popd
%endmacro


%macro negForIdiv 2
    pushd

    mov ebx, %1
    mov ecx, %2
    changeSigns:        
        neg ecx
        neg ebx
        js changeSigns

    
    mov %1, ebx
    mov %2, ecx

    popd
%endmacro



main:
    push rbp




    mov esi, 0
    ;addMas lenMas, mas, esi  
    mov edx, 0 
    getLenMas lenx, 4, esi
    ;mov esi, edx
    ;call printf

    ;sub esi, 4

    subMass x, y, esi, esi, 4

    addMas lenx, buf, esi
    getLenMas lenx, 4, edi

    mov edx, 0    
    negForIdiv esi, edi
    mov eax, esi

    mov ecx, edi    
    mov ebx, ecx

    
    idiv ebx
    mov esi, eax

    mov rdi, format1
    cmp edx, 0 
    
    je end
    


    
f:
    mov rdi, format
    
    

end:    
    call printf
    pop rbp
    mov       rax, 60
    
    xor       rdi, rdi

    syscall


section .data
    format1 db "answer = %d", 0xA, 0xD
    n1 dd 10
    n2 dd 3
    mas dd 1, 10, 100, 1000, 10000
    
    lenMas equ $ - mas
    
    x dd 5, 3, 2, 6, 1, 7, 4
    lenx equ $ - x

    y dd 0, 10, 1, 9, 2, 8, 5


    buf dd 10 dup (1)


    format db "answer = %d + %d/%d", 0xA, 0xD
    