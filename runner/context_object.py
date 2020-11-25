class ContextObject:

    def __init__(self):
        self.driver = None
        self.url = ''
        self.offers = set()

    @property
    def offer_list(self):
        return [", ".join(offer) for offer in self.offers]

    def offer_list_data(self):
        return self.offers
