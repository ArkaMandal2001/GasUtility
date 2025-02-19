import datetime
from django.shortcuts import render
from servReq.models import Request
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    if request.method=='POST':
        id=request.POST['reqId']
        status=request.POST['newStatus']
        req=Request.objects.get(pk=id)
        req.status=status
        if(status=="Resolved"):
            req.dateTimeResolved=datetime.datetime.now()
        req.save()
    dataList=Request.objects.all()

    fs = FileSystemStorage()
    all_files=fs.listdir("")[1]
    fileExists=[]
    for file in all_files:
        fileExists.append(file.split('.')[0].split('_')[1])
    for data in dataList:
        if str(data.pk) not in fileExists:
            data.fileExists=False
        else:
            data.fileExists=True
    return render(request, 'manageReq.html',{'dataList':dataList})