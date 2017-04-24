import collections
from collections import Counter
import csv
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


file = open('results_svm3.txt','r')
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

dict_ = {}
i = 0
for x in sorted(d.keys()):
	dict_[x] = i
	i += 1


# plotting confusion matrix
all_classes = sorted(unique_set)
l = len(all_classes)
conf_arr = [[0 for x in range(l)] for y in range(l)]
for key in all_classes:
	results[key].sort(key=lambda x: x[0])
	for i in range(len(results[key])):
		x = dict_[key]
		y = dict_[results[key][i][0]]
		conf_arr[x][y] = results[key][i][1]

'''fl = open('filename.csv', 'w')

writer = csv.writer(fl)
writer.writerow(all_classes) #if needed
for values in conf_arr:
    writer.writerow(values)

fl.close()'''

df = pd.DataFrame(conf_arr,columns=all_classes)

data = [go.Heatmap( z=df.values.tolist(), colorscale='Viridis')]

plot(data, filename='pandas-heatmap')

'''norm_conf = []
for i in conf_arr:
    a = 0
    tmp_arr = []
    a = sum(i, 0)
    for j in i:
        tmp_arr.append(float(j)/float(a))
    norm_conf.append(tmp_arr)

fig = plt.figure()
plt.clf()
ax = fig.add_subplot(111)
ax.set_aspect(1)
res = ax.imshow(np.array(norm_conf), cmap=plt.cm.jet, 
                interpolation='nearest')

width, height = 101,101

for x in xrange(width):
    for y in xrange(height):
        ax.annotate(str(conf_arr[x][y]), xy=(y, x), 
                    horizontalalignment='center',
                    verticalalignment='center')

cb = fig.colorbar(res)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
plt.xticks(range(width), alphabet[:width])
plt.yticks(range(height), alphabet[:height])
plt.show()'''