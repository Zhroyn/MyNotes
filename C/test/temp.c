#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int ElementType;
typedef struct Node *PtrToNode;
struct Node {
    ElementType data; /* 存储结点数据 */
    PtrToNode   next; /* 指向下一个结点的指针 */
};
typedef PtrToNode List; /* 定义单链表类型 */


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
void show(struct Node *r){
    printf("%c",'[');
    struct Node *p = r->next;
    do{
        printf("%d,", p->data);
        p=p->next;
    }while(p!=r->next);
    printf("%c", ']');
}

int main()
{
    int a[3] = {1,2,3};
    List L = CreateList(a, 3);
    List r = L->next;
    r->next->next->next = r;
    show(r);
}