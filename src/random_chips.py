import sys
import random
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QPen
from src.playing_chip import PlayingChip


class RandomChips(QWidget):
    def __init__(self, parent, height, width, diameter, count):
        super().__init__(parent)
        self.count = count
        self.setGeometry(100, 100, width, height)  # Здесь задается размер окна

        self.height_ = height
        self.width_ = width
        self.diameter = diameter
        self.generating_chips(self.count)

    def generating_chips(self, count):
        for child in self.findChildren(PlayingChip):
            child.deleteLater()
        # Генерация случайных позиций для фишек
        if count > (self.width_ - self.diameter) or count > (self.height_ - self.diameter):
            # print("Слишком много фишек для указанного размера области!")
            return
        
        x_pos = random.sample(range(0, self.width_ - self.diameter), count)
        y_pos = random.sample(range(0, self.height_ - self.diameter), count)

        for i in range(count):
            chip = PlayingChip(self, '', self.diameter)
            chip.move(x_pos[i], y_pos[i])
            chip.show()
        
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(0, 0, 0, 100), 2))
        painter.drawRect(1, 1, self.width_ - 1, self.height_ - 1)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomChips(85, 85, 10, 50)
    window.show()
    sys.exit(app.exec())
