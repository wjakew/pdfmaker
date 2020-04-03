import PDF_Maker as PDMaker
import sys
import os

version = "v 1.0.0"
date = "04.2020"

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

# wykonywanie programu z linii polecen
if  len(sys.argv) == 3:

    # przepisanie danych z konsoli do programu
    catalog_path = str(sys.argv[1])
    pdf_name = str(sys.argv[2])

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
    print("Opening graphical interface - to be added")
    print("Type 'python3 main.py help' for further instructions")



