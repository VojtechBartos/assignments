# Assigments

This repo contains various Python programming assignment for data engineering role.

## 1. Counter

### Instructions

1. Write a body of a `count_analyses` method of `counter` module , that returns number of possible analyses for given `pandas.DataFrame`. 
2. Finish `py.tests` in `tests/counter/test_counter_analyses`.

### Installation

Run: `pip install -r requirements.txt`

### Test

Run: `py.test tests/counter`


## 2. Graph

### Instructions

1. Create new class `Edge` representing relation between 2 nodes.
2. Create new `Graph` method `add_edge` adding new edge to the graph.
3. Write tests for `add_edge` method.

### Installation

Run: `pip install -r requirements.txt`

### Test

Run: `py.test tests/graph`


## 3. Analysis of Tweets Correlation

### Instructions

In `/tweets/tweets.py` write simple program that:

1. Loads 8,000 Twitter tweets from `/tweets/tweets.json` downloaded from Twitter API.
2. Shapes data into `Pandas.DataFrame` so that:
2.1. `Pandas.DataFrame` columns will contain  tweets' `tag` attribute (i.e. ["#ai", "#analytics", "conference", "acquisition"])
2.2. `Pandas.DataFrame` index will contain tweets' `created_at` binned into 10-minutes buckets (i.e. ["2019-02-11 11:00:00", "2019-02-11 10:50:00"]) sorted in descending order.
2.3. `Pandas.DataFrame` cells will contain `count` of tweets tagged with particular `tag` (column) ar particular `created_at` bin (index).
3. Performs correlation analysis between all pairs of `tags`. Determine and provide reasoning if any correlation between `tags` was observed.

Optional:

1. Extend program to enable custom bin `frequency`. 
2. Write tests.

#### Example:

```
tag                 #acquisition   #ai #analytics #bigdata #conference #meetup   #ml #startup
created_at
2019-02-11 11:00:00          6.0  72.0       10.0     28.0         7.0     4.0  12.0     42.0
2019-02-11 10:50:00          1.0  45.0       12.0     16.0         2.0     NaN   4.0     22.0
2019-02-11 10:40:00          3.0  44.0        6.0     19.0         9.0     4.0   4.0     20.0
2019-02-11 10:30:00          1.0  66.0       11.0     41.0         2.0     NaN   7.0     26.0
2019-02-11 10:20:00          2.0  63.0        8.0     21.0         4.0     3.0   7.0     23.0
2019-02-11 10:10:00          1.0  61.0        7.0     12.0         7.0     NaN   5.0     25.0
2019-02-11 10:00:00          2.0  73.0       13.0     18.0        14.0     NaN   7.0     49.0
2019-02-11 09:50:00          NaN  63.0       12.0     28.0         4.0     1.0  11.0     29.0
2019-02-11 09:40:00          1.0  68.0        5.0     26.0         5.0     1.0   5.0     26.0
2019-02-11 09:30:00          1.0  77.0        9.0     29.0         6.0     1.0   5.0     34.0
2019-02-11 09:20:00          1.0  44.0        3.0     14.0         5.0     5.0   1.0     19.0
2019-02-11 09:10:00          NaN  54.0        6.0     20.0        10.0     4.0   8.0     29.0
2019-02-11 09:00:00          NaN  78.0       11.0     26.0         9.0     2.0   7.0     35.0
2019-02-11 08:50:00          NaN  55.0        9.0     22.0         2.0     6.0   2.0     24.0
2019-02-11 08:40:00          NaN  61.0        8.0     15.0         7.0     2.0   9.0     35.0
2019-02-11 08:30:00          2.0  68.0       11.0     20.0         3.0     1.0   9.0     41.0
2019-02-11 08:20:00          3.0  12.0        8.0     39.0         7.0     1.0   5.0     23.0
2019-02-11 08:10:00          2.0   NaN       12.0     17.0         3.0     2.0   8.0     37.0
2019-02-11 08:00:00          1.0   NaN       16.0     59.0         5.0     1.0  17.0     90.0
2019-02-11 07:50:00          1.0   NaN       11.0     23.0         3.0     1.0  14.0     22.0
2019-02-11 07:40:00          NaN   NaN        8.0     20.0         4.0     2.0  24.0     36.0
2019-02-11 07:30:00          1.0   NaN        9.0     25.0         8.0     1.0  22.0     35.0
2019-02-11 07:20:00          1.0   NaN        7.0     19.0         4.0     4.0  13.0     11.0
2019-02-11 07:10:00          2.0   NaN        6.0     10.0         5.0     NaN  21.0     26.0
2019-02-11 07:00:00          1.0   NaN        9.0     19.0         2.0     NaN  12.0     23.0
2019-02-11 06:50:00          NaN   NaN        3.0     10.0         4.0     1.0   1.0     15.0
2019-02-11 06:40:00          NaN   NaN        4.0      6.0         NaN     2.0   2.0     14.0
2019-02-11 06:30:00          2.0   NaN        3.0     12.0         1.0     1.0   6.0     34.0
2019-02-11 06:20:00          1.0   NaN        1.0     15.0         NaN     1.0   3.0     10.0
2019-02-11 06:10:00          1.0   NaN        8.0     12.0         NaN     4.0   4.0     15.0
```


