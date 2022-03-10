#include <stdio.h>
#include <ctype.h>
#define SIZE 100


int main(int argc, char *argv[])
{
    int n, array[SIZE], getint(int *);

    for (n = 0; n < SIZE && getint(&array[n]) != EOF; n++)
        ;
    
}


int getch(void);
void ungetch(int);


