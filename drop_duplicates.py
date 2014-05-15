import pandas as pd
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--column', help='the column to remove duplicates by')	
args = parser.parse_args()

if args.column is None:
	print '--column option is required'
	sys.exit(0)

df = pd.read_csv(sys.stdin)
df2 = df.drop_duplicates(cols=args.column, take_last=True)
df2.to_csv(sys.stdout, index=False)
