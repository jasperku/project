all:	Main.c Poker.o BlackJack.o
	cc Main.c Poker.o BlackJack.o

Poker.o: Poker.c Poker.h
	cc Poker.c -c
	
BlackJack.o: BlackJack.c BlackJack.h
	cc BlackJack.c -c
	
clean: 
	rm *.c~ *.h~ *.o a.out
	
	