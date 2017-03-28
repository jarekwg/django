from django.db import models


class NulledCharField(models.CharField):
    """
    Sensible use case: We want uniqueness on a CharField whilst also allowing it to be empty.
    In the DB, '' == '', but NULL != NULL. So we store emptystring as NULL in the db, but treat it
    as emptystring in the code.
    """
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return ''
        else:
            return value

    def to_python(self, value):
        if isinstance(value, models.CharField):
            return value
        if value is None:
            return ''
        return value

    def get_prep_value(self, value):
        if value is '':
            return None
        else:
            return value
