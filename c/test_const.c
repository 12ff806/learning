#include <stdio.h>


int main(int argc, char *argv[])
{
    const double e = 2.71828182845905;
    const char msg[] = "warning: ";
    //char msg[] = "warning: ";

    printf("%s\n", msg);
    msg[0] = 'a';
    printf("%s\n", msg);
    return 0;
}
