import sys

from PySide2 import QtGui, QtCore, QtSvg,QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout,QPushButton




class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        renderer = QtSvg.QSvgRenderer('/home/enes/Downloads/svg_example-main/icons8-home.svg')        
        self.orig_svg = QtGui.QImage(500, 500, QtGui.QImage.Format_ARGB32)
        self.pushButton = QPushButton("")
        painter = QtGui.QPainter(self.orig_svg)
        renderer.render(painter)

        pixmap = QtGui.QPixmap.fromImage( self.orig_svg )
        self.pushButton.setIcon(QIcon(pixmap))

        renderer_3 = QtSvg.QSvgRenderer('/home/enes/Downloads/svg_example-main/icons8-settings.svg')        
        self.orig_svg_3 = QtGui.QImage(500, 500, QtGui.QImage.Format_ARGB32)    
        self.pushButton_3 = QtWidgets.QPushButton("")
        painter_3 = QtGui.QPainter(self.orig_svg_3)
        renderer_3.render(painter_3)

        pixmap_3 = QtGui.QPixmap.fromImage( self.orig_svg_3 )
        self.pushButton_3.setIcon(QIcon(pixmap_3))

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)

        layout.addWidget(self.pushButton)
        layout.addWidget(self.pushButton_3)
        self.setLayout(layout)
    
    @QtCore.Slot()
    def pushButton_clicked(self):
        self.new_image = self.orig_svg.copy()

        self.paint = QtGui.QPainter()
        self.paint.begin( self.new_image )
        self.paint.setCompositionMode( QtGui.QPainter.CompositionMode_SourceIn )
        self.paint.fillRect( self.new_image.rect(), QtGui.QColor( 255, 0, 0) )
        self.paint.end()
        self.pushButton.setIcon( QtGui.QPixmap.fromImage(self.new_image) )
        
        self.new_image_3 = self.orig_svg_3.copy()

        self.paint_3 = QtGui.QPainter()
        self.paint_3.begin( self.new_image_3 )
        self.paint_3.setCompositionMode( QtGui.QPainter.CompositionMode_SourceIn )
        self.paint_3.fillRect( self.new_image_3.rect(), QtGui.QColor( 0, 0, 0 ) )

        self.paint_3.end()
        self.pushButton_3.setIcon( QtGui.QPixmap.fromImage(self.new_image_3) )
    
    @QtCore.Slot()
    def pushButton_3_clicked(self):
        self.new_image_3 = self.orig_svg_3.copy()

        self.paint_3 = QtGui.QPainter()
        self.paint_3.begin( self.new_image_3 )
        self.paint_3.setCompositionMode( QtGui.QPainter.CompositionMode_SourceIn )
        self.paint_3.fillRect( self.new_image_3.rect(), QtGui.QColor( 255, 0, 0) )

        self.paint_3.end()
        self.pushButton_3.setIcon( QtGui.QPixmap.fromImage(self.new_image_3) )

        self.new_image = self.orig_svg.copy()

        self.paint = QtGui.QPainter()
        self.paint.begin( self.new_image )
        self.paint.setCompositionMode( QtGui.QPainter.CompositionMode_SourceIn )
        self.paint.fillRect( self.new_image.rect(), QtGui.QColor( 0, 0, 0 ) )
        self.paint.end()
        self.pushButton.setIcon( QtGui.QPixmap.fromImage(self.new_image) )
        


app = QApplication(sys.argv)
window = Form()
window.show()
sys.exit(app.exec_())
