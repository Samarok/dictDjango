from django.shortcuts import render
from dictApp.models import Word
from dictApp.forms import WordForm

def home(request):
    context = {
        'PageTitle':"My dictionary",
        'active':'Home'
    }
    return render(request, 'home.html', context)

def wordsList(request):
    context = {
        'PageTitle':"Words list",
        'active':'WordsList',
        'words':Word.objects.all()
    }
    return render(request, 'wordslist.html', context)

def addWords(request):
        context = {
            'PageTitle':"Add words",
            'active':'AddWords',
            'form':WordForm
        }
        if request.method == "GET":
            return render(request, 'addwords.html', context)
        else:
            try:
                word = Word.objects.create(word=request.POST.get('word'), translation=request.POST.get('translation'))
                word.save()
                context["success"] = "Слово успешно добавлено"
            except Exception as ex:
                context["error"] = ex
            return render(request, 'addwords.html', context)