#include<stdio.h>
#include<stdlib.h>
typedef  int  KeyType;
typedef  struct 
{                      
  KeyType *elem; /*elem[0]一般作哨兵或缓冲区*/                     
  int Length;      
}SqList;
void f(SqList);

int main()
{
    SqList L;
    int a[11] = {0, 5, 2, 4, 1, 8, 9, 10, 12, 3, 6};
    L.elem = a;
    L.Length = 10;
    int low = 1, high = 10;
    int pivot = a[high];
    int i = low, j = high;
    while(i < j)
    {
        while(i < j && a[i] <= pivot) i++;
        while(i < j && a[j] >= pivot) j--;
        a[i] = a[i] + a[j];
        a[j] = a[i] - a[j];
        a[i] = a[i] - a[j];
    for(int i=1; i<=10; i++)
        printf("%d ", a[i]);
    printf("\n");
    }
    a[i] = a[i] + a[j];
    a[j] = a[i] - a[j];
    a[i] = a[i] - a[j];
    
    for(int i=1; i<=10; i++)
        printf("%d ", a[i]);
    printf("\n");
}

// int Partition ( SqList L, int low,  int high )
// {
//     int pivot = a[high];
//     int i = low, j = high;
//     while(i < j)
//     {
//         while(i < j && a[i] <= pivot) i++;
//         while(i < j && a[j] >= pivot) j--;
//         a[i] = a[i] + a[j];
//         a[j] = a[i] - a[j];
//         a[i] = a[i] - a[j];
//     }
//     a[i] = a[i] + a[j];
//     a[j] = a[i] - a[j];
//     a[i] = a[i] - a[j];
//     return i;
// }