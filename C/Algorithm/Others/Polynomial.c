#include <stdio.h>
#include <stdlib.h>
typedef struct PNode *Polynomial;
struct PNode {
    int coef;
    int expo;
    struct PNode *next;
};
void Attach(int coef, int expo, Polynomial *Rear);
void PrintP(Polynomial p);
Polynomial ReadP(void);
Polynomial CopyP(Polynomial p);
Polynomial MultP(Polynomial p1, Polynomial p2);
Polynomial PlusP(Polynomial p1, Polynomial p2);

int main(void) {
    Polynomial p1, p2, p3, p4;
    p1 = ReadP();
    p2 = ReadP();
    p3 = MultP(p1, p2);
    p4 = PlusP(p1, p2);
    PrintP(p3);
    printf("\n");
    PrintP(p4);
}

void Attach(int coef, int expo, Polynomial *Rear) {
    Polynomial p = (Polynomial)malloc(16);
    p->coef = coef; p->expo = expo; p->next = NULL;
    (*Rear)->next = p;
    *Rear = p;
}
void PrintP(Polynomial p) {
    if(!p) {
        printf("0 0");
    } else {
        int tag = 0;
        while(p) {
            if(tag) {printf(" ");} else {tag=1;}
            printf("%d %d", p->coef, p->expo);
            p = p->next;
        }
    }
}
Polynomial ReadP(void) {
    int n;
    scanf("%d", &n);
    if(n==0) return NULL;
    Polynomial Head = (Polynomial)malloc(16); Head->next = NULL;
    Polynomial Rear = Head;
    for(int i=1;i<=n;i++){
        int c, e;
        scanf("%d %d", &c, &e);
        Attach(c, e, &Rear);
    }
    Polynomial t = Head; Head = Head->next; free(t);
    return Head;
}
Polynomial CopyP(Polynomial p){
    Polynomial Head = (Polynomial)malloc(16); Head->next = NULL;
    Polynomial Rear = Head;
    while(p){
        Attach(p->coef, p->expo, &Rear);
        p = p->next;
    }
    Polynomial t = Head; Head = Head->next; free(t);
    return Head;
}
Polynomial PlusP(Polynomial p1, Polynomial p2) {
    if(!p1 && !p2) return NULL;
    Polynomial Head = (Polynomial)malloc(16); Head->next = NULL;
    Polynomial Rear = Head;
    while(p1 && p2){
        if(p1->expo>p2->expo){
            Attach(p1->coef, p1->expo, &Rear);
            p1 = p1->next;
        }
        else if(p1->expo<p2->expo){
            Attach(p2->coef, p2->expo, &Rear);
            p2 = p2->next;
        }
        else {
            int c = p1->coef+p2->coef;
            if(c!=0) Attach(c,p1->expo,&Rear);
            p1 = p1->next; p2 = p2->next;
        }
    }
    while(p1) {Attach(p1->coef,p1->expo,&Rear); p1 = p1->next;}
    while(p2) {Attach(p2->coef,p2->expo,&Rear); p2 = p2->next;}
    Polynomial t = Head; Head = Head->next; free(t);
    return Head;
}
Polynomial MultP(Polynomial p1, Polynomial p2){
    Polynomial p = NULL;
    if(!p1 || !p2) return p;
    while(p1){
        Polynomial p3, t;
        Polynomial p4 = CopyP(p2);
        p3 = t = p4;
        while(t){
            t->coef *= p1->coef;
            t->expo += p1->expo;
            t = t->next;
        }
        p = PlusP(p, p3);
        p1 = p1->next;
    }
    return p;
}