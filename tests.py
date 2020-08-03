import photo_reader as PR
import file_searcher as FS
import PDF_Maker as PDF
import KivyMain as MainWindow
import gui_selectionwindow as guis

test_src = "samples/sample1.jpg"
test_src2 = 'samples/'

#test objects

#img = PR.Photo_Reader(test_src)
#img.raport()

#fl = FS.File_Searcher(test_src2)
#fl.raport()

#for image in fl.images:
#    image.raport()

#PDF.PDF_Maker(test_src2,"test")
#MainWindow.Editor()

guis.Gui_selectionwindow("Test prompt","Test string info","Test button",200,200)