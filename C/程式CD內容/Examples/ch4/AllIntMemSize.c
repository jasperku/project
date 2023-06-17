#include<stdio.h>

int main()
{
	printf("Type\t\t\tMemory Size(bits)\n");
	printf("short int\t\t%lu \n",  sizeof(short)*8);
	printf("int\t\t\t%lu \n", sizeof(int)*8);
	printf("long int\t\t%lu \n",  sizeof(long int)*8);
	printf("unsigned short int\t%lu \n", sizeof(unsigned short int)*8);
	printf("unsigned int\t\t%lu \n",  sizeof(unsigned int)*8);
	printf("unsigned long int\t%lu \n", sizeof(unsigned long int)*8);
}
