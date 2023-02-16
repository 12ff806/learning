#include <stdio.h>
#include <ctype.h>
#include <string.h>


int binsearch(int x, int v[], int n) {
    int low, high, mid;
    
    low = 0;
    high = n - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else
            return mid;
    }
    return -1;
}


int atoi(char s[]) {
    int i, n, sign;
    
    for (i = 0; isspace(s[i]); i++)
        ;
    sign = (s[i] == '-') ? -1 : 1;
    if (s[i] == '+' || s[i] == '-')
        i++;
    for (n = 0; isdigit(s[i]); i++)
        n = 10 * n + (s[i] - '0');
    return sign * n;
}


void shellsort(int v[], int n) {
    int gap, i, j, temp;
    
    for (gap = n/2; gap > 0; gap /= 2)
        for (i = gap; i < n; i++)
            for (j = i-gap; j>=0 && v[j] > v[j+gap]; j-=gap) {
                temp = v[j];
                v[j] = v[j+gap];
                v[j+gap] = temp;
            }
}


void reverse(char s[]) {
    int c, i, j;
    
    for (i = 0, j = strlen(s)-1; i < j; i++, j--) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}


void itoa(int n, char s[]) {
    int i, sign;

    if ((sign = n) < 0)
        n = -n;
    i = 0;
    do {
        s[i++] = n % 10 + '0';
    } while ((n /= 10) > 0);
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}


int trim(char s[]) {
    int n;

    for (n = strlen(s)-1; n >= 0; n--) {
        if (s[n] != ' ' && s[n] != '\t' && s[n] != '\n')
            break;
    }
    s[n+1] = '\0';
    return n;
}


int main(int argc, char *argv[]) {
    int v[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    printf("%d\n", binsearch(6, v, 9));

    char s[] = "-21352";
    printf("%d\n", atoi(s));

    shellsort(v, 9);
    for (int i = 0; i < 9; i++)
        printf("%d ", v[i]);

    char s1[] = "abcdefg";
    reverse(s1);
    printf("\n%s\n", s1);

    int n = -223345;
    char s2[10];
    itoa(n, s2);
    printf("%s\n", s2);

    char s3[] = "abcde f   ";
    printf("%d\n", trim(s3));
    printf("%s\n", s3);
    printf("%d\n", strlen(s3));
    return 0;
}
