#include <stdio.h>


void squeeze(char s[], int c);


int main(int argc, char argv)
{
    char s[] = "zhaojinghui";
    squeeze(s, 'i');
    printf("%s\n", s);
    return 0;
}


void squeeze(char s[], int c)
{
    int i, j;
    
    for (i = j = 0; s[i] != '\0'; i++)
        if (s[i] != c)
            s[j++] = s[i];
    s[j] = '\0';
}
