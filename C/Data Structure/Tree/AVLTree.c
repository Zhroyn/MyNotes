#include <stdio.h>
#include <stdlib.h>
typedef struct AVLNode *AVLTree;
struct AVLNode{
    int Data;
    int height;
    AVLTree left;
    AVLTree right;
};

int GetHeight(AVLTree T);
AVLTree LLRotation(AVLTree A);
AVLTree RRRotation(AVLTree A);
AVLTree LRRotation(AVLTree A);
AVLTree RLRotation(AVLTree A);
AVLTree Insert(AVLTree T, int X);

int main(void)
{
    int N, X;
    scanf("%d", &N);
    AVLTree T = NULL;
    for(int i=0;i<N;i++)
    {
        scanf("%d", &X);
        T = Insert(T, X);
    }
    printf("%d", T->Data);
}

int GetHeight(AVLTree T)
{
    if(!T) return -1;
    else{
        int a = GetHeight(T->left);
        int b = GetHeight(T->right);
        return (a > b ? a : b) + 1;
    }
}
AVLTree LLRotation(AVLTree A)
{
    AVLTree B = A->left;
    A->left = B->right;
    B->right = A;
    A->height = GetHeight(A);
    B->height = GetHeight(B);
    return B;
}
AVLTree RRRotation(AVLTree A)
{
    AVLTree B = A->right;
    A->right = B->left;
    B->left = A;
    A->height = GetHeight(A);
    B->height = GetHeight(B);
    return B;
}
AVLTree LRRotation(AVLTree A)
{
    A->left = RRRotation(A->left);
    return LLRotation(A);
}
AVLTree RLRotation(AVLTree A)
{
    A->right = LLRotation(A->right);
    return RRRotation(A);
}
AVLTree Insert(AVLTree T, int X)
{
    if(!T){
        T = (AVLTree)malloc(sizeof(struct AVLNode));
        T->Data = X; T->left = T->right = NULL;
    }else if(X < T->Data){
        T->left = Insert(T->left, X);
        if(GetHeight(T->left) - GetHeight(T->right) == 2){
            if(X < T->left->Data) T = LLRotation(T);
            else T = LRRotation(T);
        }
    }else if(X > T->Data){
        T->right = Insert(T->right, X);
        if(GetHeight(T->right) - GetHeight(T->left) == 2){
            if(X > T->right->Data) T = RRRotation(T);
            else T = RLRotation(T);
        }
    }
    T->height = GetHeight(T);
    return T;
}