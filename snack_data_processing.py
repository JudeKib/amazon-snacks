import csv
import re
from collections import Counter
import data_cleaner
import data_io
import count_words

raw_data = data_io.get_raw_data()

cleaner = data_cleaner.data_cleaner(raw_data)
clean_data = cleaner.transform_data()

data_io.write_clean_data(clean_data)

data_io.write_title_word_counts(count_words.by_category(clean_data))
