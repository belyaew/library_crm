from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from services.BookService import add_book
from ui.AuthUi import LoginWidget


# Определение класса, отображающего окно добавления книги
class AddBookWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.title_input = QLineEdit()
        self.author_id_input = QLineEdit()
        self.category_id_input = QLineEdit()
        self.category_id_input = QLineEdit()
        add_button = QPushButton("Add Book")

        add_button.clicked.connect(self.add_book_clicked)

        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Author ID:"))
        layout.addWidget(self.author_id_input)
        layout.addWidget(QLabel("Category ID:"))
        layout.addWidget(self.category_id_input)
        layout.addWidget(add_button)

    # Обработчик нажатия кнопки добавления книги
    def add_book_clicked(self):
        title = self.title_input.text()
        author = int(self.author_id_input.text())
        category_id = int(self.category_id_input.text())
        add_book(title, author, category_id)


# Функция для создания интерфейса и запуска приложения
def create_ui():
    app = QApplication([])
    window = LoginWidget()
    # window = AddBookWindow()
    window.show()
    app.exec_()
