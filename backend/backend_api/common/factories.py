import random
from itertools import product


class FactoryUtils:

    @classmethod
    def random_float_generator(cls, min_float, max_float, decimal_numbers):
        return round(
            random.uniform(min_float, max_float), decimal_numbers)

    @classmethod
    def random_string_generator(cls, length, options_array):
        return ''.join(random.SystemRandom().choice(
            options_array) for _ in range(length))

    @classmethod
    def random_name_generator(cls, *args):
        """A function to iterate arrays to combinate values"""

        return [" ".join(element) for element in product(*args)]
