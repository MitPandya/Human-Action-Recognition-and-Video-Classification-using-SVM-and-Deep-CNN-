import collections
from collections import Counter

file = open('results_svm.txt','r')
d = {}
results = {}
for l in file:
	l = l.strip()
	l = l.split('  ')
	if l[0] in d.keys():
		d[l[0]].append(l[1])
	else:
		d[l[0]] = []
		d[l[0]].append(l[1])

print d.keys()
file.close()
unique_set = d.keys()
for x in unique_set:
	print x
	temp = []
	temp = d[x]
	res = Counter(temp)
	results[x] = res
	print "True : ",x
	print "Results: "
	print res
for key in results.keys():
	temp = results[key]
	temp = sorted(temp.items(), key=lambda x: x[1], reverse = True)
	results[key] = temp
tp = 0
tn = 0
for key in results.keys():
	if results[key][0][0] == key :
		tp += 1
	else:
		tn += 1

print "True predictions : ", tp
print "False predictions : ", tn
print "Accuracy : ",(tp * 100/(tp + tn)),"%"
