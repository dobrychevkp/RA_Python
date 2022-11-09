from PySide6.QtCore import Slot, Qt, QAbstractTableModel, QModelIndex, QTimer

from NoteApiProvider import NoteApiProvider


# NOTE: Реализуем свою модель заметок. https://doc.qt.io/qtforpython/PySide6/QtCore/QAbstractItemModel.html
class NoteTableModel(QAbstractTableModel):
    """Табличная модель заметок с автоматическим обновлением."""

    __update_timeout = 10_000
    __columns = ['author', 'message']

    def __init__(self, provider, parent=None):
        super().__init__(parent)
        self.__api: NoteApiProvider = provider

        # NOTE: Храним заметки просто в списке.
        self.__notes = []

        # NOTE: Таймер. https://doc.qt.io/qtforpython/PySide6/QtCore/QTimer.html
        self.__timer = QTimer(self)

        # NOTE: Будем обновлять модель по таймауту.
        self.__timer.timeout.connect(self.update_model)

        self.__timer.start(self.__update_timeout)
        self.update_model()

    def columnCount(self, parent=QModelIndex()) -> int:
        # NOTE: Кол-во столбцов таблицы (знаем заранее, сами задали).
        return len(self.__columns)

    def rowCount(self, parent=QModelIndex()) -> int:
        # NOTE: Кол-во строк таблицы (совпадает с размером списка заметок).
        return len(self.__notes)

    def data(self, index, role=Qt.DisplayRole):
        # NOTE: DisplayRole определяет текст в ячейке. https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum
        if role == Qt.DisplayRole:
            row, column = index.row(), index.column()

            if row < self.rowCount() and column < self.columnCount():
                return self.__get_display_data(row, column)

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # NOTE: Показываем горизонтальный заголовок таблицы.
        return self.__columns[section] \
                if orientation == Qt.Horizontal and role == Qt.DisplayRole \
                else None

    @Slot()
    def update_model(self):
        notes = self.__api.get_notes()

        if notes != self.__notes:
            # WARNING: Обновляем модель строго в блоке begin/end.
            self.beginResetModel()
            self.__notes = notes
            self.endResetModel()

    def __get_display_data(self, row: int, column: int) -> str:
        return self.__notes[row][self.__columns[column]]
