from marshmallow import Schema, fields, validate, ValidationError, pre_load

class UserCreateSchema(Schema):
    username = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=255),
        error_messages={
            "required": "Title is required",
            "null": "Title is required",
            "invalid": "Title must be a string",
        },
    )

    email = fields.Str(
        required=True,
        error_messages={
            "invalid": "Email is required",
        },
    )

    password = fields.Str(
        required=True,
        error_messages={
            "invalid": "Password is required"
        }
    )

    @pre_load
    def strip_title(self, data, **kwargs):
        if "title" in data and isinstance(data["title"], str):
            data["title"] = data["title"].strip()
        return data



# class TodoUpdateSchema(Schema):
#     title = fields.Str(
#         required=False, 
#         allow_none=True,
#         validate=validate.Length(min=1, max=255),
#         error_messages={
#             "invalid": "Title must be a string",
#         },
#     )

#     completed = fields.Bool(
#         required=False,
#         allow_none=True,
#         error_messages={
#             "invalid": "Completed must be a boolean",
#         },
#     )

#     @pre_load
#     def strip_title(self, data, **kwargs):
#         if "title" in data and isinstance(data["title"], str):
#             data["title"] = data["title"].strip()
#         return data