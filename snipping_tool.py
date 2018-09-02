import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PIL import ImageGrab


class SnippingTool(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		screen_width, screen_height = ImageGrab.grab().size
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

	def get_captured_coords(self):
		x1 = min(self.begin.x(), self.end.x())
		y1 = min(self.begin.y(), self.end.y())
		x2 = max(self.begin.x(), self.end.x())
		y2 = max(self.begin.y(), self.end.y())
		return x1, y1, x2, y2


def main():
	app = QtWidgets.QApplication(sys.argv)
	st = SnippingTool()
	st.show()
	app.exec_()
	app.quit()
	print(st.get_captured_coords())


if __name__ == '__main__':
	main()
