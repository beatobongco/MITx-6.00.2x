from collections import namedtuple as nt
import pylab
import numpy

def loadFile():
  inFile = open('julytemps.txt')
  high = []
  low = []
  for line in inFile:
    fields = line.split()
    if len(fields) < 3 or fields[0] in ('Boston', 'Day'):
      continue
    else:
      high.append(int(fields[1]))
      low.append(int(fields[2]))
  return (low, high)

low, high = loadFile()

DataPoint = nt('DataPoint', ['mean', 'std'])

low_data = DataPoint(numpy.mean(low), numpy.std(low))
high_data = DataPoint(numpy.mean(high), numpy.std(high))

print(low_data, high_data)

# We can infer results using the 68-95-99.7 rule
# The yerr is just the std * 1, 2, 3 respectively
# https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule

# Results are only significant if the error bars do not intersect

for multiplier, confidence_interval in ((1, 68), (1.96, 95), (3, 99.7)):
  f = pylab.figure()
  pylab.xticks([0, 1], ['low', 'high'])
  pylab.errorbar([0, 1],
    [low_data.mean, high_data.mean],
    yerr=[low_data.std * multiplier, high_data.std * multiplier],
    fmt='o')
  pylab.title('{0}% confidence interval'.format(confidence_interval))
  f.show()
