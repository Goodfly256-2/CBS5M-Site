# Импортируем ваш объект Flask (app) из вашего главного файла (например, main.py)
from app import app as application

# Теперь у нас есть переменная 'application', которую понимает Gunicorn
if __name__ == "__main__":
    application.run()
