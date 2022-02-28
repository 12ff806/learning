#include <stdio.h>


int main(int argc, char *argv[])
{
    int a = 'A';
    while (a == 65) {
        printf("a = %d\n", a);
        printf("%d\n", a==65);
        break;
    }
    return 0;
}
