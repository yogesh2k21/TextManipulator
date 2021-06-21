from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'home.html')

def analyze(request):
    msg=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    upper=request.POST.get('upper','off')
    xtraSpace=request.POST.get('xtraSpace','off')
    newLineRemover=request.POST.get('newLineRemover','off')
    charCount=request.POST.get('charCount','off')
    if msg:
        analyzed=msg
        if upper=="on":
            UPPER=""
            for char in msg:
                UPPER=UPPER+char.upper()

            analyzed=UPPER
            params={'purpose':'Changed to upperCase','analysed_text':analyzed}

        if removepunc=="on":
            temp=""
            punctuation = '''!()*&$%^$#&#!@#$%^&*(){@}`##~|"|\/.;'"_-++='''
            for char in analyzed:
                if char not in punctuation:
                    temp=temp+char
            analyzed=temp
            params={'purpose':'Removed Punctuction','analysed_text':analyzed}

        if xtraSpace=="on":
            xtra=""
            for index,char in enumerate(analyzed):
                if not (analyzed[index]==" " and analyzed[index+1]==" "):
                    xtra=xtra+char
            analyzed=xtra
            params={'purpose':'Removing Extra Spaces','analysed_text':analyzed}

        if newLineRemover=="on":
            newline=""
            for i in analyzed:
                if i!="\n" and i!="\r":
                    newline=newline+i

            analyzed=newline
            params={'purpose':'New Line Remover','analysed_text':analyzed}

        if charCount=="on":
            Counter=None
            for index,char in enumerate(analyzed):
                Counter=index+1
            params={'purpose':'Character Counter','analysed_text':analyzed,'count':Counter}
        return render(request,'analyse.html',params)
    else:
        return HttpResponse("ERROR")