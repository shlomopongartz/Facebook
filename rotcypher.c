#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static char codebook[0x100];

char* rotationalCipher(char input[], int rotationFactor) {
  // Write your code here
  int i;
  int len;
  char *res;
  char *p;
  char *q;
 
  len = strlen(input);
  if (!len)
	return NULL;

  res = malloc(len + 1);
  if (!res) {
	  perror("malloc");
	  return NULL;
  }
  
  for (i = 0; i < sizeof(codebook)/sizeof(codebook[0]); ++i)
	codebook[i] = i;

  for (i = 'A'; i <= 'Z'; ++i)
	codebook[i] = 'A' + (i - 'A' + rotationFactor) % 26;

  for (i = 'a'; i <= 'z'; ++i)
	codebook[i] = 'a' + (i - 'a' + rotationFactor) % 26;

  for (i = '0'; i <= '9'; ++i)
	codebook[i] = '0' + (i - '0' + rotationFactor) % 10;

  p = input;
  q = res;
 
  while (*p) {
	  *q++ = codebook[*p++];
  }
  
  res[len] = '\0';
 
  return res;
}

int main()
{
	{
		char *input = "Zebra-493?";
		int rotationFactor = 3;
		char* output = "Cheud-726?";
		char *res = rotationalCipher(input, rotationFactor);
		printf("%s\n%s\n\n", output, res);
	}
	{
		char *input = "abcdefghijklmNOPQRSTUVWXYZ0123456789";
		int rotationFactor = 39;
		char * output = "nopqrstuvwxyzABCDEFGHIJKLM9012345678";
		char *res = rotationalCipher(input, rotationFactor);
		printf("%s\n%s\n\n", output, res);
	}
}
