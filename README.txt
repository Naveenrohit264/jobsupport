SETUP INSTRUCTIONS

1. Install Python
2. Install MySQL
3. Create database:
   CREATE DATABASE jobsupport;

4. Open terminal inside project folder

5. Install packages:
   pip install -r requirements.txt

6. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

7. Start server:
   python manage.py runserver

8. Open:
   http://127.0.0.1:8000
