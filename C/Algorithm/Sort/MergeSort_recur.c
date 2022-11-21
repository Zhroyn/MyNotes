#include <stdio.h>

void Merge(int a[], int tmp[], int left, int right)
{
    int i = left, mid = (left+right)/2;
    int p1 = left, p2 = mid + 1;
    while (p1 <= mid && p2 <= right)
    {
        if(a[p1] < a[p2]) tmp[i++] = a[p1++];
        else tmp[i++] = a[p2++];
    }
    while(p1 <= mid) tmp[i++] = a[p1++];
    while(p2 <= right) tmp[i++] = a[p2++];
    for(i = left; i <= right; i++) a[i] = tmp[i];
}
void mergesort(int a[], int tmp[], int left, int right)
{
    if(left < right)
    {
        mergesort(a, tmp, left, (left+right)/2);
        mergesort(a, tmp, (left+right)/2 + 1, right);
        Merge(a, tmp, left, right);
    }
}
void MergeSort(int a[], int N)
{
    int tmp[N];
    mergesort(a, tmp, 0, N-1);
}

int main(void)
{
    int a[10] = {5, 2, 4, 1, 8, 9, 10, 12, 3, 6};
    int b[10] = {3, 1, 2, 8, 7, 5, 9, 4, 6, 0};
    MergeSort(a, 10);
    MergeSort(b, 10);
    for(int i=0;i<10;i++) printf("%d ", a[i]);
    printf("\n");
    for(int i=0;i<10;i++) printf("%d ", b[i]);
    printf("\n");
}