
# Print an A4 document as an A6 booklet. 
# After printing, cut paper in half, fold, and insert lower half inside upper half.

# Inputs:
# Number of pages of original document
# folio size - number of sheets of A5 paper that will be bound together

# Output
# Each line contains a sequence of numbers to input into Word as the pages you want to print
# representing each folio

import math

FRONT = 0
BACK = 1
TOP_LEFT = 0
TOP_RIGHT = 1
BOTTOM_LEFT = 2
BOTTOM_RIGHT = 3

def generate_page_order(total_A4_sheets):

    total_a6_pages = total_A4_sheets * 8

    a6_pages = [[[0 for _ in range(4)] for _ in range(2)] for _ in range(total_A4_sheets)]
    
    for sheet_nr in range(0, total_A4_sheets):
        a6_pages[sheet_nr][FRONT][TOP_LEFT] = total_a6_pages - ((sheet_nr) * 2)
        a6_pages[sheet_nr][FRONT][TOP_RIGHT] = 1 + ((sheet_nr) * 2)
        a6_pages[sheet_nr][FRONT][BOTTOM_LEFT] = a6_pages[sheet_nr][FRONT][TOP_LEFT] - (total_A4_sheets *2)
        a6_pages[sheet_nr][FRONT][BOTTOM_RIGHT] = a6_pages[sheet_nr][FRONT][TOP_RIGHT] + (total_A4_sheets *2)
    
        a6_pages[sheet_nr][BACK][TOP_LEFT] = a6_pages[sheet_nr][FRONT][TOP_RIGHT] + 1
        a6_pages[sheet_nr][BACK][TOP_RIGHT] = a6_pages[sheet_nr][FRONT][TOP_LEFT] - 1
        a6_pages[sheet_nr][BACK][BOTTOM_LEFT] = a6_pages[sheet_nr][FRONT][BOTTOM_RIGHT] + 1
        a6_pages[sheet_nr][BACK][BOTTOM_RIGHT] = a6_pages[sheet_nr][FRONT][BOTTOM_LEFT] - 1
    
    return a6_pages


def output(a6_pages, folio_nr):
    # for each additional folio, add folio_nr * folio_size
    offset = folio_nr * A4_pages_per_folio * 8
    output_nrs = []
    for sheet_nr in range(0, len(a6_pages)):
        for sheet_side in range(0, 2):
            for sheet_position in range(0, 4):
                curr_page = min(a6_pages[sheet_nr][sheet_side][sheet_position] + offset, nr_pages) 
                output_nrs.append(str(curr_page)) 
    print(','.join(output_nrs))

def get_integer(message, default):
        try:
            number_as_integer = int(input(message + " [" + str(default) + "]: "))
            return number_as_integer
        except ValueError:
            return default

# Example usage
nr_pages = get_integer("Enter the number of pages", 8)
nr_folios = get_integer("Enter the number of folios to print", 1)
A4_pages_per_folio = math.ceil(nr_pages / (nr_folios * 8))  
print("This will result in printing " + str(A4_pages_per_folio) + " A4 pages per folio, each folio containing " + str(A4_pages_per_folio*8) + " x A6 pages")
a6_pages = generate_page_order(A4_pages_per_folio)
print("Enter the following sequences in the Print dialog, as the pages you want to print, each representing a folio")
for i in range(nr_folios):
    output(a6_pages, i)



