#include <stdio.h>

void Merge(int a[], int tmp[], int left, int right, int end)
{
    int i = left;
    int p1 = left, p2 = right;
    while (p1 < right && p2 <= end)
    {
        if(a[p1] < a[p2]) tmp[i++] = a[p1++];
        else tmp[i++] = a[p2++];
    }
    while(p1 < right) tmp[i++] = a[p1++];
    while(p2 <= right) tmp[i++] = a[p2++];
    for(i = left; i <= end; i++) a[i] = tmp[i];
}

void MergeSort(int a[], int N)
{
    int tmp[N], length = 1;
    int i;
    while (length < N)
    {
        for (i = 0; i + 2*length < N; i += 2*length)
            Merge(a, tmp, i, i+length, i+2*length-1);
        if (i + length < N)
            Merge(a, tmp, i, i+length, N-1);
        length *= 2;
    }
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