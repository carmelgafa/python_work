import csv
import io
import urllib.request

url = "https://raw.github.com/datasets/gdp/master/data/gdp.csv"
url='https://people.sc.fsu.edu/~jburkardt/data/csv/snakes_count_1000.csv'
webpage = urllib.request.urlopen(url)
datareader = csv.reader(io.TextIOWrapper(webpage))

data = list(datareader)

print(data)
    