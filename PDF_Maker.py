import file_searcher as FS

#klasa tworzaca obietk tworzacy pdfa ze zdjec z podanego katalogu
class PDF_Maker:

    def __init__(self, catalog_path, pdf_name):
        
        self.images = FS.File_Searcher(catalog_path) #lista obiektow Photo_Reader

        self.make(pdf_name)

    def make(self, name):
        img_list = []   # inicjalizacja listy zawierajacej wszystkie zdjecia niezbedne do pdfa

        # kopiowanie z obiektu do listy
        for image in self.images.images:
            img_list.append(image.im)
        im1 = img_list[0]
        img_list.remove(im1)
        im1.save(self.images.path+name+".pdf",save_all = True,append_images = img_list)

