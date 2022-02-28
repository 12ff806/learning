#include <stdio.h>


void strcat_v1(char s[], char t[]);


int main(int argc, char *argv[])
{
    char s[] = "zhao";
    char t[] = "jinghui";

    strcat_v1(s, t);
    printf("%s\n", s);
    return 0;
}


void strcat_v1(char s[], char t[])
{
    int i, j;
    
    i = j = 0;
    while (s[i] != '\0')
        i++;
    while ((s[i++] = t[j++]) != '\0')
        ;
}
