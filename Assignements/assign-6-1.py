text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(":")
numstr = text[pos+1:].strip()
res = float(numstr)
print res