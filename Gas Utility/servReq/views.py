from django.shortcuts import render,HttpResponse
from servReq.models import Request
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    if(request.method=='POST'):
        name=request.POST['name']
        mobno=request.POST['mobno']
        reqType=request.POST['reqType']
        desc=request.POST['desc']
        req=Request(name=name,mobno=mobno,reqType=reqType,desc=desc)
        req.save()
        request_file = request.FILES['file'] if 'file' in request.FILES else None
        if request_file:
            fs = FileSystemStorage()
            filename=request_file.name
            extension=filename.split('.')[-1]
            file = fs.save("file_"+str(req.pk)+"."+extension, request_file)
        messages.success(request, 'Request Submitted Successfully with Tracking ID:'+str(req.pk))
    return render(request, 'servReq.html',{'heading':'Serve Request Page'})