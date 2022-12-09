#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int ElementType;
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data; /* 存储结点数据 */
    PtrToNode   Next; /* 指向下一个结点的指针 */
};
typedef PtrToNode List; /* 定义单链表类型 */


void K_Reverse( List L, int K )
{
    List t[K];
    List p = L, prev = L;
    while (p) {
        for (int i=0; i<K && p; i++) {
            p = p->Next;
            t[i] = p;
        }
        if (p) {
            p = t[0];
            p->Next = t[K-1]->Next;
            for (int i=K-1; i>0; i--) {
                t[i]->Next = t[i-1];
            }
            prev->Next = t[K-1];
            p = prev = t[0];
        }
    }
}

int main()
{
    List L1 = (List)malloc(sizeof(struct Node));
    List L2 = (List)malloc(sizeof(struct Node));
    List L3 = (List)malloc(sizeof(struct Node));
    List L4 = (List)malloc(sizeof(struct Node));
    List L5 = (List)malloc(sizeof(struct Node));
    List L6 = (List)malloc(sizeof(struct Node));
    L1->Data = 1;
    L2->Data = 2;
    L3->Data = 3;
    L4->Data = 4;
    L5->Data = 5;
    L6->Data = 6;
    L1->Next = L2;
    L2->Next = L3;
    L3->Next = L4;
    L4->Next = L5;
    L5->Next = L6;
    L6->Next = NULL;
    List L = (List)malloc(sizeof(struct Node));
    L->Next = L1;
    K_Reverse(L, 3);
}