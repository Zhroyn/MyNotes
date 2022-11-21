#include <stdio.h>
#include <stdlib.h>
typedef struct TNode *BinTree;
struct TNode{
    int Data;
    BinTree left;
    BinTree right;
};

BinTree Insert( BinTree BST, int X );
BinTree Delete( BinTree BST, int X );
BinTree Find( BinTree BST, int X );
BinTree FindMin( BinTree BST );
BinTree FindMax( BinTree BST );

int main()
{
    BinTree BST, MinP, MaxP, Tmp;
    int X;
    int N, i;

    BST = NULL;
    scanf("%d", &N);
    for ( i=0; i<N; i++ ) {
        scanf("%d", &X);
        BST = Insert(BST, X);
    }
    MinP = FindMin(BST);
    MaxP = FindMax(BST);
    scanf("%d", &N);
    for( i=0; i<N; i++ ) {
        scanf("%d", &X);
        Tmp = Find(BST, X);
        if (Tmp == NULL) printf("%d is not found\n", X);
        else {
            printf("%d is found\n", Tmp->Data);
            if (Tmp==MinP) printf("%d is the smallest key\n", Tmp->Data);
            if (Tmp==MaxP) printf("%d is the largest key\n", Tmp->Data);
        }
    }
    scanf("%d", &N);
    for( i=0; i<N; i++ ) {
        scanf("%d", &X);
        BST = Delete(BST, X);
    }
    printf("%d ", BST->left->Data);
/*10
5 8 6 2 4 1 0 10 9 7
5
6 3 10 0 5
5
5 7 0 10 3*/
}
BinTree Insert( BinTree BST, int X )
//若无返回值，则BST为NULL时无法插入;当X已存在时不会再插入
{
    BinTree new = (BinTree)malloc(sizeof(struct TNode));
    new->Data = X; new->left = new->right = NULL;
    if(!BST) return new;
    
    BinTree t = BST, pre;
    while(t)
    {
        pre = t;
        if(X < t->Data) t = t->left;
        else if(X > t->Data) t = t->right;
        else if(X == t->Data) return BST;
    }
    if(X < pre->Data) pre->left = new;
    else pre->right = new;
    return BST;
}
BinTree Delete( BinTree BST, int X )
{
    BinTree t = BST, pre;
    if(!BST) return NULL;
    if(X == BST->Data){
        if(!BST->left && !BST->right){
            free(BST); return NULL;
        }
        else if(!BST->left || !BST->right){
            if(BST->left) t = BST->left;
            else t = BST->right;
            free(BST); return t;
        }
    }

    while(X != t->Data){
        pre = t;
        if(X < t->Data) t = t->left;
        else if(X > t->Data) t = t->right;
        if(!t) return BST;
    }
    if(t->left && t->right){
        BinTree tmp = t;
        t = t->right;
        while(t->left) {pre = t; t = t->left;}
        tmp->Data = t->Data;
    }
    if(t->left){
        if(t->Data < pre->Data) pre->left = t->left;
        else pre->right = t->left;
    }
    else{
        if(t->Data < pre->Data) pre->left = t->right;
        else pre->right = t->right;
    }
    free(t); return BST;
}
BinTree Find( BinTree BST, int X )
{
    while(BST && X != BST->Data)
    {
        if(X < BST->Data) BST = BST->left;
        else BST = BST->right;
    }
    return BST;
}
BinTree FindMin( BinTree BST )
{
    if(BST){
        while(BST->left) BST = BST->left;
    }
    return BST;
}
BinTree FindMax( BinTree BST )
{
    if(BST){
        while(BST->right) BST = BST->right;
    }
    return BST;
}