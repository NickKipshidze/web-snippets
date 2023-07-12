import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import QTimer
import requests

class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setLayout(qtw.QVBoxLayout())
        
        self.draw()
        
        self.comments: list = []
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_comments)
        self.timer.start(1000)
        
        self.show()
    
    def update_comments(self) -> None:
        new_comments: list = requests.get("http://127.0.0.1:8000/comments").json()
        
        if len(new_comments) > len(self.comments):
            new_comments = new_comments[len(self.comments):]
            
            for comment in new_comments:
                self.comments.append(comment)
                self.comments_container.layout().addWidget(
                    qtw.QLabel(comment["author"] + " - " + comment["content"])
                )
    
    def new_comment(self) -> None:
        comment: dict = {
            "author": self.name_input.text(), 
            "content": self.comment_input.text()
        }
        
        self.comment_input.setText("")
        
        requests.post("http://127.0.0.1:8000/comments/new", json=comment)
    
    def draw(self) -> None:
        self.comments_container = qtw.QWidget()
        self.comments_container.setLayout(qtw.QVBoxLayout())
        
        self.comment_input = qtw.QLineEdit()
        self.comment_input.returnPressed.connect(self.new_comment)
        self.name_input = qtw.QLineEdit()
        
        self.layout().addWidget(self.comments_container)
        
        self.layout().addWidget(self.comment_input)
        self.layout().addWidget(self.name_input)
        
if __name__ == "__main__":
    app = qtw.QApplication([])
    
    main_window = MainWindow()
    
    app.exec()