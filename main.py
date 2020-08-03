import PDF_Maker as PDMaker
import gui
import gui_selectionwindow as guis
import sys
import os

version = "v 1.1.0"
date = "08.2020"

catalog_path = ""
pdf_name = ""

spaces = int(os.get_terminal_size().columns)
header1 = "PDF_MAKER "+version
header2 = "by Jakub Wawak"

# welcome text
welcome1 = header1.center(spaces)# - len(header1))
welcome2 = header2.center(spaces)# - len(header2))
print(welcome1)
print(welcome2)
print("")

def run(string_path,string_pdf_name):
    # przepisanie danych z konsoli do programu
    catalog_path = string_path
    pdf_name = string_pdf_name

    # pierwsze sprawdzenie czy nazwa sciezki konczy sie prawidlowo
    # i ewentualna korekcja
    if catalog_path.endswith("/") == False:
        catalog_path = catalog_path + "/"

    # echo info
    print(("Source: "+catalog_path).center(spaces))
    print(("Future pdf name: "+pdf_name+".pdf").center(spaces))

    if os.path.exists(catalog_path) == False:
        print("Path doesnt exist".center(spaces))

    else:
        pdf = PDMaker.PDF_Maker(catalog_path,pdf_name)
        for line in pdf.images.log:
            print(line)

# wykonywanie programu z linii polecen
if  len(sys.argv) == 3:
    catalog_path = str(sys.argv[1])
    pdf_name = str(sys.argv[2])
    run(catalog_path,pdf_name)

# wyswietlanie help
elif len(sys.argv) == 2 and sys.argv[1] == "help":
    print("Help".center(spaces))
    print("")
    print("python3 main.py path name_of_the_file")
    print("")
    print("Arguments:")
    print("path - source path to your catalog with photos")
    print("name_of_the_file - name of the pdf file that program will create ")
    print("WARNING!")
    print("Remember to not include '.pdf' at the end of the name of the file")
    print("")
    print("example: python3 main.py samples/ test")
    print("")
    print("Program made by JAKUB WAWAK".center(spaces))
    print("kubawawak@gmail.com".center(spaces))
    print((version + " " + date).center(spaces))
# wykonywanie programu z gui
else:
    main_window = gui.GUI()

    if ( main_window.flag ):
        #input_window = guis.Gui_selectionwindow("Test prompt","Test string info","Test button",200,200)
        name = input("PDF file name:")
        if name != "":
            ans = input("Are you sure to use this data? (y/n)")
            if ans == "y":
                print("Data saved")
                run(main_window.file_path,name)
            else:
                print("Procedure cancelled")
        else:
            print("Name is empty")
            print("Procedure cancelled")




