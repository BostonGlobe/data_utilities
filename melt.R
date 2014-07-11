#! /usr/local/bin/Rscript --vanilla --default-packages=reshape,optparse

# load libraries
suppressPackageStartupMessages(library(argparse))
suppressPackageStartupMessages(library(reshape))

# setup parser
parser <- ArgumentParser()
parser$add_argument('--ids')
parser$add_argument('--columns')
args <- parser$parse_args()

# read data from stdin
d <- read.csv(file("stdin"), strip.white=TRUE)

# melt data
d <- melt(d, id=unlist(strsplit(args$ids, split=',')))

# rename data
names(d) <- unlist(strsplit(args$columns, split=','))

# write data to stdout
write.csv(d, stdout(), row.names=FALSE)