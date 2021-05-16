#include <stdio.h>
// Add any extra import statements you may need here
#include <stdlib.h>

// Add any helper functions you may need here


int* findMaxProduct(int arr[], int n, int *output_size) {
  // Set output_size for test cases to run correctly
  // Write your code here  
  int max[3];
  int *out;
  int max_ind, mid_ind, min_ind;
  int i;

  if (!n) {
	  *output_size = 0;
	  return NULL;
  }

  out = malloc(n * sizeof(int));
  if (!out) {
	  perror("malloc");
	  *output_size = 0;
	  return NULL;
  }

  *output_size = n;

  out[0] = -1;
  if (n < 2)
	  return out;

  out[1] = -1;
  if (n < 3)
	  return out;

  out[2] = arr[0] * arr[1] * arr[2];
  
  max_ind = 0;
  min_ind = 0;
  for (i = 1; i < 3; ++i) {
      if (arr[i] < arr[min_ind])
          min_ind = i;
      else if (arr[i] > arr[max_ind])
	      max_ind = i;
  }
  mid_ind = 3 - max_ind - min_ind;
  max[0] = arr[min_ind];
  max[1] = arr[mid_ind];
  max[2] = arr[max_ind];

  /* start output */

  for (i = 3; i < n; ++i) {
	  if (arr[i] > max[2]) {
		  max[0] = max[1];
		  max[1] = max[2];
		  max[2] = arr[i];
	  } else if (arr[i] > max[1]) {
		  max[0] = max[1];
		  max[1] = arr[i];
	  } else if (arr[i] > max[0]) {
		  max[0] = arr[i];
	  }
	  out[i] = max[0] * max[1] * max[2];
  }

  return out;
}












// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom, but they are otherwise not editable!
void printIntegerArray(int array[], int size) {
  printf("[");
  for (int i = 0; i < size; i++) {
    if (i != 0) {
      printf(", ");
    }
    printf("%d", array[i]);
  }
  printf("]");
}

int test_case_number = 1;

void check(int expected[], int output[], int size, int out_size) {
  int expected_size = size;
  int output_size = out_size;
  int result = 1;
  if (expected_size != output_size) {
    result = 0;
  }
  else {
    for (int i = 0; i < size; i++) {
      result &= (output[i] == expected[i]);
    }
  }
  const char* rightTick = u8"\u2713";
  const char* wrongTick = u8"\u2717";
  if (result) {
    printf("%s Test #%d\n", rightTick, test_case_number);
  }
  else {
    printf("%s Test #%d: Expected ", wrongTick, test_case_number);
    printIntegerArray(expected, size); 
    printf(" Your output: ");
    printIntegerArray(output, output_size);
    printf("\n");
  }
  test_case_number++;
}

int main() {
  // Testcase 1
  int n_1 = 5;
  int arr_1[] = {1, 2, 3, 4, 5};
  int expected_1[] = {-1, -1, 6, 24, 60};
  int output_1_size;
  int *output_1 = findMaxProduct(arr_1, n_1, &output_1_size);
  check(expected_1, output_1, n_1, output_1_size);
  
  // Testcase 2
  int n_2 = 6;
  int arr_2[] = {2, 4, 7, 1, 5, 3};
  int expected_2[] = {-1, -1, 56, 56, 140, 140};
  int output_2_size;
  int *output_2 = findMaxProduct(arr_2, n_2, &output_2_size);
  check(expected_2, output_2, n_2, output_2_size);

  // Add your own test cases here
  
}
