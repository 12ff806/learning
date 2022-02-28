#include <stdio.h>


int main(int argc, char *argv[])
{
    enum boolean {NO, YES};
    enum escapes {BELL = '\a', BACKSPACE = '\b', TAB = '\t', 
                  NEWLINE = '\n', VTAB = '\v', RETURN = '\r'};
    enum months {JAN = 1, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC};
    

    printf("no = %d, yes = %d\n", NO, YES);
    printf("%d\n", DEC);
    printf("%d\n", TAB);
    return 0;
}

