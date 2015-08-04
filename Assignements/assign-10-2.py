name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

EmailsHours = dict()

for line in handle:
    words = line.split()
    if len(words) > 0 and words[0] == "From":
        times = words[5].split(':')
        EmailsHours[times[0]] = EmailsHours.get(times[0],0)+1

HoursList = EmailsHours.keys()
HoursList.sort()

for i in HoursList:
	print i, EmailsHours[i]