from marshmallow import Schema, fields, validate, ValidationError, pre_load

class GroupCreateschema(Schema):
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=255),
        error_messages={
            "required": "Group name is required",
            "null": "Group name is required",
            "invalid": "Group name must be a string",
        },
    )

    @pre_load
    def strip_title(self, data, **kwargs):
        if "name" in data and isinstance(data["name"], str):
            data["name"] = data["name"].strip()
        return data