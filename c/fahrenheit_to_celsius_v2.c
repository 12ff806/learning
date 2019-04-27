#include <stdio.h>


/* 当fahr=0, 20, ..., 300 时, 分别打印华氏温度与摄氏温度对照表 */
int main()
{
    float fahr, celsius;
    float lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;
     
    printf("Fahr  Celsius\n");

    fahr = lower;
    while (fahr <= upper){
        celsius = (5.0 / 9.0) * (fahr - 32.0);
        printf("%3.0f  %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
