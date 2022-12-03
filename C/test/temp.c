#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *readlist()
{
    struct ListNode *sentinel = malloc(sizeof(struct ListNode));
    sentinel->next = NULL;
    struct ListNode *p = sentinel;
    int t;
    scanf("%d", &t);
    while (t != -1) {
        struct ListNode *new = malloc(sizeof(struct ListNode));
        new->data = t; new->next = NULL;
        p->next = new;
        p = p->next;
        scanf("%d", &t);
    }
    return sentinel->next;
}
struct ListNode *getodd( struct ListNode **L )
{
    struct ListNode *senOdd = malloc(sizeof(struct ListNode));
    senOdd->next = NULL;
    struct ListNode *senEven = malloc(sizeof(struct ListNode));
    senEven->next = NULL;
    struct ListNode *p = *L;
    struct ListNode *pOdd = senOdd;
    struct ListNode *pEven = senEven;
    
    while (p) {
        struct ListNode *new = malloc(sizeof(struct ListNode));
        new->data = p->data; new->next = NULL;
        if (p->data % 2) {
            pOdd->next = new;
            pOdd = pOdd->next;
        } else {
            pEven->next = new;
            pEven = pEven->next;
        }
        p = p->next;
    }
    *L = senEven->next;
    return senOdd->next;
}
void printlist( struct ListNode *L )
{
     struct ListNode *p = L;
     while (p) {
           printf("%d ", p->data);
           p = p->next;
     }
     printf("\n");
}

int main()
{
    struct ListNode *L, *Odd;
    L = readlist();
    Odd = getodd(&L);
    printlist(Odd);
    printlist(L);

    return 0;
}