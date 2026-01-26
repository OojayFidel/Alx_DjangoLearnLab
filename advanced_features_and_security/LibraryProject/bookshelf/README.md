# Permissions and Groups Setup

Custom permissions were added to the Book model:
- can_add_book
- can_change_book
- can_delete_book

Groups created in Django Admin:
- Viewers
- Editors
- Admins

Permissions assigned:
- Editors: can_add_book, can_change_book
- Admins: can_add_book, can_change_book, can_delete_book

Views are protected using Django's @permission_required decorator.

# Security Best Practices (Task 3)

## Secure settings (settings.py)
- Enabled browser security headers:
  - SECURE_BROWSER_XSS_FILTER
  - X_FRAME_OPTIONS
  - SECURE_CONTENT_TYPE_NOSNIFF
- Enabled HTTPS-only cookies:
  - CSRF_COOKIE_SECURE
  - SESSION_COOKIE_SECURE
- Added HttpOnly and SameSite protections for cookies.

## CSRF Protection
- Added `{% csrf_token %}` to POST forms.

## SQL Injection Prevention
- User input validated with Django Forms.
- Database queries use Django ORM filters (parameterized), no raw SQL.

## Content Security Policy (CSP)
- Added a custom middleware that injects a basic CSP header to reduce XSS risk.

