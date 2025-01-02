
# DjangoBlogWeb
# Django Personal Blog

A simple yet powerful personal blog built with Django. Features a clean interface for readers and a user-friendly admin section for managing articles.

## Features

### Guest Section
- **Home Page:** Browse all published articles
- **Article Page:** Read full articles with publication dates
- **Responsive Design:** Mobile-friendly interface

### Admin Section
- **Dashboard:** Manage all your articles
- **Article Management:** Create, edit, and delete articles
- **Secure Authentication:** Protected admin area
- **Rich Text Editor:** Write articles in markdown format

## Technology Stack

- Python 3.x
- Django 4.x
- SQLite (default database)
- HTML/CSS
- Django Template Language

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Apply migrations:
```bash
python manage.py makemigrations
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

7. Visit http://127.0.0.1:8000 in your browser

## Project Structure

```
django-blog/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── article_detail.html
│   │       ├── dashboard.html
│   │       ├── article_form.html
│   │       └── login.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Usage

### For Readers
1. Visit the homepage to see all articles
2. Click on any article title to read the full content

### For Admins
1. Go to /login/ and enter your credentials
2. Access the dashboard to manage articles
3. Create new articles using the "Add New Article" button
4. Edit or delete existing articles from the dashboard

## Article Management

### Creating an Article
1. Log in to the admin section
2. Click "Add New Article"
3. Fill in:
   - Title
   - Content
   - Publication date
4. Click "Save"

### Editing an Article
1. Go to the dashboard
2. Find the article you want to edit
3. Click "Edit"
4. Make your changes
5. Click "Save"

## Security Features

- Session-based authentication
- CSRF protection
- Secure password hashing
- Protected admin routes

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - Rajesh Basnet


## Acknowledgments

- Django Documentation
- Django Community
- Contributors and users of this project
