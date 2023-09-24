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

%macro x1 3
    pushd

    mov eax, %1
    mov ebx, 2
    cdq
    div ebx

    mov %2, eax
    mov %3, edx

    popd
%endmacro

%macro x2 3
    pushd

    mov ebx, %1
    mov eax, %2
    cdq
    div ebx
    add ebx, eax
    
    
    mov ecx, 2
    cdq

    mov eax, ebx
    div ecx

    mov %3, eax    

    popd
%endmacro


main:
    

    x1 [num], esi, edi
    x2 esi, [num], [buf]

    mov ecx, esi
    sub ecx, [buf]
    cmp ecx, 1
    jnge end

    repeat:
        mov esi, [buf]        
        x2 esi, [num], [buf]
        sub esi, [buf]
        cmp esi, 1
        jge repeat

    end:

    push rbp

    mov edi, format
    mov esi, [buf]
    call printf

    pop rbp

    mov       rax, 60
    xor       rdi, rdi
    syscall



section .data
    num dd 144
    buf dd 0
    format db "answer: %d", 0xA, 0xD