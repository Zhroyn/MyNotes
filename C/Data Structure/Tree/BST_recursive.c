#include <stdio.h>
#include <stdlib.h>
typedef struct TNode *BinTree;
struct TNode{
    int Data;
    BinTree left;
    BinTree right;
};

BinTree Insert(BinTree BST, int X);
BinTree Delete(BinTree BST, int X);
BinTree Find(BinTree BST, int X);
BinTree FindMin(BinTree BST);
BinTree FindMax(BinTree BST);

int main()
{
    BinTree BST, MinP, MaxP, Tmp;
    int X;
    int N, i;

    BST = NULL;
    scanf("%d", &N);
    //10
    //5 8 6 2 4 1 0 10 9 7
    for ( i=0; i<N; i++ ) {
        scanf("%d", &X);
        BST = Insert(BST, X);
    }
    MinP = FindMin(BST);
    MaxP = FindMax(BST);
    printf("%d ", MinP->Data);
    printf("%d ", MaxP->Data);
    MinP = FindMin(BST);
    MaxP = FindMax(BST);
    printf("%d ", MinP->Data);
    printf("%d ", MaxP->Data);
}

BinTree Insert(BinTree BST, int X)
//当X已存在时不会再插入
{
    if(!BST){
        BST = (BinTree)malloc(sizeof(struct TNode));
        BST->Data = X; BST->left = BST->right = NULL;
    }else{
        if(X < BST->Data)
            BST->left = Insert(BST->left, X);
        else if(X > BST->Data)
            BST->right = Insert(BST->right, X);
    }
    return BST;
}
BinTree Delete(BinTree BST, int X)
{
    if(!BST) return NULL;
    
    if(X < BST->Data) BST->left = Delete(BST->left, X);
    else if(X > BST->Data) BST->right = Delete(BST->right, X);
    else{
        BinTree t;
        if(BST->left && BST->right){
            t = FindMin(BST->right);
            BST->Data = t->Data;
            BST->right = Delete(BST->right, BST->Data);
        }else{
            t = BST;
            if(!BST->left) BST = BST->right;
            else if(!BST->right) BST = BST->left;
            free(t);
        }
    }
    return BST;
}
BinTree Find(BinTree BST, int X)
{
    if(!BST || X == BST->Data) return BST;
    else if(X < BST->Data) return Find(BST->left, X);
    else if(X > BST->Data) return Find(BST->right, X);
}
BinTree FindMin(BinTree BST)
{
    if(BST){
        while(BST->left) BST = BST->left;
    }
    return BST;
}
BinTree FindMax(BinTree BST)
{
    if(BST){
        while(BST->right) BST = BST->right;
    }
    return BST;
}