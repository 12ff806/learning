#include <stdio.h>
#include <string.h>


int trim(char s[]);


int main(int argc, char *argv[])
{
    char s[] = " aaaaaa bbbb      ";
    int n = trim(s);
    printf("%s\n", s);
    printf("%d\n", n);
    return 0;
}


int trim(char s[])
{
    int n;

    for (n = strlen(s) - 1; n >= 0; n--)
        if (s[n] != ' ' && s[n] != '\t' && s[n] != '\n')
            break;
    s[n+1] = '\0';
    return n;
}
