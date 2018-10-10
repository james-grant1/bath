""" Analyze cleaned survey data

See anonymize_data.py for structure of data frame.

Run tests with::

    pytest test_analyze_data.py
"""
from __future__ import division

import numpy as np


def ana_question(df, q_root, row_weights=None):
    row_weights = 1 if row_weights is None else np.array(row_weights)[:, None]
    yes_qs = [q for q in df.columns
              if q.startswith(q_root + '-ranks-yes')]
    maybe_qs = [q for q in df.columns
              if q.startswith(q_root + '-ranks-maybe')]
    yes_rescaled = ((ana_part(df[yes_qs]) + 1).fillna(0).as_matrix() *
                    row_weights)
    maybe_rescaled = ana_part(df[maybe_qs]).fillna(0).as_matrix() * row_weights
    values = (yes_rescaled + maybe_rescaled).sum(axis=0)
    names = [q.split('-')[-1] for q in yes_qs]
    return dict(zip(names, values))


def get_categories(df):
    return [q for q in df.columns if q.startswith('category')]


def category_weights(df):
    categories = get_categories(df)
    weights = ana_part(df[categories]).copy().fillna(0)
    cat_names = [q.split('-')[-1] for q in categories]
    weights.columns = cat_names
    return weights


def ana_part(cols):
    n = len(cols.columns)
    return (n - (cols - 1)) / n


def process_data(df):
    categories = get_categories(df)
    weights = category_weights(df)
    cat_names = weights.columns
    cat_rank_mean = dict(zip(cat_names, df[categories].mean()))
    cat_scores = {}
    w_cat_scores = {}
    for cat in cat_names:
        cat_scores[cat] = ana_question(df, cat)
        w_cat_scores[cat] = ana_question(df, cat, weights[cat])
    return cat_rank_mean, cat_scores, w_cat_scores


def main():
    from pprint import pprint
    import pandas as pd
    df = pd.read_csv('thw_survey.csv')
    cat_rank_mean, cat_scores, w_cat_scores = process_data(df)
    print('Mean rank of categories')
    pprint(cat_rank_mean)
    print('Composite ranking score within categories')
    pprint(cat_scores)
    print('Weighted composite ranking score within categories')
    pprint(w_cat_scores)


if __name__ == '__main__':
    main()
