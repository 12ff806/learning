#include <stdio.h>


/*
 * Time Complexity: O(logN)
 */
int binary_search(const int a[], int x, int n) {
    int low, mid, high;

    low = 0; high = n - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        if (a[mid] < x) {
            low = mid + 1;
        }
        else if (a[mid] > x) {
            high = mid - 1;
        }
        else
            return mid;
    }
    return -1;
}


int main(int argc, char *argv[]) {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100};
    int n = sizeof(a) / sizeof(int);
    int r = binary_search(a, 6, n);
    printf("r value: %d\n", r);
}

