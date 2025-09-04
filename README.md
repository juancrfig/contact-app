# User Stories

- **Epic: Authentication**
  - **Story 1: User Login**
    - As a user, I want to log in with my username and password, so that I can securely access my private contact list.
    - **Acceptance Criteria:**
      - Given I am on the login page, when I enter valid credentials and submit the form, then I am redirected to the "Overview" screen.
      - Given I am on the login page, when I enter invalid credentials, then I see an error message and remain on the login page.

---

- **Epic: Core Application Layout & Navigation**
  - **Story 2: Main Navigation**
    - As a user, I want to see a persistent navigation bar at the top of the screen, so that I can easily navigate between the main sections of the application.
    - **Acceptance Criteria:**
      - The navigation bar is always visible after a successful login.
      - The navigation bar contains links for "Overview," "Contacts," and "Favorites."
      - The navigation bar contains a primary button labeled "New."

---

- **Epic: Contact Management**
  - **Story 3: Create a New Contact**
    - As a user, I want to click a "New" button that opens a form, so that I can add a new person to my contact list.
    - **Acceptance Criteria:**
      - Clicking the "New" button in the navigation bar displays a contact creation form.
      - The form contains input fields for First Name, Last Name, and Email.
      - The form includes an option (e.g., a checkbox or toggle) to set the new contact's "favorite" status.
      - A "Save" button on the form, when clicked, adds the contact to the list and closes the form.
  - **Story 4: Delete a Contact**
    - As a user, I want to be able to delete a contact from the main "Contacts" view, so that I can remove outdated or incorrect entries.
    - **Acceptance Criteria:**
      - On the "Contacts" screen, each contact card has a "Delete" button.
      - Clicking the "Delete" button removes the contact from the application permanently and updates the UI.

---

- **Epic: Contact Viewing & Interaction**
  - **Story 5: View Overview Screen**
    - As a user, I want to see my contacts separated into "Favorites" and "Other Contacts" on the main overview screen, so that I can quickly find my most important contacts.
    - **Acceptance Criteria:**
      - The "Overview" screen contains a distinct section at the top for favorite contacts.
      - A second section displays all non-favorite contacts.
      - Favorite contact cards show the full name, email, picture, and a "Remove from Favorites" button.
      - Non-favorite contact cards show the full name, email, picture, and an "Add to Favorites" button.
      - Changing a contact's favorite status on this screen seamlessly moves it to the correct group in real-time.
  - **Story 6: View All Contacts Screen**
    - As a user, I want to view an alphabetized list of all my contacts, so that I can easily find and manage any individual.
    - **Acceptance Criteria:**
      - The "Contacts" view displays all contacts in a single list, sorted alphabetically by name.
      - Each contact card shows the full name, email, and picture.
      - Favorite contacts are visually distinguished by a colored border around their picture.
      - Each card contains a button to toggle the contact's favorite status and a separate button for deletion.
  - **Story 7: View Favorites Screen**
    - As a user, I want to view a screen that shows only my favorite contacts, so that I can have a focused view of my key people.
    - **Acceptance Criteria:**
      - The "Favorites" view displays only contacts that have been marked as a favorite.
      - Each contact card shows the full name, email, picture, and a "Remove from Favorites" button.
      - Clicking the remove button updates the UI instantly, removing the contact from this view.
  - **Story 8: Paginate Contact Lists**
    - As a user, I want to see contact lists broken into pages when they become too long, so that the interface remains clean and performs well.
    - **Acceptance Criteria:**
      - On any view that displays contacts ("Contacts", "Favorites", etc.), a maximum of 16 contacts (a 4x4 grid) are shown at a time.
      - If more than 16 contacts exist in a given list, pagination controls appear at the bottom.
      - The pagination controls allow me to navigate between pages of contacts.

---
