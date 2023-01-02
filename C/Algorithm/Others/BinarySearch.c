#include <stdio.h>

int BinarySearch(int a[], int N, int x)
{
	int left = 1, right = N - 1, mid;
	while(left <= right) 
	{
		mid = (left + right) / 2;
		if (x == a[mid])
			return mid;
		if (x < a[mid])
			right = mid - 1;
		else 
			left = mid + 1;
	}
	return -1;
}

int main(void)
{
	int N = 6;
	int a[] = {5,8,6,4,2,7};
	int x = 4;
	int post = BinarySearch(a, N, x);
	printf("%d\n", post);
}
