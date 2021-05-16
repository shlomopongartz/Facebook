#include <stdio.h>
// Add any extra import statements you may need here
#include <stdlib.h>
#include <string.h>


// Add any helper functions you may need here

void findEncryptedWord2(char s[], char out[], int n) {
  // Write your code here
    if (n <= 0)
		return;

    if (n == 1) {
		out[0] = s[0];
		return;
	}

    int mid = (n - 1) / 2;

    out[0] = s[mid];
    findEncryptedWord2(&s[0], &out[1], mid);
    findEncryptedWord2(&s[mid  + 1], &out[mid + 1], n - mid - 1); 
}


char* findEncryptedWord(char s[], int n) {
  // Write your code here
    int len;
    char *out;

	if (!n)
		return NULL;
		
	out = malloc(n + 1);
	if (!out) {
		perror("malloc");
		return NULL;
	}
	
	findEncryptedWord2(s, out, n);
	
	out[n] = '\0';
	return out;
}












// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom, but they are otherwise not editable!

void printCharArray(char arr[]) {
  printf("[\"");
  for (int i = 0; arr[i] != '\0'; i++) {
    printf("%c", arr[i]);
  }
  printf("\"]");
}

int test_case_number = 1;

void check(char expected[], char output[]) {
  int result = !strcmp(expected, output);
  const char* rightTick = u8"\u2713";
  const char* wrongTick = u8"\u2717";
  if (result) {
    printf("%s Test #%d\n", rightTick, test_case_number);
  }
  else {
    printf("%s Test # %d: Expected ", wrongTick, test_case_number);
    printCharArray(expected); 
    printf(" Your output: ");
    printCharArray(output);
    printf("\n");
  }
  test_case_number++;
}

int main() {

  int n_1 = 3;
  char s_1[] = "abc";
  char expected_1[] = "bac";
  char* output_1 = findEncryptedWord(s_1, n_1);
  check(expected_1, output_1);

  int n_2 = 4;
  char s_2[] = "abcd";
  char expected_2[] = "bacd";
  char* output_2 = findEncryptedWord(s_2, n_2);
  check(expected_2, output_2);

  // Add your own test cases here
  
}
