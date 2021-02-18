from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charctercount = request.GET.get('charctercount','off')

    # Check which box is on
    if removepunc == 'on':
        Punctuations = '''!()-[]{};:'",<>./?!@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in Punctuations:
                analyzed += char
        remove = {'purpose': 'Removed Punctuations', 'removepunc': analyzed}
        # Analyze HttpResponse
        return render(request,'analyze.html',remove)
    
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
            if char == ' ':
                analyzed += '   '
        params = {'purpose': 'Changes to UpperCase', 'analyzed_text': analyzed}
        # Analyze HttpResponse
        return render(request,'analyze.html',params)
    
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed += char
        params = {'pupose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request,'analyze.html',params)
    
    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]) == " " and djtext[index+1] == " ":
                analyzed += char
        params = {'pupose': 'Removed Spaces', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request,'analyze.html',params)
    
    if charctercount == 'on':
        analyzed = 0
        for char in djtext:
            if char == " ":
                continue
            else:
                analyzed += 1
        params = {'purpose': 'Charcter Count', 'analyzed_text': analyzed}   
        # Analzed the text
        return render(request, 'analyze.html',params)

    else:
        return HttpResponse('Error')