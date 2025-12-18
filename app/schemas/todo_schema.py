from marshmallow import Schema, fields, validate, ValidationError, pre_load

class TodoCreateSchema(Schema):
    title = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=255),
        error_messages={
            "required": "Title is required",
            "null": "Title is required",
            "invalid": "Title must be a string",
        },
    )

    completed = fields.Bool(
        load_default=False,  #optional value, if not provided value will be automatically  set to False
        error_messages={
            "invalid": "Completed must be a boolean",
        },
    )

    # @pre_load is a hook in Marshmallow that runs before the input data is deserialized into Python objects.
    @pre_load
    def strip_title(self, data, **kwargs):  # Using **kwargs allows method to accept any extra arguments Marshmallow might send, without breaking.
        if "title" in data and isinstance(data["title"], str):
            data["title"] = data["title"].strip()
        return data


class TodoUpdateSchema(Schema):
    title = fields.Str(
        required=False,
        allow_none=True,
        validate=validate.Length(min=1, max=255),
        error_messages={
            "invalid": "Title must be a string",
        },
    )

    completed = fields.Bool(
        required=False,
        allow_none=True,
        error_messages={
            "invalid": "Completed must be a boolean",
        },
    )

    @pre_load
    def strip_title(self, data, **kwargs):
        if "title" in data and isinstance(data["title"], str):
            data["title"] = data["title"].strip()
        return data

