#include <stdio.h>
#include <stdlib.h>
#define INFINITY 100000
typedef struct HeapStruct *Heap;
struct HeapStruct{
    int *Elements;
    int Size;
    int MaxSize;
};
Heap CreateHeap(int MaxSize);
void Insert(Heap H, int item);
int Delete(Heap H);

int main(void)
{
    Heap H = CreateHeap(5);
    Insert(H, 5); Insert(H, 9); Insert(H, 4); Insert(H, 6);
    printf("%d ", Delete(H));
    printf("%d ", Delete(H));
}

Heap CreateHeap(int MaxSize)
{
    Heap H = malloc(sizeof(struct HeapStruct));
    H->Elements = malloc((MaxSize + 1)*sizeof(int));
    H->Elements[0] = INFINITY;
    H->Size = 0;
    H->MaxSize = MaxSize;
    return H;
}
void Insert(Heap H, int item)
{
    int i = ++H->Size;
    for(; H->Elements[i/2] < item; i/=2)
        H->Elements[i] = H->Elements[i/2];
    H->Elements[i] = item;
}
int Delete(Heap H)
{
    int MaxItem = H->Elements[1];
    int tmp = H->Elements[H->Size--];
    int Parent, Child;
    for(Parent=1; Parent*2<=H->Size; Parent=Child)
    {
        Child = Parent * 2;
        if((Child!=H->Size) && 
            (H->Elements[Child]<H->Elements[Child+1])) Child++;
        if(tmp >= H->Elements[Child]) break;
        else H->Elements[Parent] = H->Elements[Child];
    }
    H->Elements[Parent] = tmp;
    return MaxItem;
}