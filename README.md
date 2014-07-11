# data_utilities

A (small) collection of data utilities.

## melt.py

Python script that reads a csv and melts by column. Outputs to stdout.

#### dependencies

- [Pandas](http://pandas.pydata.org/)

#### usage

**test.csv**
```csv
fips,town,2013,2014
1,boston,1,2
2,cambridge,5,7
```

`cat test.csv | python melt.py --ids fips town`

**output**
```csv
fips,town,variable,value
1,boston,2013,1
2,cambridge,2013,5
1,boston,2014,2
2,cambridge,2014,7
```

## parse_date_to_unix

Python script that reads a csv and parses date to column to unix. Outputs to stdout.

#### dependencies

- [Pandas](http://pandas.pydata.org/)

#### usage

**test.csv**
```csv
name,birthday
jane dae,01-01-2014
john doe,12-31-2014
```

`cat test.csv | python parse_date_to_unix.py --column birthday --format "%m-%d-%Y"`

**output**
```csv
name,birthday
jane dae,1388534400
john doe,1419984000
```

## drop_duplicates

Python script that reads a csv, drops duplicates based on a column. Takes the last duplicate row. Outputs to stdout.

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

## License

MIT © [The Boston Globe](http://github.com/BostonGlobe)
