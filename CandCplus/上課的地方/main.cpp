#include <iostream>
using namespace std;
 
class Book
{
    public:
        double price;
        
        void setPrice(double p)
        {
            price=p;
        }
        
        double getPrice()
        {
            return price;
        }
};
double operator+(Book b1, Book b2)
{
  double b;
  return b1.price + b2.price;
}

int main()
{
    Book b1, b2;
    
    b1.setPrice(100.0);
    b2.setPrice(88.99);
    cout << "Total price is " << b1+b2 << "!" << endl;
}
