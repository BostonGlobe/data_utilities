## drop_duplicates

Python script that reads a csv, drops duplicates based on a column, and outputs to stdout. Takes the last duplicate row.

#### dependencies

- [Pandas](http://pandas.pydata.org/)

#### usage

**test.csv**
```csv
name,twitter
john doe,@jooohndoe
john doe,@johndoe
jane dae,@janedae
```

`cat test.csv | python drop_duplicates.py --column name`

**output**
```csv
name,twitter
john doe,@johndoe
jane dae,@janedae
```
