#include <stdio.h>

void swap( int a[], int i, int j)
{
    int t = a[i];
    a[i] = a[j];
    a[j] = t;
}
int Partition ( int a[], int low, int high )
{
    int pivot = a[high];
    int i = low, j = high;
    while(i < j)
    {
        while(i < j && a[i] <= pivot) i++;
        while(i < j && a[j] >= pivot) j--;
        swap(a, i, j);
    }
    swap(a, i, high);
    return i;
}
void QuickSort ( int a[], int low, int high ) 
{ 
    if(low < high)
    {
        int p = Partition(a, low, high) ;
        QuickSort(a, low, p - 1) ; 
        QuickSort(a, p + 1, high);
     }
}

int main()
{
    int a[10] = {5, 2, 4, 1, 8, 9, 10, 12, 3, 6};
    QuickSort(a, 0, 9);
    for(int i=0; i<10; i++)
        printf("%d ", a[i]);
}
