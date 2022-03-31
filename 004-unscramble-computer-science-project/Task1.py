"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# For reference:
# The text data (`text.csv`) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
# The call data (`call.csv`) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

"""
Algorithmic complexity = O(n^2)

This implementation iterates over each of the lists one time and
adds each new phone number to the set of numbers as it proceeds.
Because the python built-in set has average-case retrieval of elements
of θ(1) and O(n) in the worst case, as we iterate over the lists of
texts and calls, getting the unique set of numbers can be done on
average in O((t+c)^2), where t is the number of text records and c is the
number of call records. This reduces to O(n^2) for worst-case performance,
with average performance being θ(n).
"""

numbers = set()

for t in texts:
    numbers.add(t[0])
    numbers.add(t[1])

for c in calls:
    numbers.add(c[0])
    numbers.add(c[1])

print(f"There are {len(numbers)} different telephone numbers in the records.")