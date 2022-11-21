#include <stdio.h>
#include <stdlib.h>
typedef struct QNode{
    int *Data;
    int front, rear;
    int MaxSize;
} *Queue;

Queue CreateQueue(int MaxSize)
{
    Queue Q = (Queue)malloc(sizeof(struct QNode));
    Q->Data = (int *)malloc((MaxSize + 1)*sizeof(int));
    Q->front = Q->rear = 0;
    Q->MaxSize = MaxSize + 1;
    return Q;
}
void Enqueue(Queue Q, int X)
{
    Q->rear = (Q->rear+1) % Q->MaxSize;
    Q->Data[Q->rear] = X;
}
int Dequeue(Queue Q)
{
    Q->front = (Q->front+1) % Q->MaxSize;
    return Q->Data[Q->front];
}
int IsEmpty(Queue Q)
{
    return (Q->front == Q->rear);
}
int IsFull(Queue Q)
{
    return ((Q->rear+1)%Q->MaxSize == Q->front);
}

int main(void)
{
    int MaxSize = 4;
    Queue Q = CreateQueue(MaxSize);
    Enqueue(Q, 5); Enqueue(Q, 1); Enqueue(Q, 9); Enqueue(Q, 6);
    printf("%d ", Dequeue(Q));
    printf("%d ", Dequeue(Q));
}