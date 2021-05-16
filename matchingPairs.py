import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
    # Write your code here
    ll = len(s)
    if len == 0:
        return 0

    candX = [False] * 0x100
    candY = [False] * 0x100
    matching = [False] * ll

    match = 0
    for x, y, ind in zip(s,t, range(ll)):
        if x == y:
            match += 1
            matching[ind] = True
        else:
            candX[ord(x)] = True
            candY[ord(y)] = True

    #Strings match any swap will decrease by 2
    if match == ll:
        return match - 2

    # A swap may decrease one match unless the unmatched char is
    # a duplicate of a matched one.
    if match == ll - 1:
        for x, ind in eumerate(s):
            if matching[ind] and candX[ord(x)]:
                return match
        return match - 1

    # Assume null char is not considerd
    # We need two cadidate to s
    cand = 0
    for i in range(1, 0x100):
        if candX[i] and candY[i]:
            if cand != 0:
                #Already have one candidate
               return match + 2
            cand = i

    return match







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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  s_3, t_3 = "mno", "mno"
  expected_3 = 1
  output_3 = matching_pairs(s_3, t_3)
  check(expected_3, output_3)
