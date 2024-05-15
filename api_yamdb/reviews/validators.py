import datetime

from django.core.validators import MaxValueValidator

current_year = datetime.datetime.now().year

validate_year = [MaxValueValidator(current_year)]
