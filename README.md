# ChatApp

ChatApp is a real-time chat application built using Django and Django Channels. It allows users to register, log in, and chat with each other in real-time.

## Features

* User registration and authentication
* Real-time messaging using WebSockets
* Display of online users
* Chat history between users

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MaheshKumar1533/ChatApp.git
   cd ChatApp
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Register a new user or log in with an existing user.
3. Start chatting with other users.

## Project Structure

* `ChatApp/` - Main project directory
  * `ChatApp/__init__.py`
  * `ChatApp/asgi.py` - ASGI configuration for the project
  * `ChatApp/settings.py` - Project settings
  * `ChatApp/urls.py` - URL routing for the project
  * `ChatApp/wsgi.py` - WSGI configuration for the project
* `Chat/` - Chat application directory
  * `Chat/__init__.py`
  * `Chat/admin.py` - Admin configuration
  * `Chat/apps.py` - App configuration
  * `Chat/consumers.py` - WebSocket consumers for real-time messaging
  * `Chat/models.py` - Database models
  * `Chat/routing.py` - WebSocket routing
  * `Chat/tests.py` - Tests for the application
  * `Chat/urls.py` - URL routing for the application
  * `Chat/views.py` - Views for handling HTTP requests
  * `migrations/` - Directory for database migrations
* `templates/` - HTML templates
  * `templates/index.html` - Main chat interface
  * `templates/login.html` - Login page
  * `templates/register.html` - Registration page
* `requirements.txt` - List of dependencies
* `manage.py` - Django's command-line utility

## License

This project is licensed under the MIT License. See the LICENSE file for details.
