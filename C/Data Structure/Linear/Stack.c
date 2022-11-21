#include <stdio.h>
#include <stdlib.h>
typedef struct SNode *Stack;
struct SNode{
    int *Data;
    int Top;
    int MaxSize;
};

Stack CreateStack(int MaxSize);
void Push(Stack S, int X);
int Pop(Stack S);
int IsEmpty(Stack S);
int IsFull( Stack S );

int main(void)
{
    int MaxSize = 10;
    Stack S = CreateStack(MaxSize);
    Push(S, 5); Push(S, 7); Push(S, 1); Push(S, 9);
    printf("%d ", Pop(S));
    printf("%d ", Pop(S));
}

Stack CreateStack(int MaxSize)
{
    Stack S = (Stack)malloc(sizeof(struct SNode));
    S->Data = (int *)malloc(MaxSize * sizeof(int));
    S->Top = -1;
    S->MaxSize = MaxSize;
    return S;
}
void Push(Stack S, int X)
{
    S->Data[++S->Top] = X;
}
int Pop(Stack S)
{
    return S->Data[S->Top--];
}
int IsEmpty(Stack S)
{
    return (S->Top == -1);
}
int IsFull( Stack S )
{
    return (S->Top == S->MaxSize-1);
}