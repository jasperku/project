#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Product.h"

Product getAProductInfo()
{
  Product p;
  char c;
  char sizeStr[3];
  printf("ID=?");
  scanf(" %d", &p.ID);
  printf("price=?");
  scanf(" %f", &p.price);
  getchar();
  printf("type (b for book, k for keychain, t for t_shirt)=?");
  c=getchar();
  getchar();
  switch(c)
  {
    case 'b':
      p.type=book;
      printf("Author?");
      fgets(p.attribute.author,20, stdin);
      p.attribute.author[strlen(p.attribute.author)-1]='\0';
      break;
    case 'k':
      p.type=keychain;
      printf("Material (c for copper, s for steel, w for wood, p for plastic )?");
      c=getchar();
      getchar();
      switch(c)
      {
        case 'c':
          p.attribute.material=copper;
          break;
        case 's':
          p.attribute.material=steel;
          break;
        case 'w':
          p.attribute.material=wood;
          break;
        case 'p':
          p.attribute.material=plastic;
          break;        
      }
      break;
    case 't':
      p.type=t_shirt;
      printf("Size (XS, S, M, L, XL, XXL)?");
      scanf(" %s", sizeStr);
      if(strcmp(sizeStr,"XS")==0)
        p.attribute.size=XS;
      else if(strcmp(sizeStr,"S")==0)
        p.attribute.size=S;
      else if(strcmp(sizeStr,"M")==0)
        p.attribute.size=M;
      else if(strcmp(sizeStr,"L")==0)
        p.attribute.size=L;
      else if(strcmp(sizeStr,"XL")==0)
        p.attribute.size=XL;
      else if(strcmp(sizeStr,"XXL")==0)
        p.attribute.size=XXL;
      getchar();
      break;
  }
  return p;
}

void showAProductInfo(Product p)
{
  printf("ID:%d", p.ID);
  printf(" price=%.2f", p.price);
  switch(p.type)
  {
    case book:
      printf(" Book( ");
      printf("%s )", p.attribute.author);
      break;
    case keychain:
      printf(" Keychain( ");
      switch(p.attribute.material)
      {
        case copper:
          printf("copper )");
          break;
        case steel:
          printf("steel )");
          break;
        case wood:
          printf("wood )");
          break;
        case plastic:
          printf("plastic )");
          break;
      }
      break;
    case t_shirt:
      printf(" T Shirt( ");
      switch(p.attribute.size)
      {
        case XS:
          printf("XS )");
          break;
        case S:
          printf("S )");
          break;
        case M:
          printf("M )");
          break;
        case L:
          printf("L )");
          break;
        case XL:
          printf("XL )");
          break;
        case XXL:
          printf("XXL )");
          break;
      }
      break;
  }
  printf("\n");
}

void showAllProductInfo(Product products[], int count)
{
  int i;
  for(i=0;i<count;i++)
    showAProductInfo(products[i]);
}

void searchProduct(Product products[], int count, int id)
{
  int i;
  int found=0;
  
  for(i=0;i<count;i++)
  {
    if(products[i].ID==id)
    {
      showAProductInfo(products[i]);
      found=1;
      break;
    }
  }
  if(!found)
    printf("Product not found!\n");
}

void showHelp()
{
  printf("i: insert a new product.\n");
  printf("l: list all products.\n");
  printf("s: search for a product.\n");
  printf("q: quit.\n");
}

int main()
{
  Product products[10];
  int i=0;
  int id;
  int quit =0;
  char cmd;
  
  while(!quit)
  {
    printf("command?");
    cmd=getchar();
    switch(cmd)
    {
      case 'h':
        showHelp();
        getchar();
        break;
      case 'i':
        products[i++]=getAProductInfo();
        break;
      case 'l':
        showAllProductInfo(products, i);
        getchar();
        break;
      case 's':
        printf("ID?");
        scanf(" %d", &id);
        searchProduct(products, i, id);
        getchar();
        break;
      case 'q':
        quit=1;
        break;
      case 10:
        printf("Wrong command!\n");
        break;
      default:
        printf("Wrong command!\n");
        getchar();
        break;
    }
  }
}