//sayı tahmin oyunu
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(){
    int bs;
    srand(time(NULL));
    bs=rand() % 100;
    //printf("bs=%d\n",bs);
    int tahmin;
    for(int i=1;i<100;i++) {
        scanf("%d",&tahmin);
        if(tahmin<bs){
            printf("arttir\n");
        } else if (tahmin>bs){
            printf("azalt\n");
        } else {
            printf("tebrikler %d adimda buldunuz",i);
            break;
        }
    }
}