import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
    # Write your code here
    l = len(arr)
    s = sum(arr)
    if s % 2 == 1:
        return False

    #0-1 knapsac with val as total weight values as wights
    # and all values are 1.  
    val = s // 2
    table = [[0 for x in range(val + 1)] for y in range(l + 1)] 
    print("sum is %d val is %d" % (s, val))

    for i, wight in enumerate(arr, 1):
        for w in range(1, val + 1):
            if w < wight:
                #can't add this item
                table[i][w] = table[i - 1][w]
            else:
                #Profit if we take the item
                t = wight + table[i - 1][w - wight]
                if t > table[i - 1][w]:
                    table[i][w] = t
                else:
                    table[i][w] = table[i - 1][w]

    for ll in table:
        print(ll)


    if table[l][val] == val:
        return True
    else:
        print("result %d" % table[l][val]);
        return False










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
