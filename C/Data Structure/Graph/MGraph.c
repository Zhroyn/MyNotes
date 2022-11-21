#include <stdio.h>
#include <stdlib.h>
#define MaxVertexNum 1000
typedef struct GNode{
    int Nv, Ne;
    int D[MaxVertexNum+1][MaxVertexNum+1];
} *Graph;

Graph BuildGragh(int Nv, int Ne)
{
    Graph G = (Graph)malloc(sizeof(struct GNode));
    G->Nv = Nv; G->Ne = Ne;
    int v1, v2, w;
    for(v1=1;v1<=Nv;v1++)
    {
        for(v2=1;v2<=Nv;v2++) G->D[v1][v2] = 0;
    }
    for(int i=0;i<Ne;i++)
    {
        scanf("%d %d %d", &v1, &v2, &w);
        G->D[v1][v2] = w;
        G->D[v2][v1] = w;
    }
    return G;
}

int main(void)
{
    int Nv, Ne;
    scanf("%d %d", &Nv, &Ne);
    Graph G = BuiltGragh(Nv, Ne);
}
/*10 9
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10*/