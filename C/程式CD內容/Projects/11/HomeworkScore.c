#include <stdio.h>

#define numStudents 50

int main()
{
  int i,j,k;
  int temp;
  int plagiarism[numStudents]= {0};
  int homework[numStudents][9];
  float sum[numStudents]={0.0};
  float average[numStudents][2];
  float temp0, temp1;
  
  for(i=0;i<numStudents; i++)
  {
    scanf("%2d %d:%d:%d:%d:%d:%d:%d:%d",
          &homework[i][0],
          &homework[i][1],
          &homework[i][2],
          &homework[i][3],
          &homework[i][4],
          &homework[i][5],
          &homework[i][6],
          &homework[i][7],
          &homework[i][8]); 
  }
  for(i=0; i<numStudents; i++)
  {
    for(j=1; j<8; j++)
    {
      for(k=1; k<8-i; k++)
      {
        if( homework[i][k]<homework[i][k+1])
        {
           temp=homework[i][k];
           homework[i][k]=homework[i][k+1];
           homework[i][k+1]=temp;
        } 
        if((plagiarism[i]!=1)&&((homework[i][j]==-2)||(homework[i][k]==-2)))
           plagiarism[i]=1;
      }
    }
  }
  
  for(i=0;i<numStudents; i++)
  {
    if(plagiarism[i]==1)
    {
      for(j=8; j>3; j--)
      {
        sum[i]+= (homework[i][j]>=0? homework[i][j] : 0);
      }
    }
    else
    {
      for(j=1;j<6;j++)
      {
        sum[i]+= (homework[i][j]>0? homework[i][j] : 0);
      }
    }
    average[i][0] = homework[i][0];
    average[i][1] = sum[i]/5;
  }
  
  for(i=0;i<numStudents-1;i++)
  {
    for(j=0;j<numStudents-i-1;j++)
    {
      if(average[j][1]<average[j+1][1])
      {
        temp0 = average[j][0];
        temp1 = average[j][1];
        average[j][0]=average[j+1][0];
        average[j][1]=average[j+1][1];
        average[j+1][0]=temp0;
        average[j+1][1]=temp1;
      }
    }
  }
  
  printf("Rank No. Score\n");
  for(i=0;i<numStudents;i++)
  {  
     printf("%2d   %2d  %6.2f\n",i+1, (int)average[i][0], average[i][1]);
  }
}