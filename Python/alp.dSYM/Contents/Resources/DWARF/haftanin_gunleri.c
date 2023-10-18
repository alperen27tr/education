//kullanicinin secimine gore haftanin gununu soyleyen program
#include <stdio.h>

int
main ()
{
  printf ("bir secim yapiniz (1-7):");
  int secim;
  scanf ("%d", &secim);
  switch (secim)
    {
    case 1:
      printf ("pazartesi");
      break;
    case 2:
      printf ("sali");
      break;
    case 3:
      printf ("carsamba");
      break;
    case 4:
      printf ("persembe");
      break;
    case 5:
      printf ("cuma");
      break;
    case 6:
      printf ("cumartesi");
      break;
    case 7:
      printf ("pazar");
      break;
    default:
      printf("yanlis secim");
      break;
    }

  return 0;
}
