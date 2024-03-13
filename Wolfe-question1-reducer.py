#!/usr/bin/env python
# this line means that the script is executable,
# it calls the language interpreter to run the code inside the script
# and is the guide to find 'python'


# import the module for reading and writing data
import sys

# initialize the variables, chosen and word with None and chosen_count with 0
(chosen, chosen_count, word) = (None, 0, None)

# values produced by the mapper are read by STDIN (standard input) and do
# the following for each input line (loop)
for line in sys.stdin:
#     remove leading and trailing whitespace
    line = line.strip()

#     line is split by tab, that was used in the printing of the result by
#     the mapper, and assigned to key and value respectively
    (word, count) = line.split('\t',1)

#     Need to check if count is str or int
    try:
        count = int(count)
    except ValueError:
        continue

#     itterate through the inputs.
    if chosen == word:
        chosen_count += count
    else:
        if chosen:
            #output resuts
            print('%s\t%s' % (chosen, chosen_count))
        chosen = word
        chosen_count = count

# last variable catch
if chosen == word:
    print('%s\t%s' % (chosen, chosen_count))  