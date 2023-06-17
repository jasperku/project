all:	Main.c StringBox.o
	cc Main.c StringBox.o

StringBox.o: StringBox.c StringBox.h
	cc StringBox.c -c
	
clean: 
	rm *~ *.c~ *.h~ *.o a.out
	