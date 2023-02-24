from flask_admin.babel import gettext

from wtforms.validators import StopValidation
from wtforms.fields import SelectMultipleField
from flask_mongoengine.wtf.fields import ModelSelectMultipleField


class FieldListInputRequired(object):
    """
        Validates that at least one item was provided for a FieldList
    """

    field_flags = ('required',)

    def __call__(self, form, field):
        if type(field) is ModelSelectMultipleField:
            print(field.data)
            if len(field.data) == 0:
                field.errors[:] = []
                raise StopValidation(gettext('This field requires at least one item.'))
        elif type(field) is SelectMultipleField:
            print('SELECTFIELD')
            print(field.data)
            if len(field.data) == 0:
                field.errors[:] = []
                raise StopValidation(gettext('This field requires at least one item.'))
        else:
            if len(field.entries) == 0:
                field.errors[:] = []
                raise StopValidation(gettext('This field requires at least one item.'))
