#include <stdio.h>


int strlen_v1(char s[]);


int main(int argc, char *argv[])
{
    char *s = "aaaaaaab";
    printf("len = %d\n", strlen_v1(s));
    return 0;
}


int strlen_v1(char s[])
{
    int i = 0;
    while (s[i] != '\0')
        ++i;
    return i;
}

