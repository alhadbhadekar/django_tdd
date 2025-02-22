# Django Blogs Project

## Overview

This project is a simple blogging application built using Django, following Test-Driven Development (TDD) principles. The goal is to create a robust, maintainable, and scalable blog platform.

## Features

- User authentication (registration, login, logout)
- Create, read, update, and delete blog posts
- Comment on blog posts
- User profiles
- Basic admin interface for managing posts and comments

## Technologies Used

- Python
- Django
- SQLite (for development)
- Bootstrap (for styling)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/alhadbhadekar/django_tdd.git
   cd django-blogs
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django documentation
- TDD principles

Enjoy building and blogging!
