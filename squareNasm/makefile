CC = g++
CFLAGS = -std=c++11 -Wall -pedantic
SOURCES = sqrl.asm

OUT = a.out 
TARGET = sqrl.o


all:
	nasm -felf64 $(SOURCES) && gcc -no-pie -fno-pie $(TARGET) && ./$(OUT)


clean:	
	rm $(TARGET)
	rm $(OUT)

run: all

