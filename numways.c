#include <stdio.h>
#include <stdlib.h>

static int cmp(const void *p1, const void *p2)
{
	return *((int *) p1) > *((int *) p2); 
}

int numberOfWays(int arr[], int n, int k) {
	// Write your code here
	int l, r;
	int count;

	if (n < 2)
		return 0;

	qsort(arr, n, sizeof(int), cmp);

	count = 0;
	l = 0; r = n - 1;
	while (l < r) {
		int s = arr[l] + arr[r];
		if (s == k) {
			if (arr[l] == arr[r]) {
				int rep = r - l + 1;
				count += rep * (rep - 1) / 2;
				break;
			} else {
				int lcount = 1;
				int rcount = 1;
				int tmp;
				tmp = arr[l];
				for (++l; arr[l] == tmp && l < r; ++l)
					++lcount;
				tmp = arr[r];
				for (--r; arr[r] == tmp && l < r ; --r)
					++rcount;
				count += lcount * rcount;
			}
		} else if (s < k) {
			++l;
		} else {
			--r;
		}
	}

	return count;
}

int main()
{
	{
		int nums[] = {1, 2, 3, 4, 3};
		int res = numberOfWays(nums, sizeof(nums)/sizeof(nums[0]), 6);
		printf("res %d\n", res);
	}
	{
		int nums[] = {1, 5, 3, 3, 3};
		int res = numberOfWays(nums, sizeof(nums)/sizeof(nums[0]), 6);
		printf("res %d\n", res);
	}
}
