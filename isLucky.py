"""
Ticket numbers usually consist of an even number of digits. A ticket number is
 considered lucky if the sum of the first half of the digits is equal to
  the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with
an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

n = 1230


def is_lucky(num):
    num_list = list(str(num))
    half = len(num_list) // 2
    first_half = num_list[:half]
    second_half = num_list[half:]
    return sum(int(num) for num in second_half) == sum(int(num) for num in
                                                       first_half)


print(is_lucky(n))
