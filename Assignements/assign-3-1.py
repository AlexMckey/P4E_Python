inp = raw_input("Enter Hours:")
hours = float(inp)
inp = raw_input("Enter Rate:")
rate = float(inp)
if hours <= 40 :
    pay = hours * rate
else :
    pay = 40 * rate + (hours - 40) * 1.5 * rate
print pay