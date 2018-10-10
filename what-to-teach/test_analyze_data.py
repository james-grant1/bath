""" Tests for analyze_data module

Run with::

    pytest test_analyze_data.py
"""
from __future__ import division

from numpy import nan, allclose

import pandas as pd

from analyze_data import (ana_question, ana_part, category_weights,
                          get_categories)

# Version of allclose that also checks NaN values are in correct position
def nallclose(first, second):
    return allclose(first, second, equal_nan=True)


def test_ana_part():
    # Dataframe where col0 has choice, no others.
    df = pd.DataFrame({'col0': [1, nan],
                       'col1': [nan, nan]})
    assert nallclose(ana_part(df),
                     [[1.0, nan],
                      [nan, nan]])
    # All choices
    df = pd.DataFrame({'col0': [1, 2],
                       'col1': [2, 1]})
    assert nallclose(ana_part(df),
                     [[1.0, 0.5],
                      [0.5, 1]])
    # Dataframe where col0 and col1 have choices
    df = pd.DataFrame({'col0': [1, nan],
                       'col1': [nan, 2]})
    assert nallclose(ana_part(df),
                     [[1.0, nan],
                      [nan, 0.5]])
    df = pd.DataFrame({'col0': [2, nan],
                       'col1': [nan, 1]})
    assert nallclose(ana_part(df),
                     [[0.5, nan],
                      [nan, 1]])
    # Three potential options
    df = pd.DataFrame({'cola': [2, nan, nan],
                       'colb': [nan, 1, nan],
                       'colc': [nan, nan, nan]})
    assert nallclose(ana_part(df),
                     [[2/3, nan, nan],
                      [nan, 1, nan],
                      [nan, nan, nan]])
    # Three potential options
    df = pd.DataFrame({'cola': [1, nan, nan],
                       'colb': [nan, 3, nan],
                       'colc': [nan, nan, 2]})
    assert nallclose(ana_part(df),
                     [[1, nan, nan],
                      [nan, 1/3, nan],
                      [nan, nan, 2/3]])



def dallclose(first, second):
    # Assert dictionaries contain same keys, similar values
    if sorted(first) != sorted(second):
        return False
    for key, value in first.items():
        if not nallclose(value, second[key]):
            return False
    return True


def test_ana_question():
    # opt1 yes both, no maybes
    df = pd.DataFrame({'q1-ranks-yes-opt1': [1, 1],
                       'q1-ranks-yes-opt2': [nan, nan],
                       'q1-ranks-maybe-opt1': [nan, nan],
                       'q1-ranks-maybe-opt2': [nan, nan]})
    # Two ranks 1, translates to two 2 values, total is 4.
    assert dallclose(ana_question(df, 'q1'),
                     {'opt1': 4,
                      'opt2': 0})
    df.loc[0, 'q1-ranks-yes-opt1'] = nan
    # One ranks 1, translates to one 2 values, total is 2.
    assert dallclose(ana_question(df, 'q1'),
                     {'opt1': 2,
                      'opt2': 0})
    df.loc[:, 'q1-ranks-maybe-opt2'] = [1, 1]
    # Previous total, plus two 1s for opt2
    assert dallclose(ana_question(df, 'q1'),
                     {'opt1': 2,
                      'opt2': 2})
    df.loc[0, 'q1-ranks-maybe-opt2'] = nan
    assert dallclose(ana_question(df, 'q1'),
                     {'opt1': 2,
                      'opt2': 1})
    df.loc[1, 'q1-ranks-yes-opt1'] = nan
    assert dallclose(ana_question(df, 'q1'),
                     {'opt1': 0,
                      'opt2': 1})
    df = pd.DataFrame({'q1-ranks-yes-opt1': [nan, nan],
                       'q1-ranks-yes-opt2': [1, 1],
                       'q1-ranks-maybe-opt1': [1, 1],
                       'q1-ranks-maybe-opt2': [nan, nan]})
    assert dallclose(ana_question(df, 'q1'),
                     {'opt1': 2,
                      'opt2': 4})
    df = pd.DataFrame({'q1-ranks-yes-opt1': [2, 2],
                       'q1-ranks-yes-opt2': [1, 1],
                       'q1-ranks-maybe-opt1': [nan, nan],
                       'q1-ranks-maybe-opt2': [nan, nan]})
    assert dallclose(ana_question(df, 'q1'),
                     {'opt1': 1.5 + 1.5,
                      'opt2': 2 + 2})
    assert dallclose(ana_question(df, 'q1', row_weights=[1, 0.5]),
                     {'opt1': 1.5 + 1.5 * 0.5,
                      'opt2': 2 + 2 * 0.5})
    df = pd.DataFrame({'q1-ranks-yes-opt1': [nan, 1],
                       'q1-ranks-yes-opt2': [1, nan],
                       'q1-ranks-maybe-opt1': [1, nan],
                       'q1-ranks-maybe-opt2': [nan, 1]})
    assert dallclose(ana_question(df, 'q1'),
                     {'opt1': 2 + 1,
                      'opt2': 2 + 1})
    # Test weighting
    assert dallclose(ana_question(df, 'q1', row_weights=[1, 0.5]),
                     {'opt1': 1 + 1,
                      'opt2': 2 + 0.5})



def test_category_weights():
    df = pd.DataFrame({'cola': [1, nan, nan],
                       'colb': [nan, 3, nan],
                       'colc': [nan, nan, 2]})
    assert get_categories(df) == []
    assert category_weights(df).empty
    df = pd.DataFrame({'category-one': [1, 2],
                       'category-two': [2, 1]})
    assert get_categories(df) == ['category-one', 'category-two']
    exp = pd.DataFrame({'one': [1, 0.5],
                        'two': [0.5, 1]})
    assert category_weights(df).equals(exp)
    df = pd.DataFrame({'category-one': [1, nan],
                       'category-two': [nan, 1]})
    exp = pd.DataFrame({'one': [1., 0.],
                        'two': [0., 1.]})
    assert category_weights(df).equals(exp)
