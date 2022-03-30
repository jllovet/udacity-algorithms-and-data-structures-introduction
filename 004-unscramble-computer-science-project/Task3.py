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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# For reference:
# The text data (`text.csv`) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
# The call data (`call.csv`) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

def is_bangalore_number(n):
    return n[:5] == "(080)"

def is_mobile_number(n):
    return " " in n and n[0] in ["7", "8", "9"]

def is_telemarketer_number(n):
    return n[:3] == "140"

def is_fixed_line_number(n):
    return "(" in n and ")" in n

def get_area_code(n):
    if is_bangalore_number(n):
        return "(080)"
    if is_fixed_line_number(n):
        return n[ 0 : n.index(")") + 1 ]
    if is_telemarketer_number(n):
        return "140"
    if is_mobile_number(n):
        return n[:4]

class AreaCode:
    """AreaCode represents a summary of the phone activity from an area code

    Attributes:
        area_code: str of area code
        phone_numbers: set of strings for phone numbers in call logs with area code
        called_number_history: list of strings for phone numbers called from within area code
        codes_called: set of strings for area codes called from area code
    """
    def __init__(self, area_code, phone_numbers, called_number_history, codes_called):
        self.area_code = area_code
        self.phone_numbers = set(phone_numbers)
        self.called_number_history = list(called_number_history)
        self.codes_called = set(codes_called)
    def get_history_of_numbers_called_in_area_code(self, code):
        """Returns a filtered list of str for phone numbers for each call made to the area code provided

        Note: this does not return a set, but rather a filtered list of the call history from the area code
        """
        h = []
        for number in self.called_number_history:
            if get_area_code(number) == code:
                h.append(number)
        return h

def aggregate_call_logs_by_area_code():
    """Returns a dict of AreaCode to summarize call log information
    """
    calls_summary = dict()
    for c in calls:
        calling_number = c[0]
        receiving_number = c[1]
        code_of_caller = get_area_code(c[0])
        code_of_receiver = get_area_code(c[1])
        
        # Construct a new AreaCode if not already in the dictionary
        if calls_summary.get(code_of_caller) is None:
            calls_summary[code_of_caller] = AreaCode(
                area_code=code_of_caller,
                phone_numbers=set([calling_number]),
                codes_called=set([code_of_receiver]),
                called_number_history=list(receiving_number),
            )
        # Update the AreaCode record if it is already in the dictionary
        else:
            calls_summary[code_of_caller].phone_numbers.add(calling_number)
            calls_summary[code_of_caller].codes_called.add(code_of_receiver)
            calls_summary[code_of_caller].called_number_history.append(receiving_number)
    return calls_summary


def get_area_codes_called_from_bangalore(calls_summary):
    codes = calls_summary.get("(080)").codes_called
    print("The numbers called by people in Bangalore have codes:")
    for n in sorted(codes):
        print(n)

def get_percentage_of_calls_within_bangalore(calls_summary):
    area_code = "(080)"
    b = calls_summary.get(area_code)
    num_calls_in_same_area_code = len(b.get_history_of_numbers_called_in_area_code(area_code))
    num_all_calls_from_area_code = len(b.called_number_history)
    percentage = round(num_calls_in_same_area_code / num_all_calls_from_area_code * 100, 2)
    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

calls_summary = aggregate_call_logs_by_area_code()
get_area_codes_called_from_bangalore(calls_summary)
get_percentage_of_calls_within_bangalore(calls_summary)
