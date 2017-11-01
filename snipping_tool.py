import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk


class SnippingTool(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 2))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()


def capture():
    app = QtWidgets.QApplication(sys.argv)
    st = SnippingTool()
    st.show()
    # print(dir(app))
    app.exec_()
    # app.quit()

    x1 = min(st.begin.x(), st.end.x())
    y1 = min(st.begin.y(), st.end.y())
    x2 = max(st.begin.x(), st.end.x())
    y2 = max(st.begin.y(), st.end.y())

    return x1, y1, x2, y2


if __name__ == '__main__':
    print(capture())
