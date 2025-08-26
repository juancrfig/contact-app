from flask import Flask, request
from db import db
from flask_smorest import abort
import uuid

app = Flask(__name__)

@app.get("/contacts")
def get_contacts():

    # Check for the 'favorite' query parameter. It'll return None if the parameter is not in the URL
    favorite_request = request.args.get('favorite')
    if favorite_request and favorite_request.lower() == 'true':
        favorite_contacts = [
            contact for contact in db["contacts"] if contact["favorite"]
        ]
        return {"contacts": favorite_contacts}
    else:
        return {"contacts": db["contacts"]}

@app.post("/contacts")
def create_contact():
    contact_data = request.get_json()

    if (
        "first_name" not in contact_data
        or "last_name" not in contact_data
        or "email" not in contact_data
        or "favorite" not in contact_data
    ):
        abort(400,message="Bad Request. Ensure 'first_name', 'last_name' and 'email' are present.")

    for contact in db["contacts"]:
        if contact["email"] == contact_data["email"]:
            abort(400, message="Email already registered.")

    contact_id = uuid.uuid4().hex
    new_contact = {**contact_data, "id": contact_id}
    db["contacts"].append(new_contact)

    return new_contact

@app.delete("/contacts")
def delete_contact():
    email_to_delete = request.get_json()["email"]

    for contact in db["contacts"]:
        if contact["email"] == email_to_delete:
            db["contacts"].remove(contact)

    return f"Contact with email {email_to_delete} deleted."

@app.put("/contacts")
def update_contact():
    email_to_update = request.get_json()["email"]

    for contact in db["contacts"]:
        if contact["email"] == email_to_update:
            contact["favorite"] = not contact["favorite"]
    return f"Contact with email {email_to_update} updated."
