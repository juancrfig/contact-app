from marshmallow import Schema, fields


class ContactSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    favorite = fields.Boolean(required=True)

class ContactUpdateSchema(Schema):
    email = fields.Email(required=True)
    favorite = fields.Boolean(required=False)