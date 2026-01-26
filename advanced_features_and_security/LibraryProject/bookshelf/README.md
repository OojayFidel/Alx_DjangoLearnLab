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
