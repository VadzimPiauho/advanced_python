import requests
import json


API_key = "b040dcab9c3a195f42200439"


class Money(object):
    def __init__(self, value, currency="USD"):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f"{self.value} {self.currency}"

    def __repr__(self):
        return f"{self.value} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money):
            value = other.value
            if self.currency != other.currency:
                value = other.value / self.currency_rate(self.currency, other.currency)    # noqa
            return Money(self.value + value, self.currency)
        else:
            return Money(self.value + other, self.currency)

    def __radd__(self, other):
        return Money(other + self.value, self.currency)

    def __mul__(self, other):
        if isinstance(other, Money):
            value = other.value
            if self.currency != other.currency:
                value = other.value / self.currency_rate(self.currency, other.currency)    # noqa
            return Money(self.value * value, self.currency)
        else:
            return Money(self.value * other, self.currency)

    def __rmul__(self, other):
        return Money(other * self.value, self.currency)

    def currency_rate(self, basic_exchange_rate, secondary_exchange_rate):
        url = f"https://v3.exchangerate-api.com/bulk/{API_key}/{basic_exchange_rate}"    # noqa
        request = json.loads(requests.get(url).text)
        return request["rates"][secondary_exchange_rate]


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11)   # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    print(z + 3.11*x + y*0.8)   # result in “EUR”
    # >>543.21 EUR

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]

    s = sum(lst)

    print(s)    # result in “BYN”
    # >>123.45 BYN
