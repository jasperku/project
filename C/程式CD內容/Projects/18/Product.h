typedef enum {book, keychain, t_shirt} Type;
typedef enum {copper, steel, wood, plastic } Material;
typedef enum {XS, S, M, L, XL, XXL} Size;

typedef struct 
{
  int ID;
  float price;
  Type type;
  union
  {
      char author[20];
      Material material;
      Size size;
  } attribute;
} Product;
                        
