#include <stdio.h>
#include <conio.h>
main()
{
int sayfa=10,int okunansayfa=0,gun=0;
while(okunansayfa<1000,) {
    okunansayfa=+sayfa;
    sayfa+=5;
    gun++;
}
printf("%d. gun icinde kitap bitmiş olur" , gun);
getche();

}