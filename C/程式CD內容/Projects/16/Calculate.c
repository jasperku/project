#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  
  if(argc!=4)
  {
    printf("usage: Calculate A op B\n");
  }
  else
  {
    int operand1, operand2;  
    operand1 = atoi(argv[1]);
    operand2 = atoi(argv[3]);
    
    double result=0.0;
    switch(argv[2][0])
    {
      case '+':
                result = operand1 + operand2;
                break;
      case '-':
                result = operand1 - operand2;
                break;
      case 'x':
                result = operand1 * operand2;
                break;
      case '/':
                result = operand1 / (double)operand2;
                break;
      default:
            printf("usage: Calculate A op B\n");
            break;
    }
    printf("%d%c%d=%.2f\n", operand1, argv[2][0], operand2, result);
  }
}