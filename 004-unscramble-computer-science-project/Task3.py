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
    """Returns boolean indicating whether number is from Bangalore

    Runtime complexity = O(1)
    """
    if len(n) >= len("(080)"):
        return n[:5] == "(080)"
    else:
        return False

def is_mobile_number(n):
    """Returns boolean indicating whether the number is for a mobile phone

    Runtime complexity = O(n), where n is the length of string n
    """
    return " " in n and n[0] in ["7", "8", "9"] and len(n) >= 4

def is_telemarketer_number(n):
    """Returns boolean indicating whether number is from a telemarketer

    Runtime complexity = O(1)
    """
    if len(n) >= len("140"):
        return n[:3] == "140"
    else:
        return False

def is_fixed_line_number(n):
    """Returns boolean indicating whether number is from a fixed line

    Runtime complexity = O(n), where n is the length of string n
    """
    return "(" in n and ")" in n

def get_area_code(n):
    """Returns string for area code of phone number

    Runtime complexity = O(n), where n is the length of string n
    """
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
        """Returns filtered list of str of called phone numbers for calls in area code

        Note: this does not return a set, but rather a filtered list of the call history
        from the area code
        
        Complexity = O(n), where n is the num of elements in self.called_number_history
        Using this method is not the algorithmically optimal option, but having an
        additional pass through this helper function allows the solution
        to be more general than explicitly pre-computing the single solution for
        Bangalore would be. However, that said, it only adds a single additional
        pass that operates in O(n), which does not change the order of the runtime
        complexity of the entire solution.
        """
        h = []
        for number in self.called_number_history:
            if get_area_code(number) == code:
                h.append(number)
        return h

def aggregate_call_logs_by_area_code():
    """Returns a dict of AreaCode to summarize call log information

    Algorithmic complexity = O(n^4) for worst case, with θ(n) or "amortized O(n)" 
    for average case
    
    Iterating over the list of calls has algorithmic complexity of O(n).

    The O(n^4) time in the worst case comes from the worst-case time for dict
    and set lookups and updates that are performed for each of the steps while
    iterating over the list of calls. However, the hash function used by the dict
    and set would have to be very bad for each of them to require O(n) time and
    make the runtime O(n^4) for the entire function. The solution is effectively
    linear, presuming that the hash function is effective (which is a safe
    assumption here).

    Using this structure makes the solution generalizable for metrics against
    other area codes.
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
    """Satisfies requirements of Part A

    Runtime complexity = O(n log n) + O(n) to use the built-in sorted method and
    iterate over the list of area codes to print them, where n is the number of
    elements in the set codes_called, which contains the area codes that have been
    called from Bangalore in this case.
    """
    codes = calls_summary.get("(080)").codes_called
    print("The numbers called by people in Bangalore have codes:")
    for n in sorted(codes):
        print(n)

def get_percentage_of_calls_within_bangalore(calls_summary):
    """Satisfies requirements of Part B

    Runtime complexity = O(n) to execute the method get_history_of_numbers_called_in_area_code.
    Otherwise, the operations can all be executed in O(1).
    """
    area_code = "(080)"
    b = calls_summary.get(area_code)
    num_calls_in_same_area_code = len(b.get_history_of_numbers_called_in_area_code(area_code))
    num_all_calls_from_area_code = len(b.called_number_history)
    percentage = round(num_calls_in_same_area_code / num_all_calls_from_area_code * 100, 2)
    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
Overall solution complexity is O(n) + O(m log m) + O(p), where n is the number
of records in the original call logs, where m is the number of area codes
called from Bangalore, and where p is the number of calls made from the
Bangalore area code. However, since in the context of approximating runtime
complexity O(n) is an order lower than O(n log n), the additional passes
described can be subsumed under the time O(n log n) for the complexity of the
entire solution.
"""
calls_summary = aggregate_call_logs_by_area_code()
get_area_codes_called_from_bangalore(calls_summary)
get_percentage_of_calls_within_bangalore(calls_summary)
