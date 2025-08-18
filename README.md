# Task Tracker API (Practice Project)

Practice backend API to manage user tasks. Allows user registration, JWT authentication, and CRUD operations on personal tasks.

Technologies:
- Python 3.10+
- Django 5.2+
- Django REST Framework
- Django REST Framework SimpleJWT
- SQLite

Installation:
1. Clone the repo: git clone https://github.com/joy-amorin/task-tracker-api.git && cd task-tracker-api
2. Create & activate virtual environment, install dependencies, run migrations:
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
3. (Optional) Create superuser: python manage.py createsuperuser
4. Run server: python manage.py runserver

Main Endpoints:

**User Registration**
- URL: /api/register/ (POST)
- Body: {"username": "new_user", "email": "user@example.com", "password": "yourpassword"}
- Response: {"id": 1, "username": "new_user", "email": "user@example.com"}

**JWT Login**
- URL: /api/token/ (POST)
- Body: {"email": "user@example.com", "password": "yourpassword"}
- Response: {"refresh": "<refresh_token>", "access": "<access_token>"}
> Use access token as Authorization: Bearer <access_token> for protected endpoints.

**Tasks CRUD**
- URL base: /api/tasks/ (GET, POST, PATCH, DELETE)
- Each task belongs to a user; only own tasks can be viewed/modified.
- Create task (POST): {"title": "Practice guitar", "description": "Major and minor scales"}
- List tasks (GET): returns only logged-in user's tasks
- Update task (PATCH): {"completed": true}
- Delete task (DELETE): removes the specified task

Authentication & Permissions:
- JWTAuthentication for external clients
- Permissions: IsAuthenticatedOrReadOnly (non-authenticated users can only view)

Notes:
- Each user has their own task list.
- DRF web interface can be used to test registration and login.
