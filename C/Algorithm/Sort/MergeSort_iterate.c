#include <stdio.h>

void Merge(int a[], int t[], int left, int right) {
    int mid = (left + right + 1) / 2;
    int p1 = left, p2 = mid;
    int i = left;
    while (p1 <= mid - 1 && p2 <= right) {
        if (a[p1] < a[p2]) t[i++] = a[p1++];
        else t[i++] = a[p2++];
    }
    while (p1 <= mid - 1) t[i++] = a[p1++];
    while (p2 <= right) t[i++] = a[p2++];
    for (int j = left; j <= right; j++) {
        a[j] = t[j];
    }
}

void MergeSort(int a[], int N) {
    int t[N];
    for (int len = 1; len < N; len *= 2) {
        for (int i = 0; i < N; i += 2 * len) {
            if (i + len < N) {
                Merge(a, t, i, i + 2 * len - 1);
            }
        }
    }
}

int main(void)
{
    int N = 10;
    int a[] = {3, 1, 2, 8, 7, 5, 9, 4, 6, 0};
    MergeSort(a, N);
    for(int i = 0; i < N; i++)
        printf("%d ", a[i]);
}   