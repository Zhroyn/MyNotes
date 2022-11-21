#include <stdio.h>
#include <stdlib.h>
typedef struct VNode{
    int v;
    int weight;
    struct VNode *AdjV;
} *Vertex;
typedef struct GNode{
    int Nv, Ne;
    Vertex *G;
} *Graph;
// adjas (ofdofna) asd [of] na dsfa AbC abc ABC aBC
int main(void)
{
    Graph G = (Graph)malloc(sizeof(struct GNode));
    G->G = malloc( 50*sizeof(struct VNode) );
    G->G[0]->v = 0;
    printf(".");
    G->G[1]->v = 1;
    printf(".");
    G->G[2]->v = 2;
    printf(".");
    printf("%d", G->G[2]->v);
}