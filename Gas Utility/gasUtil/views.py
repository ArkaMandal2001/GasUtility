from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'base.html',{'heading':'Home Page'})
def download(request,reqId):
    fs = FileSystemStorage()
    all_files=fs.listdir("")
    for file in all_files[1]:
        if file.split('.')[0]=="file_"+str(reqId):
            file_name=file
            break
    response = HttpResponse(fs.open(file_name, 'rb').read())
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename='+file_name
    return response