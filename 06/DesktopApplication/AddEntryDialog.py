from dataclasses import dataclass

from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QDialog, QLabel, QLineEdit, QDialogButtonBox


@dataclass
class Entry:
    original: str
    translation: str
    transcription: str


class AddEntryDialog(QDialog):
    """Диалог добавления новой записи."""

    def __init__(self, parent=None):
        super(AddEntryDialog, self).__init__(parent)

        self.entry = None

        self.setWindowTitle('Add new entry')

        self._original_label = QLabel('original', self)
        self._original_edit = QLineEdit(self)

        self._translation_label = QLabel('translation', self)
        self._translation_edit = QLineEdit(self)

        self._transcription_label = QLabel('transcription', self)
        self._transcription_edit = QLineEdit(self)

        self._button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            parent=self
        )

        # NOTE: Компонуем элементы формы по сетке.
        grid_layout = QGridLayout()
        grid_layout.addWidget(self._original_label, 0, 0)
        grid_layout.addWidget(self._original_edit, 0, 1)
        grid_layout.addWidget(self._translation_label, 1, 0)
        grid_layout.addWidget(self._translation_edit, 1, 1)
        grid_layout.addWidget(self._transcription_label, 2, 0)
        grid_layout.addWidget(self._transcription_edit, 2, 1)

        layout = QVBoxLayout()
        layout.addLayout(grid_layout)
        layout.addWidget(self._button_box)

        self.setLayout(layout)

        # NOTE: Нажатие "OK".
        self._button_box.accepted.connect(self.accept)

        # NOTE: Нажатие "Cancel".
        self._button_box.rejected.connect(self.reject)

    def accept(self):
        self.entry = Entry(
            self._original_edit.text(),
            self._translation_edit.text(),
            self._transcription_edit.text()
        )

        super().accept()
