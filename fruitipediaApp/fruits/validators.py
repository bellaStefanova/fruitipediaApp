from django.core.exceptions import ValidationError


def validate_name(value):
    for s in value:
        if not s.isalpha():
            raise ValidationError("Fruit name should contain only letters!")