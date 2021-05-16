import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOperations(arr):
    # Write your code here

    ll = len(arr)
    arein = [0] * (ll + 1)
    for i, val in enumerate(arr):
        arein[val] = i

    swaps = 0
    #Don't need to check last number
    for val in range(1, ll):
        # val is from 1..n isin is from 0..n-1
        isin = arein[val]
        tobe = val - 1
        diff = isin + 1 - val
        if diff > 0:
            swaps += 1
            if tobe == 0:
                arr[tobe:isin + 1] = arr[isin::-1]
            else:
                arr[tobe:isin + 1] = arr[isin:tobe - 1: -1]
            #Need to swap arein too.
            isin += 1
            arein[val:isin + 1] = arein[isin + 1 :val - 1: -1]



    return swaps











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
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  # Add your own test cases here
