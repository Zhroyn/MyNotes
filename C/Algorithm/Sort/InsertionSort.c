#include <stdio.h>

void InsertionSort(int A[], int N)
{
    int i, j, tmp;
    for (i = 1; i < N; i++)
    {
        tmp = A[i];
        for (j = i; j > 0 && A[j - 1] > tmp; j--)
            A[j] = A[j - 1];
        A[j] = tmp;
    }
}

int main(void)
{
    int N;
    scanf("%d", &N);
    int A[N];
    for(int i=0;i<N;i++) scanf("%d", &A[i]);
    InsertionSort(A, N);
}
/*
10
3 1 2 8 7 5 9 4 6 0
*/