#include <iostream>
#include <string.h>

using namespace std;

#define N 5 //duljina polja

//okretanje redoslijeda članova polja
void okr(int f[N]){
    int f2[N];

    for (int i=0; i<5; i++)
        f2[i]=f[N-i-1];
    
    for (int i=0; i<5; i++)
        f[i]=f2[i];
}

//zamjena i-tog i j-tog člana
void zam(int i, int j, int f[N]){
    i -=1; j-=1;
    int a = f[i];
    f[i] = f[j];
    f[j] = a;
}

//sortiranje po veličini
void sort(int f[N]){
    int a;
    for (int i=0; i<N; i++)
        for (int j=0; j<i; j++){
            if(f[j]>f[j+1]){
                a = f[j];
                f[j] = f[j+1];
                f[j+1] = a;
            }
        }
}

int main(){
    int a=2,b=15,polje[N]={15,7,5,9,87}; //granice intervala a,b i polje

    okr(polje); //okretanje redoslijeda

    zam(1,2, polje); //zamjena 1. i 2. člana

    sort(polje); //sortiranje po veličini

    cout << "U intervalu [" << a << "," << b << "] nalaze se: ";

    for (int i=0;i<5;i++)
        if (polje[i]>=a && polje[i]<=b)
            cout << polje[i] << "  ";
}