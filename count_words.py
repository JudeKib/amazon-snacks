from collections import Counter


def get_words(title) -> list:
    useless_words = {'the', 'an', 'a', 'and', 'or', 'of', 'for', 'on', 'to', 'per', 'with', 'by', 'lb',
                     'oz', 'ounce', 'ounces', 'count', 'ct', 'snack', 'snacks', 'may', 'vary', '&', '-', '|'}
    title_words = set([word.strip('.,()/*') for word in title.lower().split()])
    filtered_title_words = [word for word in title_words if word not in useless_words]
    return filtered_title_words


def by_category(clean_data) -> dict:
    word_counts = {}
    for row in clean_data:
        category = row['category']
        
        if not word_counts.get(category):
            word_counts.update({category: Counter()})

        title_words = get_words(row['title'])
        word_counts[category].update(title_words)

    return word_counts