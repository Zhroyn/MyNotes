#include <stdio.h>

void swap( int *a, int *b ) {
    int t = *a;
    *a = *b;
    *b = t;
}
#define A 1
#if A == 1
int Partition ( int a[], int left, int right )
{
    int i = left, j = right;
    while (i < j) {
        while (i < j && a[i] <= a[right]) i++;
        while (i < j && a[j] >= a[right]) j--;
        swap(&a[i], &a[j]);
    }
    swap(&a[i], &a[right]);
    return i;
}
#else
int Partition(int a[], int left, int right) {
    int p = left;
    for (int i = left; i < right; i++) {
        if (a[i] < a[right]) {
            swap(&a[p++], &a[i]);
        }
    }
    swap(&a[p], &a[right]);
    return p;
}
#endif
void QSort ( int a[], int left, int right ) 
{ 
    if(left < right)
    {
        int p = Partition(a, left, right);
        QSort(a, left, p - 1) ; 
        QSort(a, p + 1, right);
     }
}

void QuickSort(int a[], int N) {
    QSort(a, 0, N);
}

int main(void)
{
    int N = 10;
    int a[] = {3, 1, 2, 8, 7, 5, 9, 4, 6, 0};
    QuickSort(a, N);
    for(int i = 0; i < N; i++)
        printf("%d ", a[i]);
}
