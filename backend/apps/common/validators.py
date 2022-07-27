import string
from django.forms import ValidationError


def validate_name(name: string) -> bool:
    '''Validate if name contains only alphanumerics'''

    if not name.isalpha():
        msg = 'The name must not contain numbers'
        raise ValidationError(msg)
    return True
