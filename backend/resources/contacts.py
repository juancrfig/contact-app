import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import db
from schemas import ContactSchema


blp = Blueprint("contacts", __name__, description="Operations related to contacts")

@blp.route("/contacts")
class Contact(MethodView):

    @blp.response(200, ContactSchema(many=True))
    def get(self):
        # Check for the 'favorite' query parameter. It'll return None if the parameter is not in the URL
        favorite_request = request.args.get('favorite')
        if favorite_request and favorite_request.lower() == 'true':
            favorite_contacts = [
                contact for contact in db["contacts"] if contact["favorite"]
            ]
            return {"contacts": favorite_contacts}
        else:
            return {"contacts": db["contacts"]}

    def delete(self):
        email_to_delete = request.get_json()["email"]

        for contact in db["contacts"]:
            if contact["email"] == email_to_delete:
                db["contacts"].remove(contact)

        return f"Contact with email {email_to_delete} deleted."

    @blp.arguments(ContactSchema)
    @blp.response(201, ContactSchema)
    def post(self, contact_data):

        for contact in db["contacts"]:
            if contact["email"] == contact_data["email"]:
                abort(400, message="Email already registered.")

        contact_id = uuid.uuid4().hex
        new_contact = {**contact_data, "id": contact_id}
        db["contacts"].append(new_contact)

        return new_contact

    def put(self, data):
        email_to_update = data["email"]

        for contact in db["contacts"]:
            if contact["email"] == email_to_update:
                contact["favorite"] = not contact["favorite"]

        return f'Contact with email: "{email_to_update}" updated.'