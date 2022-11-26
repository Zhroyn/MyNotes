#include <stdio.h>


int main()
{
    int h, m;
    double s;
//     scanf(" %d : %d : %lf", &h, &m, &s);
    scanf(" %d ", &h);
    getchar();
    scanf(" %d ", &m);
    getchar();
    scanf(" %lf", &s);
    printf("%d:%d:%lf", h, m, s);
}
