from django.shortcuts import render

def home_view(request):
    return render(request,'base.html')

def bankByIFSC():
    pass
def bankByNameandCity():
    pass