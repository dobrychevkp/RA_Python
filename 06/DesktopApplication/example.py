import sys

from PySide6.QtWidgets import QApplication

from Window import Window

if __name__ == '__main__':
    # NOTE: Создаём объект приложения.
    app = QApplication(sys.argv)

    # NOTE: Создаём и показываем окно.
    window = Window()
    window.show()

    # NOTE: Запускаем цикл обработки событий (завершается после закрытия последнего окна).
    sys.exit(app.exec())
