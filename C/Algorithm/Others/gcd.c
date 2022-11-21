#include <stdio.h>

int gcd(int a, int b)
{
    int r;
    while(b)
    {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main()
{
    printf("%d\n", gcd(5,7));
    printf("%d\n", gcd(15,5));
    printf("%d\n", gcd(1573,1364));
}