# FAQ System with Multi-Language Support

## Overview

This project is a Django-based FAQ (Frequently Asked Questions) management system that allows storing and managing FAQs in multiple languages. The system supports a WYSIWYG editor for content input, provides automatic translation for multiple languages, and implements caching for performance optimization.

## 🌟 Features

- **FAQ Management**: Create, retrieve, update, and delete FAQs with rich text answers.
- **Multi-Language Support**: FAQs can be translated into different languages using the Google Translate API.
- **Caching**: Uses Redis cache to store frequently accessed translations for performance.
- **WYSIWYG Editor**: Rich text support for both questions and answers.
- **API Endpoints**: Exposes RESTful API endpoints to manage FAQs and retrieve them in different languages.

## 📸 Screenshots

- <img width="1462" alt="Image" src="https://github.com/user-attachments/assets/368354f8-05cc-46fe-b30a-254a3e432ad5" />

- <img width="1460" alt="Image" src="https://github.com/user-attachments/assets/076ea5e7-a1ac-44fa-9da6-e27448de996c" />

- <img width="1464" alt="Image" src="https://github.com/user-attachments/assets/14e6f3c4-1187-45da-8d24-7214fe774e91" />

- <img width="1466" alt="Image" src="https://github.com/user-attachments/assets/935b0922-13d6-4fff-8d62-1df3d49654a2" />

- <img width="1470" alt="Image" src="https://github.com/user-attachments/assets/40cfed58-31c0-46df-b29d-29ae462e3741" />

## 🛠️ Requirements

- Python 3.12.7
- Django 5.1.5
- Django REST Framework 3.15.2
- django-ckeditor 6.7.2
- django-redis 5.4.0
- googletrans 3.1.0a0
- Redis 4.5.5 (for caching)

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ShanuRocky/faq_project.git
    cd faq_project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Redis** (if you don't have it running):
    - You can install Redis by following [this guide](https://redis.io/download).
    - Start Redis server on `127.0.0.1:6379`.

5. **Run migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser** to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

Now the application should be running on `http://localhost:8000/`.

## API Endpoints

### 1. **Create FAQ**
- **Endpoint**: `POST /api/faqs/`
- **Request Body**:
    ```json
    {
        "question": "What is the capital of France?",
        "answer": "The capital of France is <b>Paris</b>."
    }
    ```

### 2. **Retrieve FAQ**
- **Endpoint**: `GET /api/faqs/{id}/`
- **Query Parameters**:
    - `lang`: Optional. Language code (e.g., `en`, `fr`, `es`).
- **Response Body**:
    ```json
    {
        "id": "1",
        "question": "What is the capital of France?",
        "translated_question": "What is the capital of France?",
        "answer": "The capital of France is <b>Paris</b>.",
        "translated_answer": "The capital of France is <b>Paris</b>."
    }
    ```
  
    Example request for French:
    ```
    GET /api/faqs/1/?lang=fr
    ```

### 3. **List FAQs**
- **Endpoint**: `GET /api/faqs/`
- **Query Parameters**:
    - `lang`: Optional. Language code (e.g., `en`, `fr`, `es`).
  
    Example request:
    ```
    GET /api/faqs/?lang=fr
    ```

### 4. **Get Supported Languages**
- **Endpoint**: `GET /api/supported-languages/`
- **Response**:
    ```json
    {
        "supported_languages": ["en", "fr", "es", "de"]
    }
    ```

## Admin Panel

To access the Django admin panel:

1. Navigate to `http://localhost:8000/admin/`.
2. Log in with the superuser credentials you created during the setup.
3. You will be able to view, add, edit, and delete FAQs.

## Testing

To test the API, you can use the provided `tests.py` script.

### Running the Test Script
1. Ensure the Django server is running.
2. Run the test script:
    ```bash
    python faq_app/tests.py
    ```

The script will perform the following actions:
- Retrieve supported languages.
- Create a new FAQ.
- Retrieve the FAQ in multiple languages.
- List FAQs in different languages.

## Cache Configuration

The project uses Redis to cache FAQ translations. You can configure Redis in the `settings.py` file under `CACHES`.

Example Redis configuration:

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

--- 
## Use Docker to Set Up the Project

---
### **Setup Instructions**
1. **Clone the repository**  
   ```sh
   git clone <your-github-repo-url>
   cd <your-project-folder>
   ```
2. **change the settings.py**
```
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://host.docker.internal:6379/1',  # to run on docker
        # 'LOCATION': 'redis://127.0.0.1:6379/1' ,   # to run host machine
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}
```
3. **Build Docker images**  
   ```sh
   docker-compose build
   ```

4. **Start the containers**  
   ```sh
   docker-compose up 
   ```

5. **Verify running containers**  
   ```sh
   docker ps
   ```

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Django
- Django REST Framework
- Google Translate
- CKEditor
- Redis