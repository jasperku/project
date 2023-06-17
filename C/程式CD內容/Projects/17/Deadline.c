#include <stdio.h>
#include <string.h>

typedef enum { Sunday=0, 
               Monday=1,
               Tuesday=2,
               Wednesday=3,
               Thursday=4,
               Friday=5,
               Saturday=6,
               Undef=-1 } Weekday;

char weekdayString[][10] ={"Sunday", "Monday", "Tuesday", "Wednesday",
                           "Thursday", "Friday", "Saturday" };

Weekday getWeekday(char day[])
{
  Weekday i=Sunday;

  for(i=Sunday;i<=Saturday;i++)
  {
    if(strcmp(day, weekdayString[i])==0)
      return i;
  }
  return Undef;
}

int main()
{
  Weekday startDay, endDay;
  char today[10];
  int days;

  printf("What day (of the week) is it today? ");
  scanf(" %s", today);

  if((startDay = getWeekday(today))!=Undef)
  {
    printf("How many days after today? ");
    scanf(" %d", &days);
    endDay = (startDay+days)%7;
    printf("%d days later is %s.\n", days, weekdayString[endDay]);
    if(endDay==Sunday) // how about if(endDay==0)?
      printf("Because the end day is Sunday, it is extended to Monday!\n");
  }
  else
    printf("unknown weekday");
}