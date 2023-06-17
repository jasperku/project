#include <stdio.h>
#define N 10

void showData(int num[])
{
   int i;
   for(i=0; i<N;i++)
      printf("%d ", num[i]);
   printf("\n");
}

void sortData(int num[])
{
   int i, j, temp;
   for(i=0;i<N-1;i++)
      for(j=0;j<N-i-1;j++)
         if(num[j]<num[j+1])
         {
            temp=num[j];
            num[j]=num[j+1];
            num[j+1]=temp;
         }
}

int main()
{
   int data[N]={21, 5, 34, 67, 26, 24, 9, 18, 32, 190};
   showData(data);
   sortData(data);
   showData(data);
   int i=5;
   for(int j=0;j<i;j++)
   {
      int temp;
      temp=i;
      
   }
}
