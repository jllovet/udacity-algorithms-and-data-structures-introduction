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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# For reference:
# The text data (`text.csv`) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
# The call data (`call.csv`) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

def get_set_of_numbers_in_text_records():
    """Returns a set of the phone numbers in text records

    Runtime complexity = O(n) to iterate over the list of text records,
    since adding items to the accumulator set is O(1) for each item and can
    thus be disregarded.
    """
    texters = set()
    for t in texts:
        texters.add(t[0]) # add number that sent text
        texters.add(t[1]) # add number that received text
    return texters

def identify_telemarketers():
    """Returns a sorted list of possible telemarketers from text and call records
    
    Algorithmic complexity = Amortized O(n^2) for worst case, with θ(n log n) for
    average case
    
    Sorting the list of possible telemarketers takes O(n log n) in the worst case.
    The single pass through the texts and calls records each take O(n). The basic
    set operations (e in set, add e to set) that the implementation uses each take
    O(n) in the worst case, with θ(1) in the average case. Since these occur nested
    inside a loop, in the worst case, this produces an amortized O(n^2). The set
    difference takes O(n) in the worst case. Consequently, since all of the other
    orders are lower than O(n^2) in the context of approximations of runtime
    complexity, the runtime complexity reduces to O(n^2).
    """
    texters = get_set_of_numbers_in_text_records()
    numbers_called = set()
    possible_telemarketers = set()
    for c in calls:
        numbers_called.add(c[1])
        # check for any activity suggesting number is not telemarketer
        if c[0] not in texters:
            possible_telemarketers.add(c[0])
    possible_telemarketers = possible_telemarketers - numbers_called # set difference
    return sorted(possible_telemarketers)


"""
Algorithmic complexity = Amortized O(n^2) for worst case, with θ(n log n) for
average case

Sorting the list of possible telemarketers takes O(n log n) in the worst case.
The single pass through the texts and calls records each take O(n). The basic
set operations (e in set, add e to set) that the implementation uses each take
O(n) in the worst case, with θ(1) in the average case. Since these occur nested
inside a loop, in the worst case, this produces an amortized O(n^2). The set
difference takes O(n) in the worst case. Consequently, since all of the other
orders are lower than O(n^2) in the context of approximations of runtime
complexity, the runtime complexity reduces to O(n^2).

The pass through the sorted list to print them takes O(n), but for the entire
solution this does not change the runtime complexity, in light of the
considerations above.
"""
possible_telemarketers = identify_telemarketers()

print("These numbers could be telemarketers: ")

for t in possible_telemarketers:
    print(t)
