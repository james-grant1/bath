""" Script to anonymize THW data
"""

import sys

import pandas as pd

fname = sys.argv[1]

full_df = pd.read_table(fname, encoding='utf_16_le')

# Drop the first 19 questions (potentially identifying).
df = full_df.iloc[:, 19:].copy()

# Drop the another column (doesn't have any useful data)
df.drop(columns='Q3 - Topics', inplace=True)

# The first row has a description of the questions.
descriptions = df.iloc[0, :]
# The second has an import-id.
# Drop these from the current dataframe.
df.drop([0, 1], inplace=True)


def to_var(in_str):
    return '_'.join(in_str.lower().strip().split())


OPTION_RECODER = {'code': 'testing',
                  'continuous': 'continuous_integration',
                  'programming': 'programming_paradigms',
                  'data': 'visualization',
                  'object': 'object_oriented',
                  'different': 'data_modes',
                  'running': 'bear_batch',
                  'api': 'api_driven_development',
                  'fast': 'fast_databases',
                  'version': 'version_control_git',
                  'choosing': 'choosing_text_editor',
                  'comparing': 'comparing_vc_software',
                  'mean': 'MEAN_software_stack',
                 }


def get_opt(in_str):
    parts = in_str.lower().strip().split()
    if len(parts) > 1 and parts[1] == 'node.js':
        return parts[1]
    opt = parts[1] if parts[0] == 'the' else parts[0]
    return OPTION_RECODER.get(opt, opt)



# Replace Q11_0_1_RANK etc names with something more descriptive
new_names = []
for name, description in zip(df.columns, descriptions):
    d_parts = description.split(' - ')
    if name.startswith('Q17'):
        # Rank categories question variables
        d_type = to_var(d_parts[1])
        new_names.append('category-' + d_type)
        continue
    # A group / rank questions
    # key tools, language etc
    area = to_var(d_parts[0].split('.')[0])
    # Whether this is a group or rank variable
    grp_rank = to_var(d_parts[1])
    # Whether this is a Yes or a Maybe variable
    y_m = to_var(d_parts[2].split(' ')[0])
    name_parts = [area, grp_rank, y_m]
    if grp_rank == 'ranks':
        # The option to which rank refers
        name_parts.append(get_opt(d_parts[3]))
    new_names.append('-'.join(name_parts))

df.columns = new_names

# Save cleaned data to csv
df.to_csv('thw_survey.csv', index=False)
