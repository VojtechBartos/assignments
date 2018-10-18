import pytest
import pandas as pd
from assignments.counter.counter import count_analyses


df1 = [
    {'location': "SF", 'product': "iPhone", 'quantity': 10},
    {'location': "LA", 'product': "iPhone", 'quantity': 11},
    {'location': "SF", 'product': "iMac", 'quantity': 12},
    {'location': "LA", 'product': "iMac", 'quantity': 13}
]

df2 = [
    {'location': "SF", 'product': "iPhone", 'color': 'black', 'quantity': 10},
    {'location': "LA", 'product': "iPhone", 'color': 'black', 'quantity': 11},
    {'location': "SF", 'product': "iMac", 'color': 'grey', 'quantity': 12},
    {'location': "LA", 'product': "iMac", 'color': 'grey', 'quantity': 13}
]

@pytest.mark.parametrize("data,expected", [
    (df1, 8),
    (df2, 16)
])
def test_count_analyses(data, expected):
    assert count_analyses(pd.DataFrame(data)) == expected