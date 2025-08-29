from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from models.db import db
from models.contacts import ContactModel
from resources.schemas import ContactUpdateSchema
from .schemas import ContactSchema
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint("contacts", __name__, description="Operations related to contacts")

@blp.route("/contacts")
class ContactList(MethodView):

    @jwt_required
    @blp.response(200, ContactSchema(many=True))
    def get(self):
        """Retrieves all contacts"""
        return ContactModel.query.all()

    @jwt_required
    @blp.arguments(ContactSchema)
    @blp.response(201, ContactSchema)
    def post(self, contact_data):
        """Creates a new contact"""
        # The database can enforce email uniqueness, which is more reliable
        if ContactModel.query.filter(ContactModel.email == contact_data["email"]).first():
            abort(409, message="A contact with that email already exists")

        contact = ContactModel(**contact_data)

        try:
            db.session.add(contact)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(409, message=f"There was a problem creating a new contact: {e}")

        return contact

    @jwt_required
    @blp.route("/contacts/<string:contact_id>")
    class Contact(MethodView):
        @blp.response(200, ContactSchema)
        def delete(self, contact_id):
            """Deletes a contact by its ID"""
            contact = ContactModel.query.get_or_404(contact_id)
            db.session.delete(contact)
            db.session.commit()
            # A 204 response is standard for successful deletion with no content to return
            return {"message": "Contact deleted successfully"}, 200


    @jwt_required
    @blp.arguments(ContactUpdateSchema)
    @blp.response(200, ContactSchema)
    def patch(self, update_data, contact_id):
        """Updates an existing contact's favorite state"""
        contact = ContactModel.query.get_or_404(contact_id)

        # Update the contact object with new data if it exists in the request
        for key, value in update_data.items():
            setattr(contact, key, value)

        db.session.add(contact)
        db.session.commit()

        return contact

