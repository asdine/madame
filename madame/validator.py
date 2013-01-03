# -*- coding: utf-8 -*-

"""
    Madame.validator
    ~~~~~~

    Custom schema validator based on validictory.

    :copyright: (c) 2012 by Asdine El Hrychy.
    :license: MIT, see LICENSE for more details.
"""

import re
import validictory
from validictory import SchemaValidator


class CustomValidator(SchemaValidator):
    def validate_type_objectid(self, val):
        """Adds a method to handle ObjectIds"""
        return re.match('[a-f0-9]{24}', val)

class Validator():
    def validate(self, data, schema):
        try:
            validictory.validate(data, schema, validator_cls=CustomValidator)
            return True
        except ValueError, error:
            self.error = str(error)
        return False
