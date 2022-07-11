import string


def validate_name(name: string) -> bool:
    '''Validate if name contains alphanumerics'''

    return not name.isalpha()
