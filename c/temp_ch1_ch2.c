#include <stdio.h>
#include <string.h>


int strlen_v1(char s[]) {
    int i;

    i = 0;
    while (s[i] != '\0')
        ++i;
    return i;
}


int atoi(char s[]) {
    int i, n;

    n = 0;
    for (i = 0; s[i] >= '0' && s[i] <= '9'; ++i)
        n = 10 * n + (s[i] - '0');
    return n;
}


int lower(int c) {
    /*
    if (c >= 'A' && c <= 'Z')
        return c + 'a' - 'A';
    else
        return c;
    */

    return (c >= 'A' && c <= 'Z') ? c + 'a' - 'A': c;
}


int isdigit_v1(int c) {
    int d;

    d = (c >= '0' && c <= '9');
    return d;
}


unsigned long int next = 1;


int rand(void) {
    next = next * 1103515245 + 12345;
    return (unsigned int)(next/65536) % 32768;
}


void srand(unsigned int seed) {
    next = seed;
}


void squeeze(char s[], int c) {
    int i, j;
    
    for (i = j = 0; s[i] != '\0'; i++) {
        if (s[i] != c) {
            s[j++] = s[i];
        }
    }
    s[j] = '\0';
}


void strcat_v1(char s[], char t[]) {
    int i, j;
    
    i = j = 0;
    while (s[i] != '\0')
        i++;
    while ((s[i++] = t[j++]) != '\0')
        ;
}


unsigned getbits(unsigned x, int p, int n) {
    return (x >> (p+1-n)) & ~(~0 << n);
}


int bitcount(unsigned x) {
    int b;
    
    for (b = 0; x != 0; x >>= 1) {
        if (x & 01)
            b++;
    }
    return b;
}


int main(int argc, char *argv[]) {
    char s[] = "12345";
    
    printf("%d\n", strlen_v1(s));
    printf("%d\n", strlen(s));
    printf("%d\n", atoi(s));
    
    char c = 'M';
    printf("%c\n", lower(c));

    char i = 'A';
    printf("%d\n", isdigit_v1(i));

    int seed = 806;
    srand(seed);
    printf("%d\n", rand());

    return 0;
}
