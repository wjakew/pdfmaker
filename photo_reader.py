from PIL import Image

# klasa Photo_Reader
# tworzy obiekt zawierajacy jedno zdjecie

class Photo_Reader:

    # metoda __init__
    # metoda buduje obiekt
    # (self,src):
    #   - src - string - konkretna sciezka dostepu do zdjecia
    def __init__(self,src):
        self.photo_src = src    # przekopiowanie sciezki dostepu do pliku
        self.open_image()       # otwiera zdjecie w obiekcie Image biblioteki PIL
    
        # przygotowanie do stworzenia pdf
        self.im.convert('RGB')  # ustawienie jednej przestrzeni barw
        


    # metoda raport
    # metoda dostarcza informacje o pliku
    def raport(self):
        print("Object src: "+ self.photo_src)
        print("Details: "+str(self.im.format)+","+str(self.im.size)+","+str(self.im.mode))
    
    # metoda open_image
    # metoda tworzy obiekt Image biblioteki Pillow
    def open_image(self):
        self.im = Image.open(self.photo_src)    # obiekt typu Image zawierajacy zdjecia
