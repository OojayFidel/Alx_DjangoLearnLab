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


## Comment Functionality for Blog Posts

This project implements a comment system to improve interactivity on blog posts. Users can read comments under each post, authenticated users can add new comments, and comment authors can edit or delete their own comments.

### Features Implemented

- Display all comments related to a specific blog post
- Authenticated users can add comments from the post detail page
- Comment authors can update (edit) their own comments
- Comment authors can delete their own comments
- Permissions are enforced to prevent unauthorized edits/deletes

---

### Comment Model

The comment system is built using a `Comment` model with the following fields:

- `post` (ForeignKey): Links each comment to a specific `Post` (many comments to one post)
- `author` (ForeignKey): Links each comment to the Django `User` model
- `content` (TextField): The body of the comment
- `created_at` (DateTimeField): Timestamp when the comment was created
- `updated_at` (DateTimeField): Timestamp when the comment was last updated

---

### URL Routes

| Route | Description | Access |
|-------|------------|--------|
| `/post/<int:pk>/` | View a post and its comments | Public |
| `/post/<int:pk>/comment/new/` | Add a new comment to a post | Authenticated users only |
| `/comment/<int:pk>/update/` | Edit a comment | Comment author only |
| `/comment/<int:pk>/delete/` | Delete a comment | Comment author only |

---

### Permissions and Access Control

- Anyone can view posts and their comments.
- Only authenticated users can add comments.
- Only the comment author can edit or delete their comment.
- Unauthorized users attempting to modify another user’s comment will be blocked (403).

---

### Security Implementation

- All POST forms use CSRF protection (`{% csrf_token %}`).
- Comment authorship is automatically assigned to the logged-in user.
- Django authentication and session management are used for secure access control.

---

### Testing Instructions

1. Open a post detail page (e.g., `/post/1/`) and confirm comments are displayed.
2. While logged out, attempt to add a comment — you should be redirected to login.
3. Log in and submit a comment — confirm it appears under the post.
4. Edit your own comment — confirm the update is saved.
5. Log in as another user and try to edit/delete a comment you do not own — access should be denied.
6. Delete your own comment — confirm it is removed from the post detail page.

---


## Advanced Features: Tagging and Search

This project includes tagging and search functionality to improve content organization and make posts easier to discover. Users can assign multiple tags to a post and search posts by title, content, or tag names.

### Features Implemented

- Tag model created to store reusable tags
- Many-to-Many relationship between `Post` and `Tag`
- Posts can have multiple tags, and tags can belong to multiple posts
- Tag field supports creating new tags that don’t already exist
- Search supports queries across:
  - post title
  - post content
  - tag names
- Tag names are displayed on posts and are clickable to filter posts by tag

---

### Tagging System

#### Tag Model
Tags are stored using a `Tag` model with a unique `name` field. A Many-to-Many relationship is established between `Post` and `Tag` to support multiple tags per post.

#### Adding Tags to Posts
The `PostForm` includes a `tags` input field that accepts **comma-separated values** (e.g., `food, spicy, friday`). During save:
- each tag name is cleaned and split
- existing tags are reused
- new tags are created automatically if they do not exist
- selected tags are linked to the post

---

### Search Functionality

A search endpoint allows users to search for posts using a query parameter. The search checks for matches in:
- `title` (case-insensitive)
- `content` (case-insensitive)
- `tags__name` (case-insensitive)

The results are displayed on a dedicated search results page.

---

### URL Routes

| Route | Description | Access |
|------|-------------|--------|
| `/search/` | Search posts by title/content/tags using `?q=` | Public |
| `/tags/<tag_name>/` | View all posts with a specific tag | Public |

---

### Template Updates

- A search bar is included in the post listing template to submit queries to `/search/`.
- Tags are displayed on post list and post detail pages.
- Each tag is linked to a filtered view that shows only posts containing that tag.
- Dedicated pages exist for:
  - tag-filtered posts
  - search results

---

### Testing Instructions

1. Create or edit a post and add tags using comma-separated values (e.g., `food, spicy, friday`).
2. Open the post detail page and confirm tags display correctly.
3. Click a tag and confirm it opens the filtered tag page (`/tags/<tag_name>/`).
4. Use the search bar to search a keyword found in:
   - a title
   - a content body
   - a tag name  
   Confirm matching posts appear on `/search/`.
5. Confirm searching a non-existing term returns “No matching posts found.”

---

