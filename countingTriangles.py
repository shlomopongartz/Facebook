import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def ident(s, t):
    if s[0] != t[0]:
        return False
    if s[1] != t[1]:
        return False
    if s[2] != t[2]:
        return False
    return True

def countDistinctTriangles(arr):
    # Write your code here
    ll = len(arr)
    if ll <= 1:
        return ll

    # Change to canonicl form
    cann = [None] * ll
    for ind, t in enumerate(arr):
       minind = 0
       maxind = 0
       minval = t[0]
       maxval = t[0]
       for i in [1,2]:
           if t[i] < minval:
               minind = i
               minval = t[i]
           elif t[i] >= maxval:
               maxind = i
               maxval = t[i]
       cann[ind] = (minval, t[3 - minind - maxind], maxval)

    count = 0
    last = (0, 0, 0)
    for t in cann:
        if ident(last, t):
            continue
        count += 1
        last = t

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
  arr_1 = [(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]
  expected_1 = 3
  output_1 = countDistinctTriangles(arr_1)
  check(expected_1, output_1)

  arr_2 = [(3, 4, 5), (8, 8, 9), (7, 7, 7)]
  expected_2 = 3
  output_2 = countDistinctTriangles(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  arr_3 = [(2, 2, 3), (3, 2, 2), (2, 5, 6)]
  expected_3 = 2
  output_3 = countDistinctTriangles(arr_3)
  check(expected_3, output_3)

  arr_4 = [(8, 4, 6), (100, 101, 102), (84, 93, 173)]
  expected_4 = 3
  output_4 = countDistinctTriangles(arr_4)
  check(expected_4, output_4)
