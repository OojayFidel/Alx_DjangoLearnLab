# Django Blog Authentication System

## Overview
This project implements a complete user authentication system including registration, login, logout, and profile management using Django's built-in authentication framework.

## Features
- User registration with email field
- Login and logout functionality
- Profile view and edit
- CSRF protection
- Secure password hashing

## URL Endpoints
- /register/
- /login/
- /logout/
- /profile/

## Setup Instructions
1. Clone the repository
2. Install dependencies
3. Run migrations:
   python manage.py migrate
4. Start server:
   python manage.py runserver

## Testing
- Register a new account
- Login and logout
- Edit profile
- Verify protected routes redirect when not logged in

## Security
- CSRF tokens enabled
- Passwords securely hashed
- Profile access protected using login_required

## Blog Post Management Features (CRUD)

This project implements full CRUD (Create, Read, Update, Delete) functionality for blog posts using Django’s class-based views.

### Features Implemented

- Users can view all posts (`ListView`)
- Users can view individual posts (`DetailView`)
- Authenticated users can create new posts (`CreateView`)
- Authors can edit their own posts (`UpdateView`)
- Authors can delete their own posts (`DeleteView`)

---

### URL Routes

| Route | Description | Access |
|-------|------------|--------|
| `/posts/` | View all blog posts | Public |
| `/posts/<int:pk>/` | View a single post | Public |
| `/posts/new/` | Create a new post | Authenticated users only |
| `/posts/<int:pk>/edit/` | Edit a post | Author only |
| `/posts/<int:pk>/delete/` | Delete a post | Author only |

---

### Permissions and Access Control

- **List and Detail views are publicly accessible** to all users.
- **Creating a post requires authentication** using `LoginRequiredMixin`.
- **Editing and deleting posts are restricted to the post author** using:
  - `LoginRequiredMixin`
  - `UserPassesTestMixin`
- Unauthorized users attempting to edit or delete a post they do not own will receive a permission error (403).

---

### Security Implementation

- CSRF protection is enabled for all POST forms.
- Post authorship is automatically assigned to the logged-in user.
- Django’s authentication system ensures secure session handling.

---

### Testing Instructions

1. Navigate to `/posts/` to view all posts.
2. Attempt to access `/posts/new/` while logged out (should redirect to login).
3. Log in and create a new post.
4. Edit your own post — changes should save successfully.
5. Log in as a different user and attempt to edit another user's post — access should be denied.
6. Delete a post as its author and confirm it is removed from the list view.

---

