#include <stdio.h>


int atoi(char s[]);


int main(int argc, char *argv[])
{
    char s[] = "158";
    printf("atoi: %s -> %d\n", s, atoi(s));
    return 0;
}


int atoi(char s[])
{
    int i, n;
    
    n = 0;
    for (i = 0; s[i] >= '0' && s[i] <= '9'; ++i)
        n = 10 * n + (s[i] - '0');
    return n;
}
