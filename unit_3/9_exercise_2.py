import pylab

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

diffTemps = [h - l for h, l in zip(high, low)]
pylab.plot(range(1,32), diffTemps)
