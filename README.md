# SnipBox

SnipBox is a short note-saving application that allows users to save short text snippets with a title, note, timestamp, and tags. Tags can be reused across multiple snippets, and the application uses JWT for authentication.

## Features

- User registration and authentication using JWT.
- Save snippets with a title, note, created and updated timestamps, and associated tags.
- Tags are unique and can be reused across multiple snippets.

## Technologies

- Django
- Django Rest Framework
- JWT (JSON Web Tokens)

## Setup and Installation

### Prerequisites

- Python 3
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/shadow7788/SnipBox.git
    cd SnipBox/SnipBox
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m virtualenv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```sh
    python manage.py migrate
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```sh
    python manage.py runserver
    ```
