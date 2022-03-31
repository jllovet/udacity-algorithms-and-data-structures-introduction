"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# For reference:
# The text data (`text.csv`) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
# The call data (`call.csv`) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

def find_number_on_phone_longest():

    call_times = dict()

    def process_record(record, phone_number_index, number_on_phone_longest):
        update_call_times_subtotal(record, phone_number_index)
        return update_number_on_phone_longest(record, phone_number_index, number_on_phone_longest)

    def update_call_times_subtotal(record, phone_number_index):
        """Updates the running total call time for a number in the call_times dictionary

        Runtime complexity = O(n) in the worst case for dict lookups and modifications,
        with average time of θ(1).
        """
        if call_times.get(record[phone_number_index]) is None:
            call_times[record[phone_number_index]] = int(record[3]) # Add number to dict if not present with duration of call
        else:
            call_times[record[phone_number_index]] += int(record[3]) # Add duration of call to entry for number

    def update_number_on_phone_longest(record, phone_number_index, number_on_phone_longest):
        """Returns the number that has been on the phone the longest so far

        Args:
            record:
                list of str for a line from the calls records
            phone_number_index:
                int for index of the number to be compared against the number currently listed as
                having the greatest summed call times
                0 for the calling number.
                1 for the receiving number.
            number_on_phone_longest:
                str for current number listed with the greatest summed call times

        Runtime complexity = O(n) in the worst case for dict lookups, with average time
        of θ(1).
        """
        # Compare to number listed as being on the longest and switch if needed
        if call_times[record[phone_number_index]] > call_times.get(number_on_phone_longest):
            number_on_phone_longest = record[phone_number_index]
        return number_on_phone_longest

    # Initialize to first calling number encountered
    number_on_phone_longest = calls[0][0]

    # Finds solution in single pass over list.
    for c in calls:
        # Handle calling telephone number
        number_on_phone_longest = process_record(c, 0, number_on_phone_longest)
        # Handle receiving telephone number
        number_on_phone_longest = process_record(c, 1, number_on_phone_longest)

    print(f"{number_on_phone_longest} spent the longest time, {call_times.get(number_on_phone_longest)} seconds, on the phone during September 2016.")


"""
Algorithmic complexity = O(n^2) for worst case, with θ(n) for average case.
This approach keeps a dictionary of running totals of call times per number
and a running tally of the number that has spent the longest on the phone so far.
Since it keeps running score as it iterates over the list of calls, only a single
pass is needed over the list, and it produces a solution in linear time.

A note on the implementation: to avoid having to allocate additional
memory for the call_times dict in each of the helper functions, it is contained
within the parent scope of those helper functions and is a semi-global variable,
with the caveat that it is still only available within the scope of the function
find_number_on_phone_longest. For this to work, the helper functions are defined
and executed in the scope of find_number_on_phone_longest.
"""

find_number_on_phone_longest()
