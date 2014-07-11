import pandas as pd
import sys
import datetime
import calendar
import argparse

parser = argparse.ArgumentParser(description='Parse date column to unix.')
parser.add_argument('--column', help='name of date column')
parser.add_argument('--format', help='format of date values - see https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior')
args = parser.parse_args()

# read csv from stdin into a dataframe
df = pd.read_csv(sys.stdin, low_memory=False)

def date_to_unix(d):
	return calendar.timegm(datetime.datetime.strptime(d, args.format).utctimetuple())

df[args.column] = df[args.column].map(date_to_unix)

# output dataframe to stdout
df.to_csv(sys.stdout, index=False)
