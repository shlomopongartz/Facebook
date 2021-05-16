import math
# Add any extra import statements you may need here

# Add any helper functions you may need here
def dounheap(heap, k, N):
    v = heap[k]
    while k <= N // 2:
        j = k + k
        if j < N:
            if heap[j] < heap[j + 1]:
                j += 1
            if v >= heap[j]:
                break
            heap[k] = heap[j]
            k = j
    heap[k] = v

def replace(heap, v, ll):
    heap[1] = v
    dounheap(heap, 1, ll)

def heapify(heap, i):
    v = heap[i]
    heap[0] = 0x7fffffff
    while heap[i // 2] <= v:
        heap[i] = heap[i // 2]
        i = i // 2
    heap[i] = v

def buidheap(heap, ll):
    for i in range(1, len(heap)):
        heapify(heap, i)

def maxCandies(arr, k):
    # Write your code here
    ll = len(arr)
    if ll == 0:
        return 0

    heap = [0] + arr 

    count = 0
    buidheap(heap, ll)

    count = 0
    for i in range(k):
        count += heap[1]
        replace(heap, heap[1] // 2, ll)

    return count









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1, k_1 = 5, 3
  arr_1 = [2, 1, 7, 4, 2]
  expected_1 = 14
  output_1 = maxCandies(arr_1, k_1)
  check(expected_1, output_1)

  n_2, k_2 = 9, 3
  arr_2 = [19, 78, 76, 72, 48, 8, 24, 74, 29]
  expected_2 = 228
  output_2 = maxCandies(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
