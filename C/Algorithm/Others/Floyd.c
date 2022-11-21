#include <stdio.h>
#include <stdlib.h>
#define INFINITY 100000
#define MaxVertexNum 100
typedef struct GNode{
    int Nv, Ne;
    int D[MaxVertexNum+1][MaxVertexNum+1];
} *Graph;

Graph BuiltGragh(int Nv, int Ne);
void Floyd(Graph G);

int main(void)
{
    int Nv, Ne;
    scanf("%d %d", &Nv, &Ne);
    Graph G = BuiltGragh(Nv, Ne);
    Floyd(G);
    
    for(int i=1;i<=Nv;i++)
    {
        for(int j=1;j<=Nv;j++)
            printf("%6d ", G->D[i][j]);
        printf("\n");
    }
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

void Floyd(Graph G)
{
    for(int k=1;k<=G->Nv;k++)
        for(int i=1;i<=G->Nv;i++)
            for(int j=1;j<=G->Nv;j++)
            {
                if(i!=j && G->D[i][k]+G->D[k][j] <= G->D[i][j])
                    G->D[i][j] = G->D[i][k] + G->D[k][j];
            }
}
Graph BuiltGragh(int Nv, int Ne)
{
    Graph G = (Graph)malloc(sizeof(struct GNode));
    G->Nv = Nv; G->Ne = Ne;
    int v1, v2, w;
    for(v1=1;v1<=Nv;v1++)
    {
        for(v2=1;v2<=Nv;v2++) G->D[v1][v2] = INFINITY;
    }
    for(int i=0;i<Ne;i++)
    {
        scanf("%d %d %d", &v1, &v2, &w);
        G->D[v1][v2] = w;
        G->D[v2][v1] = w;
    }
    return G;
}