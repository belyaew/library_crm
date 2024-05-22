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
        self.place_pub_input = QLineEdit()
        self.publisher_input = QLineEdit()
        self.release_date_input = QLineEdit()
        self.page_count_input = QLineEdit()
        self.isbn_input = QLineEdit()
        add_button = QPushButton("Add Book")

        add_button.clicked.connect(self.add_book_clicked)

        layout.addWidget(QLabel("Название:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("ФИО автора:"))
        layout.addWidget(self.author_id_input)
        layout.addWidget(QLabel("Место издания:"))
        layout.addWidget(self.place_pub_input)
        layout.addWidget(QLabel("Издатель:"))
        layout.addWidget(self.publisher_input)
        layout.addWidget(QLabel("Год издания:"))
        layout.addWidget(self.release_date_input)
        layout.addWidget(QLabel("Количество страниц:"))
        layout.addWidget(self.page_count_input)
        layout.addWidget(QLabel("ISBN:"))
        layout.addWidget(self.isbn_input_input)
        layout.addWidget(QLabel("Category ID:"))
        layout.addWidget(self.category_id_input)
        layout.addWidget(add_button)

    # Обработчик нажатия кнопки добавления книги
    def add_book_clicked(self):
        title = self.title_input.text()
        author = int(self.author_id_input.text())
        category_id = int(self.category_id_input.text())
        place_pub = int(self.place_pub_input.text())
        publisher = int(self.publisher_input.text())
        release_date = int(self.release_date_input.text())
        page_count = int(self.page_count_input.text())
        isbn_input = int(self.isbn_input_input.text())
        add_book(title, author, release_date, category_id, place_pub, publisher, page_count, isbn_input)


# Функция для создания интерфейса и запуска приложения
def create_ui():
    app = QApplication([])
    window = LoginWidget()
    # window = AddBookWindow()
    window.show()
    app.exec_()
