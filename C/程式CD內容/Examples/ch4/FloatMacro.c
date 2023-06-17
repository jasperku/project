#include <stdio.h>
#include <float.h>

int main()
{
  printf("FLT_RADIX = %d\n", FLT_RADIX);

  printf("\nFLT_MANT_DIG = %d\n", FLT_MANT_DIG);
  printf("DBL_MANT_DIG = %d\n", DBL_MANT_DIG);
  printf("LDBL_MANT_DIG = %d\n", LDBL_MANT_DIG);

  printf("\nFLT_DIG = %d\n", FLT_DIG);
  printf("DBL_DIG = %d\n", DBL_DIG);
  printf("LDBL_DIG = %d\n", LDBL_DIG);

  printf("\nFLT_MIN_EXP = %d\n", FLT_MIN_EXP);
  printf("DBL_MIN_EXP = %d\n", DBL_MIN_EXP);
  printf("LDBL_MIN_EXP = %d\n", LDBL_MIN_EXP);

  printf("\nFLT_MAX_EXP = %d\n", FLT_MAX_EXP);
  printf("DBL_MAX_EXP = %d\n", DBL_MAX_EXP);
  printf("LDBL_MAX_EXP = %d\n", LDBL_MAX_EXP);

  printf("\nFLT_MIN_10_EXP = %d\n", FLT_MIN_10_EXP);
  printf("DBL_MIN_10_EXP = %d\n", DBL_MIN_10_EXP);
  printf("LDBL_MIN_10_EXP = %d\n", LDBL_MIN_10_EXP);

  printf("\nFLT_MAX_10_EXP = %d\n", FLT_MAX_10_EXP);
  printf("DBL_MAX_10_EXP = %d\n", DBL_MAX_10_EXP);
  printf("LDBL_MAX_10_EXP = %d\n", LDBL_MAX_10_EXP);

  printf("\nFLT_MIN = %e\n", FLT_MIN);
  printf("DBL_MIN = %e\n", DBL_MIN);
  printf("LDBL_MIN = %Le\n", LDBL_MIN);

  printf("\nFLT_MAX = %e\n", FLT_MAX);
  printf("DBL_MAX = %e\n", DBL_MAX);
  printf("LDBL_MAX = %Le\n", LDBL_MAX);

  printf("\nFLT_EPSILON = %e\n", FLT_EPSILON);
  printf("DBL_EPSILON = %e\n", DBL_EPSILON);
  printf("LDBL_EPSILON = %Le\n", LDBL_EPSILON);

  printf("\nFLT_ROUNDS = %d\n", FLT_ROUNDS);

}
