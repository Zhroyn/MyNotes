#include <stdio.h>
#include <stdlib.h>
#define MaxSize 100
int BinarySearch(int L[], int X);

int main(void)
{
	//int L[MaxSize + 1];
	//L[0] = 0;
	int L[6] = {5,8,6,4,2,7};
	int X = 4;
	int post = BinarySearch(L, X);
	printf("%d\n", post);
}
int BinarySearch(int L[], int X)
{
	int left = 1;
	int right = L[0];
	while(left <= right) 
	{
		if (X == L[(left + right) / 2])
			return (left + right) / 2;
		if (X < L[(left + right) / 2])
			right = (left + right) / 2 - 1;
		else 
			left = (left + right) / 2 + 1;
	}
	return 0;
}
