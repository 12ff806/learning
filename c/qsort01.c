#include <stdio.h>


void qsort(int v[], int left, int right);


int main(int argc, char *argv[])
{
    int v[] = {5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8};
    qsort(v, 0, 10);
    for (int i = 0; i <= 10; i++)
        printf("%d ", v[i]);

    return 0;
}


void qsort(int v[], int left, int right)
{
    int i, last;
    void swap(int v[], int i, int j);

    if (left >= right)
        return;
    //swap(v, left, (left + right)/2);
    last = left;
    for (i = left+1; i <= right; i++)
        if (v[i] < v[left])
            swap(v, ++last, i);
    swap(v, left, last);

    qsort(v, left, last-1);
    qsort(v, last+1, right);
}


void swap(int v[], int i, int j)
{
    int temp;
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}
