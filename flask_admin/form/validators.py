from flask_admin.babel import gettext

from wtforms.validators import StopValidation
from wtforms.fields import SelectMultipleField


class FieldListInputRequired(object):
    """
        Validates that at least one item was provided for a FieldList
    """

    field_flags = ('required',)

    def __call__(self, form, field):
        if type(field) is not SelectMultipleField:
            if len(field.entries) == 0:
                field.errors[:] = []
                raise StopValidation(gettext('This field requires at least one item.'))
        else:
            if len(field.choices) == 0:
                field.errors[:] = []
                raise StopValidation(gettext('This field requires at least one item.'))
