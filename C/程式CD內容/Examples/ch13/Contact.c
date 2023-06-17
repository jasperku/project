#include <stdio.h>

typedef struct { char firstname[20], lastname[20]; } Name;

typedef struct
{
  Name name;
  int phone;
} Contact;

void showName(Name n)
{
  printf("%s, %s", n.lastname, n.firstname);
}

void showContact(Contact c)
{
  showName(c.name);
  printf(" %d\n", c.phone);
}

int main()
{
  Contact someone={.phone=12345, 
                  .name={.firstname="Jun", .lastname="Wu"}};

  showContact(someone);
}
