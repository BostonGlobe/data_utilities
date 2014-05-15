import pandas as pd
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--csv', help='the csv file to process, otherwise reads from stdin')
parser.add_argument('--column', help='the column to remove duplicates by')	
args = parser.parse_args()

if args.column is None:
	print '--column option is required'
	sys.exit(0)

if args.csv is None:
	df = pd.read_csv(sys.stdin)
else:
	df = pd.read_csv(args.csv)

df2=df.drop_duplicates(cols=args.column, take_last=True)
df2.to_csv(sys.stdout, index=False)
