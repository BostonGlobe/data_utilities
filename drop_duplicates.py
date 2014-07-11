import pandas as pd
import argparse
import sys

# setup argument parsing
parser = argparse.ArgumentParser(description='Drops duplicates based on a column. Takes the last duplicate row.')
parser.add_argument('--column', help='the column to remove duplicates by')	
args = parser.parse_args()

# make column argument required
if args.column is None:
	print '--column option is required'
	sys.exit(0)

# read csv from stdin into a dataframe
df = pd.read_csv(sys.stdin, low_memory=False)

df = df.drop_duplicates(cols=args.column, take_last=True)

# output second dataframe to stdout
df.to_csv(sys.stdout, index=False)