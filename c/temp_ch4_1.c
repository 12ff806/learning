#include <stdio.h>
#include <ctype.h>

#define MAXLINE 100


double atof(char s[]) {
    double val, power;
    int i, sign;

    for (i = 0; isspace(s[i]); i++)
        ;
    sign = (s[i] == '-') ? -1 : 1;
    if (s[i] == '+' || s[i] == '-')
        i++;
    for (val = 0.0; isdigit(s[i]); i++)
        val = 10.0 * val + (s[i] - '0');
    if (s[i] == '.')
        i++;
    for (power = 1.0; isdigit(s[i]); i++) {
        val = 10.0 * val + (s[i] - '0');
        power *= 10.0;
    }
    return sign * val / power;
}


int atoi(char s[]) {
    double atof(char s[]);
    
    return (int) atof(s);
}


int getline_v1(char line[], int max) {
    int i, c;
    
    i = 0;
    while (--max > 0 && (c = getchar()) != EOF && c != '\n') {
        line[i++] = c;
    }
    if (c == '\n')
        line[i++] = c;
    line[i] = '\0';
    return i;
}


int main(int argc, char *argv[]) {
    char s[] = "    -123.4567   ";
    printf("%.4f\n", atof(s));
    
    double sum, atof(char []);
    char line[MAXLINE];
    int getline_v1(char line[], int max);

    sum = 0.0;
    while (getline_v1(line, MAXLINE) > 0)
        printf("\t%g\n", sum += atof(line));

    return 0;
}
