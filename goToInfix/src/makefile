
SOURCES = Main.hx
INPUT = input

ifeq ($(OS), Windows_NT)
	RM = del
	TARGET = Main.exe
else
	RM = rm
	TARGET = Main
endif


allpy:
	haxe -main $(SOURCES) -python $(INPUT).py
runpy: allpy
	python $(INPUT).py

cleanpy:
	$(RM) $(INPUT).py

all:
	haxe -main $(SOURCES) -neko $(INPUT).n

run: all
	neko $(INPUT).n

clean:
	$(RM) $(INPUT).n

htest:
	haxelib run munit test -coverage -result-exit-code

i:
	haxelib install munit
	haxelib install mcover
	haxelib install hamcrest

fix:
	haxelib remove munit
	haxelib remove mcover
	haxelib git munit https://github.com/massiveinteractive/MassiveUnit.git master src
	haxelib git mcover https://github.com/nech14/mcover.git
	



	





