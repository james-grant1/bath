# Analyzing the Hacker Within Survey

Log into [Qualtrics site](https://www.qualtrics.com/uk/).

Go to survey [Data and Analysis page](https://qsharingeu.eu.qualtrics.com/responses/#/surveys/SV_37Xf4QHwHq5ZU3P)

Export as Tab Separated values with default options.

That gives you a zip file with name like
`Hacker+Within+topics_August+6%2C+2018_08.47.zip`.

Unzip into this directory to give you the similarly named `.tsv` file.

Process with something like:

```
python anonymize_data.py "Hacker Within topics_August 6, 2018_08.47.tsv"
```

This gives `thw_survey.csv` that should already be committed to the repository.
