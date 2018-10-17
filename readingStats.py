from glob import glob
import pandas as pd
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import os

files = glob('pacificArctic\\*.md')

date = []
keywords = []
for file in files:
    with  open(file,'r') as f:
        date.append(f.read().split('\n')[0])
        f.seek(0)
        keywords.append(f.read().split('\n')[6].split(', '))
readDates = pd.DataFrame({'Date': pd.to_datetime(date), 'Keys':keywords})
unique = set(x for l in readDates.Keys for x in l)

topKeys = ''
numPapers = len(files)
numDays = (max(readDates.Date)-min(readDates.Date)).days+1
print('Total papers read: '+ str(len(files)) + '\n '+
     'Average per day: ' + str(numPapers/numDays) + '\n '+
     'Most common keywords: ' + str(Counter(list(itertools.chain.from_iterable(readDates.Keys.values))).most_common(5)))

readDates.groupby('Date').size().plot(x = 'Date', y='Number Papers', figsize = (10,1.5))
plt.savefig('readingTimeline.jpg')

# Now lets populate the readme file with the paper list
readme = 'README.md'
searchfile = open(readme, "r")
allText = ''
for line in searchfile:
    allText = allText+line
searchfile.close()
with open(readme,'a') as myFile:
    for file in files:
        f = open(file,'r')
        title = f.read().split('\n')[4]
        f.seek(0)
        sig = f.read().split('\n')[12]
        if os.path.basename(file)[:-3] not in allText:
            myFile.write('* ['+os.path.basename(file)[:-3]+' - '+
            title+'](https://github.com/leviner/ReadingList/tree/master/pacificArctic/'+os.path.basename(file)+') \n' +
            '     * '+ sig + ' \n')
