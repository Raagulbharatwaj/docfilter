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
    new_name = name.split('.')[0]+"_removed.csv"
    with open(fs.path(name),'r') as f1 ,open(fs.path(new_name),'a') as f2:
        reader = csv.reader(f1)
        writer = csv.writer(f2)
        count = 0
        for row in reader:
            if count==0:
                row.append("Result")
                writer.writerow(row)
                count+=1
            else:
                flag = False
                for item in row:
                    for keyword in keywords:
                        if keyword in item:
                            flag = True
                            break
                if flag:
                    row.append("KEYWORD PRESENT")
                    writer.writerow(row)
                else:
                    row.append("NO KEYWORD FOUND")
                    writer.writerow(row)
    return new_name


