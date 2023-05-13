#include <stdio.h>

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

void BubbleSort(int a[], int N) {
    for (int i = 0; i < N; i++) {
        for (int j = N - 1; j > i; j--) {
            if (a[j - 1] > a[j]) {
                swap(&a[j], &a[j - 1]);
            }
        }
    }
}
void InsertSort(int a[], int N)
{
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (a[i] > a[j]) {
                swap(&a[i], &a[j]);
            }
        }
    }
}

int main(void)
{
    int N = 10;
    int a[] = {3, 1, 2, 8, 7, 5, 9, 4, 6, 0};
    BubbleSort(a, N);
    for(int i = 0; i < N; i++)
        printf("%d ", a[i]);
}
