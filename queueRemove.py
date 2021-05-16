import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findPositions(arr, x):
  # Write your code here

    ll = len(arr)
    queue = [[y,i] for i,y in enumerate(arr,1)]
    out = []
    for i in range(x):
        topop = x if x < ll else ll
        maxelem = [-1, -1]
        poped = []
        ind = 0
        for j in range(topop):
           t = queue.pop(0)
           if t[0] > maxelem[0]:
               maxelem = t
               ind = j
           poped.append(t)
        out.append(maxelem[1]) 
        for j in range(ind):
            vv = poped[j][0] = 0 if poped[j][0] == 0 else poped[j][0] - 1
            queue.append([vv, poped[j][1]])
        for j in range(ind + 1, len(poped)):
            vv = poped[j][0] = 0 if poped[j][0] == 0 else poped[j][0] - 1
            queue.append([vv, poped[j][1]])
        ll -= 1

    return out







# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 6
  x_1 = 5
  arr_1 = [1, 2, 2, 3, 4, 5]
  expected_1 = [5, 6, 4, 1, 2]
  output_1 = findPositions(arr_1, x_1)
  check(expected_1, output_1)

  n_2 = 13
  x_2 = 4
  arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  expected_2 = [2, 5, 10, 13]
  output_2 = findPositions(arr_2, x_2)
  check(expected_2, output_2)

  # Add your own test cases here
