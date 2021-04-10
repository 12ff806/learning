#include <stdio.h>


/*
 * Time Complexity: O(N^3)
 */
int max_subsequence_sum_v1(const int a[], int n) {
    int this_sum, max_sum, i, j, k;
    
    max_sum = 0;
    for (i = 0; i < n; i++) {
        for (j = i; j < n; j++) {
            this_sum = 0;
            for (k = i; k <= j; k++) {
                this_sum += a[k];
                if (this_sum > max_sum) {
                    max_sum = this_sum;
                }
            }
        }
    }
    return max_sum;
}


/*
 * Time Complexity: O(N^2)
 */
int max_subsequence_sum_v2(const int a[], int n) {
    int this_sum, max_sum, i, j;

    max_sum = 0;
    for (i = 0; i < n; i++) {
        this_sum = 0;
        for (j = i; j < n; j++) {
            this_sum += a[j];
            if (this_sum > max_sum) {
                max_sum = this_sum;
            }
        }
    }
    return max_sum;
}


/*
 * Time Complexity: O(NlogN)
 */
int max(int a, int b) {
    return a > b ?: a, b;
}

int max3(int a, int b, int c) {
    return max(a, max(b, c));
}

int max_sub_sum_v3(const int a[], int left, int right) {
    int max_left_sum, max_right_sum;
    int max_left_border_sum, max_right_border_sum;
    int left_border_sum, right_border_sum;
    int center, i;

    /* Base Case */
    if (left == right) {
        if (a[left] > 0)
            return a[left];
        else
            return 0;
    }

    center = (left + right) / 2;
    max_left_sum = max_sub_sum_v3(a, left, center);
    max_right_sum = max_sub_sum_v3(a, center + 1, right);

    max_left_border_sum = 0; left_border_sum = 0;
    for (i = center; i >= left; i--) {
        left_border_sum += a[i];
        if (left_border_sum > max_left_border_sum)
            max_left_border_sum = left_border_sum;
    }
    
    max_right_border_sum = 0; right_border_sum = 0;
    for (i = center+1; i <= right; i++) {
        right_border_sum += a[i];
        if (right_border_sum > max_right_border_sum)
            max_right_border_sum = right_border_sum;
    }

    return max3(max_left_sum, max_right_sum, 
            max_left_border_sum + max_right_border_sum);
}

int max_subsequence_sum_v3(const int a[], int n) {
    return max_sub_sum_v3(a, 0, n -1);
}


/*
 * Time Complexity: O(N)
 */
int max_subsequence_sum_v4(const int a[], int n) {
    int this_sum, max_sum, i;
    
    this_sum = max_sum = 0;
    for (i = 0; i < n; i++) {
        this_sum += a[i];

        if (this_sum > max_sum) {
            max_sum = this_sum;
        }
        else if (this_sum < 0) {
            this_sum = 0;
        }
    }
    return max_sum;
}


int main(int argc, char *argv[]) {
    int a[] = {-2, 11, -4, 13, -5, -2};
    int n = sizeof(a) / sizeof(int);

    int r1 = max_subsequence_sum_v1(a, n);
    printf("v1 return value: %d\n", r1);

    int r2 = max_subsequence_sum_v2(a, n);
    printf("v2 return value: %d\n", r2);

    int r3 = max_subsequence_sum_v3(a, n);
    printf("v3 return value: %d\n", r3);

    int r4 = max_subsequence_sum_v4(a, n);
    printf("v4 return value: %d\n", r4);
    
    return 0;
}

