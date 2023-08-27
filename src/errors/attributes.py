from typing import Any

from errors.enums import AttributeValidationErrorType


class AttributeValidationError(Exception):
    """Exception raised if there is no value when it is needed or if the type is incorrect
    """

    def __init__(
            self,
            error_type: AttributeValidationErrorType,
            *,
            key: str,
            value: Any = None,
            actual_type: Any = None,
            expected_type: Any = None,
            message: str = "Field error [type={type}, key={key}, value={value}, actual_type={actual_type}, expected_type={expected_type}]"
    ):
        """
        :param str key: field name
        :type key: str
        :param value: field value
        :type value: Any
        :param actual_type: field type
        :type actual_type: Any
        :param expected_type: expected field type
        :type expected_type: Any
        :param message: error text template
        :type message: str
        """

        self.message = message.format(type=error_type.value, key=key, value=value, actual_type=actual_type, expected_type=expected_type)
        super().__init__(self.message)