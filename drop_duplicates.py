import pandas as pd
import argparse
import sys

# setup argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--column', help='the column to remove duplicates by')	
args = parser.parse_args()

# make column argument required
if args.column is None:
	print '--column option is required'
	sys.exit(0)

# read csv from stdin into a dataframe
df = pd.read_csv(sys.stdin)

# create a second dataframe without duplicates. take last duplicate
df2 = df.drop_duplicates(cols=args.column, take_last=True)

# output second dataframe to stdout
df2.to_csv(sys.stdout, index=False)
