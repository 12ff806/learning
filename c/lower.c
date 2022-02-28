#include <stdio.h>


int lower(int c);


int main(int argc, char *argv[])
{
    int a = 'A';
    printf("%d\n", lower(a));
    putchar(lower(a));
    return 0;
}


int lower(int c)
{
    if (c >= 'A' && c <= 'Z')
        return c + 'a' - 'A';
    else
        return c;
}
