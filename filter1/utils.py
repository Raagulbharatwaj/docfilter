import csv
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
def handle_uploaded_file(file,keywords):
    fs = FileSystemStorage()
    name = fs.save(file.name,file)
    file_path = fs.path(name)
    path = file_path.split('\\')
    path.pop(-1)
    folder_path = ""
    for i in path:
        folder_path+=f"{i}\\"
    new_name_1 = name.split('.')[0]+"_keywords_present.csv"
    new_name_2 = name.split('.')[0]+"_keywords_removed.csv"
    with open(fs.path(name),'r') as f1 ,open(fs.path(new_name_1),'a') as f2,open(fs.path(new_name_2),'a') as f3:
        reader  = csv.reader(f1)
        writer1 = csv.writer(f2)
        writer2 = csv.writer(f3)
        count = 0
        for row in reader:
            string = " ".join(row)
            if count==0:
                writer1.writerow(row)
                writer2.writerow(row)
                count+=1
            else:
                flag = False
                for keyword in keywords:
                    if keyword in string:
                        flag = True
                        writer1.writerow(row)
                        break
                if flag==False:
                    writer2.writerow(row)
    return (new_name_1,new_name_2)

