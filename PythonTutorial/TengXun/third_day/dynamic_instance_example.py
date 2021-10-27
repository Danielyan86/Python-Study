
cls = type('A', (object,), {'__doc__': 'class created by type'}) # the seond parameter is tuple, need to add comma
print(cls)
print(cls.__doc__)
