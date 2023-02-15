#include <stdio.h>


int strlen_v1(char s[]);
int strlen_v2(char s[]);


int main(int argc, char *argv[])
{
    char *s = "aaaaaab";
    printf("len = %d\n", strlen_v1(s));
    printf("len = %d\n", strlen_v2(s));
    printf("len = %d\n", strlen_v2("hello, world"));
    return 0;
}


int strlen_v2(char *s)
{
    int n;
    
    for (n = 0; *s != '\0'; s++) {
        n++;
    }
    return n;
}


int strlen_v1(char s[])
{
    int i = 0;
    while (s[i] != '\0')
        ++i;
    return i;
}

