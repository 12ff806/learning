#include <stdio.h>


/* size_t 定义成 unsigned int */
size_t strlen(const char *s);


float sum_elements(float a[], unsigned length) {
    int i;
    float result = 0;

    for (i = 0; i < length; i ++) {
        printf("i = %d\n", i);
        result += a[i];
    }
    return result;
}


int strlonger(char *s, char *t) {
    //return strlen(s) - strlen(t) > 0;
    return strlen(s) > strlen(t);
}


int main()
{
    float a[] = {1.1, 2, 3, 4};
    float r = sum_elements(a, 0);
    printf("%f\n", r);

    char *s = "abs";
    char *t = "abcs";
    int i = strlonger(s, t);
    printf("i = %d\n", i);

    return 0;
}

