# This is Debayan Sarkar

from django.http import HttpResponse
from django.shortcuts import render
#from django.shortcuts import HttpResponse

#def navigation(request):

 #  s = '''<h2>Navigation Bar<br></h2>
    #        <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br>
   #         <a href="https://www.facebook.com/">Facebook</a><br>

     #       <a href="https://www.flipkart.com/">Flipkart</a><br>

      #      <a href="https://www.hindustantimes.com
#">News</a><br>
 #           <a href="https://www.google.com/">Google</a>'''

  # return HttpResponse(s)

'''def index(request):

   return render(request,'index.html')'''
   #return HttpResponse("Hello")


#def removepunc(request):
   #return HttpResponse("remove punc")


#def cap(request):
   #return HttpResponse("capitalize first")


#def newlineremove(request):
  # return HttpResponse("newline remove first")

def index(request):

   return render(request,'index.html')


def analyze(request):


   # Get the text
   djtext = request.POST.get('text', 'default')
   print(djtext)
   removepunc = request.POST.get('removepunc', 'off')
   fullcaps = request.POST.get('fullcaps', 'off')
   newlineremover= request.POST.get('newlineremover', 'off')
   extraspaceremover= request.POST.get('extraspaceremover', 'off')
   charcounter= request.POST.get('charcounter', 'off')

   #analyzed = djtext

   if removepunc == "on":
      punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      analyzed = ""
      for char in djtext:
         if char not in punctuations:
            analyzed = analyzed + char
      params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
      djtext = analyzed
     # return render(request, 'analyze.html', params)

   if(fullcaps == "on"):
      analyzed = ""
      for char in djtext:
         analyzed = analyzed + char.upper()
      params = {'purpose': 'Change To UpperCase', 'analyzed_text': analyzed}
      djtext = analyzed
     # return render(request, 'analyze.html', params)

   if(newlineremover=="on"):
      analyzed = ""
      for char in djtext:
         if char != "\n" and char != "\r":
             analyzed = analyzed + char
      params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
      djtext = analyzed
     # return render(request, 'analyze.html', params)


   if (extraspaceremover == "on"):
      analyzed = ""
      for index, char in enumerate(djtext):
         if not (djtext[index] == " " and djtext[index + 1] == " "):
            analyzed = analyzed + char

      params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
      djtext = analyzed



      return render(request, 'analyze.html', params)

   if(charcounter == "on"):
      analyzed = ""
      count = 0
      for char in djtext:
         analyzed = analyzed + char
         #length = len(analyzed)
         count = count + 1




      params = {'purpose': 'Count The No. Of Characters', 'analyzed_text':count}

# Analyze the text

   if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
      return HttpResponse("PLEASE SELECT ANY ONE OF THE GIVEN OPTIONS")

   return render(request, 'analyze.html', params)

