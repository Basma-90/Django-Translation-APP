# Django Translation Application

This is a simple Django application that allows users to translate text using the Google Translate API.

## Features

- Translate text from one language to another.
- Support for multiple languages.

## Requirements

- Python 3.x
- Django
- googletrans library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Basma-90/django-translation-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-translation-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Visit the home page to enter the text you want to translate.
2. Choose the source and target languages from the dropdown menus.
3. Click the "Translate" button to see the translated text.
