class data_cleaner:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.clean_data = []

    def add_full_title(self):
        self.clean_row.update({'title': self.raw_row['title']})

    def add_simplified_title(self):
        raw_title = self.raw_row['title']
        
        if raw_title.find('|') > -1:
            simplified_title = raw_title.split('|')[0]
        elif raw_title.find(' - ') > -1:
            simplified_title = raw_title.split(' - ')[0]
        elif raw_title.find(',') > -1:
            simplified_title = raw_title.split(',')[0]
        elif raw_title.find(';') > -1:
            simplified_title = raw_title.split(';')[0]
        else:
            simplified_title = raw_title
        self.clean_row.update({'simplified_title': simplified_title})

    def add_list_price(self):
        self.clean_row.update({'list_price': self.raw_row['list_price']})

    def add_sale_price(self):
        self.clean_row.update({'sale_price': self.raw_row['sale_price']})

    def add_has_deal(self):
        self.clean_row.update({'has_deal': self.raw_row['has_deal']})

    def add_deal_discount(self):
        if self.raw_row['has_deal'] == 'TRUE':
            deal_discount = round((1 - float(self.raw_row['sale_price']) / float(self.raw_row['list_price'])) * 100)
            self.clean_row.update({'deal_discount': deal_discount})
        else:
            self.clean_row.update({'deal_discount': ''})

    def add_has_coupon(self):
        self.clean_row.update({'has_coupon': self.raw_row['has_coupon']})
        
    def add_rating(self):
        self.clean_row.update({'rating': self.raw_row['rating']})

    def add_reviews_count(self):
        self.clean_row.update({'reviews_count': self.raw_row['reviews_count']})

    def add_bsr(self):
        self.clean_row.update({'bsr': self.raw_row['bsr']})

    def add_category(self):
        category = self.raw_row['categories'].splitlines()[-2]
        self.clean_row.update({'category': category})

    def add_subcategory(self):
        subcategory = self.raw_row['categories'].splitlines()[-1]
        self.clean_row.update({'subcategory': subcategory})

    def transform_data(self):
        for row in self.raw_data:
            self.clean_row = {}
            self.raw_row = row

            self.add_full_title()
            self.add_simplified_title()
            self.add_list_price()
            self.add_sale_price()
            self.add_has_deal()
            self.add_deal_discount()
            self.add_has_coupon()
            self.add_rating()
            self.add_reviews_count()
            self.add_bsr()
            self.add_category()
            self.add_subcategory()

            self.clean_data.append(self.clean_row)

        return self.clean_data
