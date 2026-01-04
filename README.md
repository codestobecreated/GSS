# GSS CAR Makeovers

Premium automotive makeover services website built with Django.

## Features

- **Home Page**: Showcase services and latest projects
- **Services**: Detailed service offerings (Ceramic Coating, PPF, Wraps, Interior Customization)
- **Gallery**: Filterable project portfolio
- **About**: Company information
- **Contact**: Inquiry form with booking functionality

## Tech Stack

- **Backend**: Django 6.0
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Deployment**: Render
- **Static Files**: WhiteNoise

## Local Development

### Prerequisites

- Python 3.10+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/codestobecreated/GSS.git
cd GSS
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Deployment to Render

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/codestobecreated/GSS.git
git push -u origin main
```

### 2. Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `gss-car-makeovers`
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn gss_car_makeovers.wsgi:application`
   - **Instance Type**: Free

5. Add Environment Variables:
   - `SECRET_KEY`: (generate a new secret key)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com`
   - `DATABASE_URL`: (Render will auto-populate if you add PostgreSQL)

6. Click "Create Web Service"

### 3. Add PostgreSQL Database (Optional)

1. In Render Dashboard, click "New +" → "PostgreSQL"
2. Create database
3. Link it to your web service
4. Render will automatically set `DATABASE_URL`

## Environment Variables

Create a `.env` file for local development:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## Project Structure

```
GSS/
├── core/                   # Main app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Forms
│   └── urls.py            # URL patterns
├── gss_car_makeovers/     # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL config
│   └── wsgi.py            # WSGI config
├── static/                # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── gallery.html
│   └── ...
├── build.sh              # Render build script
├── requirements.txt      # Python dependencies
└── manage.py            # Django management
```

## License

All rights reserved © 2026 GSS CAR Makeovers

## Contact

For inquiries: info@gsscar.com
