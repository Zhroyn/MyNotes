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
void mergesort(int a[], int t[], int left, int right) {
    if (left < right) {
        int mid = (left + right + 1) / 2;
        mergesort(a, t, left, mid - 1);
        mergesort(a, t, mid, right);
        Merge(a, t, left, right);
    }
}

void MergeSort(int a[], int N) {
    int t[N];
    mergesort(a, t, 0, N-1);
}

int main(void)
{
    int a[10] = {5, 2, 4, 1, 8, 9, 10, 12, 3, 6};
    int b[10] = {3, 1, 2, 8, 7, 5, 9, 4, 6, 0};
    MergeSort(a, 10);
    MergeSort(b, 10);
    for(int i = 0; i < 10; i++)
        printf("%d ", a[i]);
    printf("\n");
    for(int i = 0; i < 10; i++)
        printf("%d ", b[i]);
    printf("\n");
}