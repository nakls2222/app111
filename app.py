# Импортируем Flask и функцию для работы с шаблонами
from flask import Flask, render_template

# Создаём экземпляр приложения Flask
app = Flask(__name__)

# Главный маршрут — корень сайта "/"
@app.route('/')
def index():
    # Функция render_template ищет файл index.html в папке templates
    # и возвращает его пользователю
    return render_template('index.html')


# Запуск сервера только при прямом вызове этого файла (не при импорте)
if __name__ == '__main__':
    app.run()