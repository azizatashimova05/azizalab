11 import sys

input_data = sys.stdin.read().split()
if input_data:
    n, l, r = map(int, input_data[:3])
    a = list(map(int, input_data[3:3+n]))
    
    # Python uses 0-based indexing; positions l and r are 1-based.
    # We reverse the slice from index l-1 to r.
    a[l-1:r] = reversed(a[l-1:r])
    print(*(a))