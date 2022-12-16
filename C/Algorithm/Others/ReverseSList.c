#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;
typedef struct Node *List;
struct Node {
    ElementType data;
    List   next;
};

void K_Reverse( List L, int K )
{
    List preTail = L, lastHead = L->next;
    List p;
    int i, j;
    while (p) {
        for (i = 0, p = lastHead; i < K-1 && p; i++, p=p->next);
        if (p) {
            preTail->next = p;
            preTail = lastHead;
            lastHead = p->next;
            for (i = 0; i < K-1; i++) {
                for (j = 0, p = preTail; j < K - i - 2;
                     j++, p = p->next);
                p->next->next = p;
            }
        } else {
            preTail->next = lastHead;
        }
    }
}

List CreateList(ElementType a[], int N)
// Create a single linked list with head node
{
    List head = (List)malloc(sizeof(struct Node));
    head->next = NULL;
    List p = head;
    for (int i = 0; i < N; i++) {
        List t = (List)malloc(sizeof(struct Node));
        t->data = a[i];
        t->next = NULL;
        p->next = t;
        p = p->next;
    }
    return head;
}
void PrintList(List L)
{
    L = L->next;
    while (L) {
        printf("%d ", L->data);
        L = L->next;
    }
    printf("\n");
}

int main()
{
    ElementType a[6] = {1, 2, 3, 4, 5, 6};
    List L = CreateList(a, 6);
    K_Reverse(L, 4);
    PrintList(L);
}