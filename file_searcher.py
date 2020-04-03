import os
import photo_reader as PR


# klasa File_Searcher
# umozliwia utworzenie obiektu zawierajacego 
# wszystkie zdjecia z podanego katalogu
class File_Searcher:

    def __init__(self,path):
        self.path = path
        self.counter = 0    # licznik zawierajacy ilosc plikow jpg w folderze
        self.photo_src_list = []    # lista zawierajaca wszystkie sciezki dostepu do katalogu
        self.entries = os.listdir(path)     # surowe dane dotyczace nazw plikow w podanej path
        self.path = path    # kopia sciezki dostepu do katalogu
        self.find_photos()  # metoda szukajaca i zwracajaca liste sciezek dostepu do zdjec

        # w tym momencie mamy wszystkie sciezki dostepu do plikow 
        # znajdujacych sie pod wskazana sciezka

        self.images = []    # lista obietkow typu Photo_Reader
        self.load_images()  # zaladowanie zdjec jako obiekty Photo_Reader

        # obiekty do logu
        self.log = []
        self.raport()

    # metoda informujaca o dzialaniu obiektu
    def raport(self):
        self.log.append("Operation log:")
        self.log.append("")
        self.log.append("JPG Files number: "+str(self.counter))
        self.log.append("")
        self.log.append("List of sources:")
        for element in self.photo_src_list:
            self.log.append(element)
        self.log.append("")
        self.log.append("Log ended.")
    
    # metoda znajduje i zwraca do obiektu typu lista 
    # liste SCIEZEK DOSTEPU do zdjec
    def find_photos(self):
        for obj in self.entries:
            if(len(obj)>3):
                if obj[len(obj)-3:] == "jpg":
                    self.counter = self.counter + 1
                    self.photo_src_list.append(self.path+obj)

        # sortowanie po nazwie ( wazne w moim zinowym nazewnictwie)
        self.photo_src_list.sort()

    # metoda tworzy obiekty typu Photo_Reader 
    # i zapisuje je w obiekcie images typu lista 
    def load_images(self):
        for file_path in self.photo_src_list:
            try:
                self.images.append(PR.Photo_Reader(file_path))  #dodajemy kazde znalezione zdjecie
            except:
                print("FS - Problem occured: "+file_path)

                    




