//girilen sayiya kadar olan asal sayilari listeleme
#include <stdio.h>
#include <math.h>
int asalmi(int x){
    int sonuc=1;
    int ustlimit = (int) sqrt( (float)x); //sayinin karekokune kadar denemek yeterli
    if(x==2){ //2 asaldir
        return sonuc;
    }
    if(x%2==0){ //cift sayilar asal degildir. hemen eleyelim
        sonuc=0;
        return sonuc;
    }
    for(int i=3;i<ustlimit;i=i+2){ //3 den baslayip 2ser artarak deniyorz
        if(x%i == 0){
            sonuc=0;
        }
    }
    return sonuc;
}

void main(){
    int n;
    printf("ust limiti giriniz:"); scanf("%d",&n);
    for(int i=2;i<=n;i++){
        if(asalmi(i)==1){
            printf("%d\n",i);
        }
    }
    
}