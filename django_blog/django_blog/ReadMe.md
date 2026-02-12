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
