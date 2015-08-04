name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
EmailsFrom = dict()

for line in handle:
    words = line.split()
    if len(words) > 0 and words[0] == "From":
        EmailsFrom[words[1]] = EmailsFrom.get(words[1],0)+1

maxFromCnt = 0
maxFromEmail = ''
for email in EmailsFrom :
	if EmailsFrom[email] > maxFromCnt :
		maxFromCnt = EmailsFrom[email]
		maxFromEmail = email

print maxFromEmail, maxFromCnt