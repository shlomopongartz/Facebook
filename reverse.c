#include <stdio.h>
#include <stdlib.h>
// Add any extra import statements you may need here


struct Node {
	int data;
	struct Node *next;
};

struct Node* getNode(int x) {
	struct Node *node = (struct Node*)malloc(sizeof(struct Node*));
	node -> data = x;
	node -> next = NULL;
	return node;
}

// Add any helper functions you may need here


struct Node* reverse(struct Node *head) {
	// Write your code here
	struct Node prehead;
	struct Node *p;
	struct Node *q;
	struct Node *b4;
	struct Node *end;

	prehead.next = head;
	p = head;
	q = &prehead;
	while (p) {
		if (p->data & 1) {
			/* Odd */
			q = p;
			p = p->next;
			continue;
		}
		/* Even */
		b4 = q;
		end = p;
		q = p;
		p = p->next;
		while (p) {
			struct Node *n;
			if (p->data & 1)
				break;
			n = p->next;
			p->next = q;
			q = p;
			p = n;
		}
		b4->next = q;
		end->next = p;
	}
	return prehead.next;
}












// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom, but they are otherwise not editable!
void printLinkedList(struct Node *head) {
  printf("[");
  while (head != NULL) {
    printf("%d", head -> data);
    head = head -> next;
    if (head != NULL)
      printf(" ");
  }
  printf("]");
}

int test_case_number = 1;

void check(struct Node *expectedHead, struct Node *outputHead) {
  int result = 1;
  struct Node *tempExpectedHead = expectedHead;
  struct Node *tempOutputHead = outputHead;
  while (expectedHead != NULL && outputHead != NULL) {
    result &= (expectedHead -> data == outputHead -> data);
    expectedHead = expectedHead -> next;
    outputHead = outputHead -> next;
  }
  if (!(expectedHead == NULL && outputHead == NULL)) result = 0;

  const char* rightTick = u8"\u2713";
  const char* wrongTick = u8"\u2717";
  if (result) {
    printf("%s Test #%d\n", rightTick, test_case_number);
  } else {
    printf("%s Test #%d: Expected ", wrongTick, test_case_number);
    printLinkedList(tempExpectedHead); 
    printf(" Your output: ");
    printLinkedList(tempOutputHead);
    printf("\n");
  }

  test_case_number++;
}

struct Node* createLinkedList(int arr[], int n) {
  struct Node *head = NULL;
  struct Node *tempHead = head;
  int v;
  for (int i = 0; i < n; i++) {
    v = arr[i];
    if (head == NULL) {
      head = getNode(v);
      tempHead = head;
    } else {
      head -> next = getNode(v);
      head = head -> next;
    }
  }
  return tempHead;
}

int main() {

  int arr_1[] = {1, 2, 8, 9, 12, 16};
  int expected1[] = {1, 8, 2, 9, 16, 12};
  struct Node *head_1 = createLinkedList(arr_1, 6);
  struct Node *expected_1 = createLinkedList(expected1, 6);
  struct Node *output_1 = reverse(head_1);
  check(expected_1, output_1);

  int arr_2[] = {2, 18, 24, 3, 5, 7, 9, 6, 12};
  int expected2[] = {24, 18, 2, 3, 5, 7, 9, 12, 6};
  struct Node *head_2 = createLinkedList(arr_2, 9);
  struct Node *expected_2 = createLinkedList(expected2, 9);
  struct Node *output_2 = reverse(head_2);
  check(expected_2, output_2);

  // Add your own test cases here
  
}
