#include <stdio.h>


void shellsort(int v[], int n);


int main(int argc, char *argv[])
{
    int v[] = {1, 20, 5, 3, 2, 4, 82, 28, 3, 21, 0, 22};
    int n = 12;
    shellsort(v, n);
    for (int i = 0; i < n; i++)
        printf("%d ", v[i]);
    return 0;
}


void shellsort(int v[], int n)
{
    int gap, i, j, temp;
    
    for (gap = n/2; gap > 0; gap /= 2)
        for (i = gap; i < n; i++)
            for (j = i-gap; j>=0 && v[j] > v[j+gap]; j-=gap) {
                temp = v[j];
                v[j] = v[j+gap];
                v[j+gap] = temp;
            }
}
