#include <stdio.h>
// Add any extra import statements you may need here
#include <math.h>

// Add any helper functions you may need here


int getBillionUsersDay(float growthRates[], int n) {
	// Write your code here
	double big, small;
	float minRate, maxRate;
	unsigned minEstim, maxEstim;
	double log_n;

	int i, ind;
	minRate = maxRate = growthRates[0];
	for (i = 1; i < n; ++i) {
		if (growthRates[i] < minRate) {
			minRate = growthRates[i];
		} else if (growthRates[i] > maxRate) {
			maxRate = growthRates[i];
		}
	}
	log_n = log10((double) n);
	minEstim = floor(9.0 - log_n) / log10(maxRate); 
	maxEstim = ceil(9.0 - log_n) / log10(minRate);

	/* bin search rightmost */
	while (minEstim < maxEstim) {
		double sum;
		unsigned long m;
		m = (minEstim + maxEstim) / 2;
		sum = 0;
		for (i = 0; i < n; ++i)
			sum += pow(growthRates[i], m);
		if (sum >= 1000000000.0) {
			maxEstim = m;
		} else if (sum < 1000000000) {
			minEstim = m + 1;
		}
	}

	return minEstim;
}












// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom, but they are otherwise not editable!
void printInteger(int n) {
  printf("[%d]", n);
}

int test_case_number = 1;

void check(int expected, int output) {
  int result = (expected == output);
  const char* rightTick = u8"\u2713";
  const char* wrongTick = u8"\u2717";
  if (result) {
    printf("%s Test #%d\n", rightTick, test_case_number);
  }
  else {
    printf("%s Test #%d: Expected ", wrongTick, test_case_number);
    printInteger(expected); 
    printf(" Your output: ");
    printInteger(output);
    printf("\n");
  }
  test_case_number++;
}

int main() {
  int n_1 = 3;
  float test_1[] = {1.1, 1.2, 1.3};
  int expected_1 = 79;
  int output_1 = getBillionUsersDay(test_1, n_1);
  check(expected_1, output_1);

  int n_2 = 2;
  float test_2[] = {1.01, 1.02};
  int expected_2 = 1047;
  int output_2 = getBillionUsersDay(test_2, n_2);
  check(expected_2, output_2);

  // Add your own test cases here
  
}
