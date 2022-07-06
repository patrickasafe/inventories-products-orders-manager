import string
import random


class Generator:
    '''A class to extend and populate '''

    fruits = ["Uva", "Banana",  "Manga", "Cajá", "Pinha",
              "Maçã", 'Pêra', 'Laranja', 'Limão', "Caqui"]

    fruits_complement = ["da Serra", "do Campo", 'do Sertão',
                         'do Norte', 'do Serrado', 'do Nordeste',
                         "Orgânico", 'Biodegradável', "Comestível",
                         "Masterblaster"]

    @classmethod
    def random_float_generator(cls, min_float, max_float, decimal_numbers):
        float_number_generated = round(
            random.uniform(min_float, max_float), decimal_numbers)
        return float_number_generated

    @classmethod
    def random_string_generator(cls, length):
        string_generated = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase) for _ in range(length))
        return string_generated

    @classmethod
    def random_product_name_generator(cls):
        random_product_name = '{} {}'.format(random.SystemRandom().choice(
            cls.fruits), random.SystemRandom().choice(cls.fruits_complement))
        return random_product_name
