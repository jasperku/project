#include <stdio.h>
#include <string.h>

#define numContact 10

typedef enum {Male, Female} Gender;

typedef enum {January, February, March, April, May, June, July,
              August, September, October, November, December} Month;

typedef struct
{
  Month month;
  short day;
  short year;
} Date;

typedef struct
{
  char firstname[20];
  char lastname[10];
} Name;
typedef enum {CHT, TWN, FET} Carrier;

typedef struct
{
  char number[10];
  Carrier carrier;
} Mobile;

typedef struct
{
  char areacode[4];
  char number[8];
} Landline;

typedef enum {LandLine, MobilePhone} PhoneType;

typedef struct
{
  Name name;
  Gender gender;
  Date birthday;
  PhoneType phonetype;
  union
  {
    Landline landline;
    Mobile mobile;
  } phone;
  char address[50];
} Contact;

Contact getAContact();
void showAContact(Contact c);
void sortContacts(Contact cs[]);
