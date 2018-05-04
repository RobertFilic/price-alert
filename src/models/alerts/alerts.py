

class Alert(object):
    def __init__(self, user, price_limit, item):
        self.user = user
        self.price_limit = price_limit
        self.item = item

    # How would it look like if we would use print method:
    def __repr__(self):
        return "Alert for {} on item {} with price {}".format(self.user.email, self.item, self.price_limit)