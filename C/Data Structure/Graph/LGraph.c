#include <stdio.h>
#include <stdlib.h>
#define MaxVertexNum 1000

typedef struct AdjVNode{
    int v, weight;
    struct AdjVNode *next;
} *AdjV; 
typedef struct VNode{
    AdjV FirstEdge;
} AdjList[MaxVertexNum];
typedef struct GNode{
    int Nv, Ne;
    AdjList G;
} *Graph;

void InsertEdge(Graph G, int v1, int v2, int w)
{
    AdjV NewV = (AdjV)malloc(sizeof(struct VNode));
    NewV->v = v2; NewV->weight = w;
    NewV->next = G->G[v1].FirstEdge;
    G->G[v1].FirstEdge = NewV;
}
Graph BuildGraph(int Nv, int Ne)
{
    Graph G = (Graph)malloc(sizeof(struct GNode));
    G->Nv = Nv; G->Ne = Ne;
    for(int i=1;i<=Nv;i++) G->G[i].FirstEdge = NULL;

    int v1, v2, w;
    for(int i=0;i<Ne;i++)
    {
        scanf("%d %d %d", &v1, &v2, &w);
        InsertEdge(G, v1, v2, w);
        InsertEdge(G, v2, v1, w);
    }
    return G;
}

int main(void)
{
    int Nv, Ne;
    scanf("%d %d", &Nv, &Ne);
    Graph G = BuildGraph(Nv, Ne);
    printf("%d", G->G[5].FirstEdge->next->next->v);
}
/*6 11
3 4 70
1 2 1
5 4 50
2 6 50
5 6 60
1 3 70
4 6 60
3 6 80
5 1 100
2 4 60
5 2 80*/