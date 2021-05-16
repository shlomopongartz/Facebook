import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here
def addToHeaps(num, botq, topq):
    #Note python heapq is min heap
    #So for max heap inverse teh values
    if len(topq) == 0 or num > topq[0]:
        heapq.heappush(topq, num)
    else:
        heapq.heappush(botq, -num)

def rebalance(botq, topq):
    if len(botq) > len(topq):
        larger = botq
        smaller = topq
    else:
        larger = topq
        smaller = botq

    if len(larger) - len(smaller) > 1:
        val = heapq.heappop(larger)
        heapq.heappush(smaller, -val)

def getMediean(botq, topq):
    if len(botq) < len(topq):
        return topq[0]
    elif len(botq) > len(topq):
        return -botq[0]
    else:
        return (topq[0] - botq[0]) // 2 

def findMedian(arr):
    # Write your code here
  
    ll = len(arr)
    if ll == 0:
        return None

    if ll == 1:
        return [1]

    topq = []
    botq = []
    result = [0] * ll

    for i, num in enumerate(arr):
        addToHeaps(num, botq, topq)
        rebalance(botq, topq)
        result[i] = getMediean(botq, topq)


    return result



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
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
