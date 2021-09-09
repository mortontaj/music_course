import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    Integer_array = []
    for i in grades:
        if i <= 38 or i % 5 < 3:
            Integer_array.append(i)
        else:
            remaining_b4_nxt_multiple_of_5 = i % 5
            compliment_to_remaining = 5 - remaining_b4_nxt_multiple_of_5
            rounded_up = i + compliment_to_remaining
            Integer_array.append(rounded_up)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

