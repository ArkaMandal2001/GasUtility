from django.shortcuts import render,HttpResponse
from servReq.models import Request
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    #data=Request.objects.all()
    if(request.method=='POST'):
        reqId=request.POST['reqId']
        if(reqId==''):
            return render(request, 'reqTrack.html',{'heading':'Request Tracking Page','error':'Request ID not entered'})
        data=Request.objects.filter(pk=reqId).first()
        if(data==None):
            return render(request, 'reqTrack.html',{'heading':'Request Tracking Page','error':'Request ID not found'})
        
        fileExists=False
        fs = FileSystemStorage()
        all_files=fs.listdir("")
        for file in all_files[1]:
            if file.split('.')[0]=="file_"+str(reqId):
                fileExists=True
                break
        return render(request, 'reqTrack.html',{'heading':'Request Tracking Page','data':data,'fileExists':fileExists})
    return render(request, 'reqTrack.html',{'heading':'Request Tracking Page'})