CC = g++
CFLAGS = -std=c++11 -Wall -pedantic
SOURCES = hm.asm

OUT = a.out 
TARGET = hm.o


all:
	nasm -felf64 $(SOURCES) && gcc -no-pie -fno-pie $(TARGET) && ./$(OUT)


clean:	
	rm $(TARGET)
	rm $(OUT)

run: all

