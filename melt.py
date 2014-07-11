import pandas as pd
from pandas.core.reshape import melt
import sys
import argparse

# setup argument parsing
parser = argparse.ArgumentParser(description='Melt data.')
parser.add_argument('--ids', help='comma-separated list of column names', nargs='+')
args = parser.parse_args()

# read csv from stdin into a dataframe
df = pd.read_csv(sys.stdin, low_memory=False)

df = melt(df, id_vars=args.ids)

# output dataframe to stdout
df.to_csv(sys.stdout, index=False)
