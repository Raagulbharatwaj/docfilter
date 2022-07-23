import csv
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
def handle_uploaded_file(file,keywords):
    fs = FileSystemStorage()
    name = fs.save(file.name,file)
    with open(fs.path(name),'r') as f:
        reader = csv.reader(f)
        next(reader)
        content = []
        for row in reader:
            content.append(" ".join([strs for strs in row]))
        print(content)
    with open(fs.path(name),'r') as f1 ,open(fs.path(name)+"removed",'a') as f2:
        reader = csv.reader(f1)
        writer = csv.writer(f2)
        count = 0
        for row in reader:
            if count==0:
                row.append("Result")
                writer.writerow(row)
            else:
                writer.writerow(row.append("hello"))
    print("success")
    return name


