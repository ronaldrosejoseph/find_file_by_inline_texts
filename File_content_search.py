import os

#path is like C:/QA/ folders seperated by /
main_path = "path of the directory"
main_path = main_path if main_path[-1] == '/' else main_path + '/'

find_in_line = ["Follow", "on"]
find_in_page = []

def readfiles(path):
    files = os.listdir(path)
    store = open("Files.txt", "a")
    for file in files:
        if not os.path.isdir(path + file):
            try:
                with open(path + file, "r") as f:
                    lines = f.readlines()
                    contents = ""
                    count = 0
                    for line in lines:
                        count += 1
                        check = 0
                        for item in find_in_line:
                            check += 1 if item in line else 0
                          #  check += 1 if item in line and (".js" in line or ".css" in line or ".html" in line) else 0
                              
                        contents += line
                        if check == len(find_in_line) > 0:
                            #print("Found words in the line of \n" + path + file + '\nLine is: ' + str(count), line + '\n')
                            store.write('File name: ' + path + file + '\nLine is: ' + str(count) + line)
                    check = 0
                    for item in find_in_page:
                        check += 1 if item in contents else 0
                    if check == len(find_in_page) > 0:
                        print("Found words in the page of \n" + path + file + '\nPage is:\n' + contents + '\n')
            except Exception as e:
                break_line = "--------------------------------------------------------------------------------"
                print("\n" + break_line + "\n" + str(e))
                print("File not readable " + path + file + "\n" + break_line + "\n")
        else:
            readfiles(path + file + '/')

        store.close()
            
readfiles(main_path)

        

