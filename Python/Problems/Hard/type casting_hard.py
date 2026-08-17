# Q32 [Hard]   Parse a CSV string '1,2.5,hello,True,None' into Python-typed values automatically.

# Q60. Write a function that takes a mixed list like:
#      [1, '2', 3.5, True, '4.2', False, 'seven', None]
#      and returns a dict:
#      {
#        'integers':   [list of ints, excluding bools],
#        'floats':     [list of floats],
#        'booleans':   [list of bools],
#        'strings':    [list of valid numeric strings converted to float],
#        'unparseable':[items that couldn't be converted to any number]
#      }