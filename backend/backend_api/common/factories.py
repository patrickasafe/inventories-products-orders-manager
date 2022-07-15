import datetime
import random
from itertools import product

from pytz import UTC


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

    @classmethod
    def min_date_time_generator(cls, min_year: int):
        """A function that returns a DateTime used as parameter for fuzzy.FuzzyDateTime(). """

        min_time = datetime.datetime(min_year, 1, 1, tzinfo=UTC)

        if datetime.datetime.now(tz=UTC) <= min_time:
            return ValueError
        return min_time


# It's not necessary, since factory.fuzzy.Fi
    # @classmethod
    # def count_until(cls, l_number: int):
    #     """A counter function generating a int list"""

    #     result = []
    #     for _ in range(1, l_number+1):
    #         result.append(_)
    #     return result
