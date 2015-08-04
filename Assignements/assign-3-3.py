inp = raw_input("Enter float number between 0.0 and 1.0: ")
num = float(inp)
if num < 0.0:
    print "Error => The number must be greater or equal than 0.0"
elif num < 0.6:
    print "F"
elif num < 0.7:
    print "D"
elif num < 0.8:
    print "C"
elif num < 0.9:
    print "B"
elif num <= 1.0:
    print "A"
else:
    print "Error => The number must be less than or equal than 1.0"