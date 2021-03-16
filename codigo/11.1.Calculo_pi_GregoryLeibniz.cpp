/*
http://edupython.blogspot.com/2015/03/pensando-en-pi.html

serie de Gregory–Leibniz
 
π = 4(1 - 1/3 + 1/5 - 1/7 + ...)

*/
#include <iostream>
#include <chrono>
#include <math.h>
#include <stdio.h>


using namespace std;

float getPowerSign(int k){
    if (k%2 == 0) return 1.0;
    else return -1.0;
}

float getSerieGregoryLeibniz(long n){
    float suma = 0;
    for (long k=1;k<n;k++)
        suma += getPowerSign(k+1)/(2.0*k-1);
    
    
    float resultado = 4 * suma;
    return resultado;
}
int  main(){

using clock = chrono::system_clock;
using sec = chrono::duration<double>;



for(int n=1;n<=12;n++){
    const auto before = clock::now();
    float  valor = getSerieGregoryLeibniz(pow(10,n));
    const sec duration = clock::now() - before;
    //cout << duration.count() << " " << n<< " " << valor  << endl;
    char buffer[50];
    sprintf(buffer,"%%f %%d %%%d.%df\n",2+n,n);
    printf(buffer,duration.count() ,n ,valor);
    FILE *fp = fopen("tiempos_c.csv","at");
    fprintf(fp,buffer,duration.count() ,n ,valor);
    fclose(fp);

    }
}
