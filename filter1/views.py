from http.client import HTTPResponse
from django.shortcuts import render
from filter1.utils import handle_uploaded_file
from django.core.files.storage import FileSystemStorage

def home_page(request):
    context = {}
    if request.method=='POST':
        text = request.POST["keywords"]
        keywords = text.split()
        uploaded_file = request.FILES["file1"]
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context["url"] = fs.url(name)
        #handle_uploaded_file(uploaded_file,keywords)
        return render(request,"home.html",context)
    return render(request,"home.html")
