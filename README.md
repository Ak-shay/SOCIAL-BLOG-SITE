# SOCIAL-BLOG-SITE

## Installation
1. Clone or download the repository.
    ```bash
    git clone https://github.com/Ak-shay/SOCIAL-BLOG-SITE.git
    ```
2. Create a new virtual environment for the project.
    ```bash
    python -m venv myvenv
    source myvenv/bin/activate
    ```
3. Install required python libraries giving in the requirements.txt file.
    ```bash
    pip install -r requirements.txt
    ```
4. Create `.env` file in your project folder(in the same directory that contain manage.py).
5. Write your environment variables in `.env` file.
	```bash
	SECRET_KEY="YOUR_SECRET"
	DEBUG=False(default)
	EMAIL_HOST="smtp.gmail.com"(default)
	EMAIL_PORT=25(default)
	EMAIL_HOST_PASSWORD="YOUR-GOOGLE-APP-PSWD"
	EMAIL_HOST_USER="YOUR-EMAIL-ADDRESS"
	```
6. Run Django migrations.
	```bash
	python manage.py makemigrations
	python manage.py migrate
	```
7. Create a superuser(admin).
	```bash
	python manage.py createsuperuser
	```
8. Start the application.
	```bash
	python manage.py runserver
	```
9. Login with your django credentials(as a admin).
	```bash
	http://127.0.0.1:8000/admin/
	```
10. Go to `http://127.0.0.1:8000/admin/sites/site/` and add `site`.
	```bash
	Domain name: 127.0.0.1
	Display name: (any)
	``` 
10. Go to `http://127.0.0.1:8000/admin/socialaccount/socialapp/` and add social application.
	```bash
	Provider: Google
	Name: -any-
	Client id: YOUR-CLIENT-ID
	Client secret: YOUR-CLIENT-SECRET
	Sites: 127.0.0.1:8000
	```
	Create your Google credentials from `https://console.developers.google.com/`
	Set Authorized redirect URIs as:
	`http://127.0.0.1:8000/accounts/google/login/callback/`
11. You are done with installation.
	Run application at `http://127.0.0.0:8000/`