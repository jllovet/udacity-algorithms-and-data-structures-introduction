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

# This approach keeps a dictionary of running totals of call times per number
# and a running tally of the number that has spent the longest on the phone so far.
# Since it keeps running score as it iteratesover the list of calls, only a single
# pass is needed over the list, and it produces a solution in linear time.

call_times = dict()

# Initialize to first calling number encountered
number_on_phone_longest = calls[0][0]

# Finds solution in single pass over list. Linear time!
for c in calls:
    # Handle calling telephone number
    if call_times.get(c[0]) is not None:
        call_times[c[0]] += int(c[3]) # Add duration of call to entry for number
    else:
        call_times[c[0]] = int(c[3]) # Add number to dict if not present with duration of call
    
    # Compare to number listed as being on the longest and switch if needed
    if call_times[c[0]] > call_times.get(number_on_phone_longest):
        number_on_phone_longest = c[0]
    
    # Handle receiving telephone number
    if call_times.get(c[1]) is not None:
        call_times[c[1]] += int(c[3]) # Add duration of call to entry for number
    else:
        call_times[c[1]] = int(c[3]) # Add number to dict if not present with duration of call
    
    # Compare to number listed as being on the longest and switch if needed
    if call_times[c[1]] > call_times.get(number_on_phone_longest):
        number_on_phone_longest = c[1]

print(f"{number_on_phone_longest} spent the longest time, {call_times.get(number_on_phone_longest)} seconds, on the phone during September 2016.")
