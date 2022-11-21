#include <stdio.h>
#define MAXN 10
void newcor(double a[], double newa[], double Inver[][3])
{
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            newa[i] += Inver[i][j]*a[j];

    for(int i=0;i<3;i++)
        printf("%lf ", newa[i]);
    printf("\n");
}
double inner(double a[], double b[], double Base[][3])
{
    double T[3][3] = {0};
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            for(int k=0;k<3;k++)
                T[i][j] += Base[k][i]*Base[k][j];
    double result = 0;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            result += a[i]*b[j]*T[i][j];
    return result;
}

int main()
{
    double E[3][3] = {
        1,0,0,
        0,1,0,
        0,0,1
    };
    double A[3][3] = {
        2,1,1,
        1,2,1,
        0,0,1
    };
    double InverA[3][3] = {
        {2.0/3,-1.0/3,-1.0/3,},
        {-1.0/3,2.0/3,-1.0/3,},
        {0,0,1}
    };
    double a[3] = {2,4,5};
    double b[3] = {13,-0.15,1};
    double newa[3] = {0}, newb[3] = {0};

    newcor(a, newa, InverA);
    newcor(b, newb, InverA);
    printf("%lf\n", inner(a, b, E));
    printf("%lf\n", inner(newa, newb, A));
}
