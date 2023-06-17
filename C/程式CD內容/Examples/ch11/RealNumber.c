#include <stdio.h>

void decompose(double val, long *int_part, double *frac_part)
{
  *int_part = (long) val;
  *frac_part = val - ((long)val);
}

int main()
{
  long int iPart;
  double fPart;
  double pi=3.1415926;
  decompose(pi, &iPart, &fPart);
  printf("The value %.7f can be divided into two parts:\n", pi);
  printf("the integer part %ld and the fractional part %.7f.\n", iPart, fPart);
}
      