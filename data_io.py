import csv

def get_raw_data() -> list:
    with open('amazon_snacks_scraped_data.csv', newline='', encoding='utf-8') as datafile:
        reader = csv.DictReader(datafile)

        raw_data = []
        for row in reader:
            raw_data.append(row)

    return raw_data


def write_clean_data(clean_data) -> None:
    with open('clean_data\cleaned_amazon_snacks_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fields = [
            'bsr',
            'title',
            'simplified_title',
            'list_price',
            'sale_price',
            'has_coupon',
            'has_deal',
            'deal_discount',
            'rating',
            'reviews_count',
            'category',
            'subcategory']
        writer = csv.DictWriter(csvfile, fields)

        writer.writeheader()
        for row in clean_data:
            writer.writerow(row)
            

def write_title_word_counts(word_counts) -> None:
    with open('clean_data\\title_word_counts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fields = ['category', 'word', 'count']
        writer = csv.DictWriter(csvfile, fields, restval=0)

        for category, word_count in word_counts.items():
            for word, ct in word_count.items():
                row = {'category': category, 'word': word, 'count': ct}
                writer.writerow(row)