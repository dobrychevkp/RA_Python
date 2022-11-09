from PySide6.QtCore import Slot

# NOTE: Для работы с БД возьмём QtSql. https://doc.qt.io/qtforpython-6.2/PySide6/QtSql/index.html
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QTableView,
    QLabel, QWidget, QPushButton,
    QFileDialog,
)

from AddEntryDialog import AddEntryDialog


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # NOTE: Настраиваем внешний вид компонентов окна (виджетов).
        self.setWindowTitle('Desktop application')

        self.__label = QLabel('Collection', self)

        self.__open_button = QPushButton('Open', self)
        self.__open_button.setToolTip('Choose the collection database')

        self.__add_button = QPushButton('Add', self)
        self.__add_button.setToolTip('Add a new entry into the collection')

        self.__model = None
        self.__view = QTableView(self)

        # NOTE: Компонуем метку и кнопки по горизонтали.
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.__label)
        horizontal_layout.addWidget(self.__open_button)
        horizontal_layout.addWidget(self.__add_button)

        # NOTE: Компонуем предыдущую компоновку и таблицу по вертикали.
        layout = QVBoxLayout()
        layout.addLayout(horizontal_layout)
        layout.addWidget(self.__view)

        self.setLayout(layout)

        # NOTE: Соединяем нужные сигналы нужных виджетов с соответствующими слотами.
        self.__open_button.clicked.connect(self.__open_collection)
        self.__add_button.clicked.connect(self.__add_new_entry)

    @Slot()
    def __open_collection(self):
        # NOTE: Вызываем диалоговое окно выбора файла (БД sqlite).
        collection, _ = QFileDialog.getOpenFileName(parent=self)

        # NOTE: Подключаемся к БД.
        self._db = QSqlDatabase.addDatabase('QSQLITE')
        self._db.setDatabaseName(collection)
        self._db.open()

        # NOTE: В качестве табличной модели используем БД.
        self.__model: QSqlTableModel = QSqlTableModel(self, self._db)
        self.__model.setTable('objects')
        self.__model.select()

        self.__view.setModel(self.__model)

    @Slot()
    def __add_new_entry(self):
        dialog = AddEntryDialog(self)

        # NOTE: Модальное диалоговое окно имеет свой цикл обработки событий.
        if dialog.exec_() == AddEntryDialog.Accepted:
            row = self.__model.rowCount()

            # NOTE: Добавляем новую строку в конец таблицы.
            self.__model.insertRow(row)

            # NOTE: Наполняем её данными.
            self.__model.setData(self.__model.index(row, 0), dialog.entry.original)
            self.__model.setData(self.__model.index(row, 1), dialog.entry.translation)
            self.__model.setData(self.__model.index(row, 2), dialog.entry.transcription)

            # NOTE: Сохраняем изменения в БД.
            self.__model.submitAll()
