from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator  
from googletrans import LANGUAGES 

def home(request):
    return render(request, 'home.html')

def translation_form(request):
    supported_languages = [(code, name) for code, name in LANGUAGES.items()]
    return render(request, 'translation.html', {'supported_languages': supported_languages})

def translate_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        source_lang = request.POST.get('source-lang')
        target_lang = request.POST.get('target-lang')

        #validation
        if text == '':
            return render(request, 'translation_result.html', {'translated_text': 'Please enter some text to translate'})
        
        if not source_lang :
            source_lang = 'english'
        if not target_lang :
            target_lang = 'english'

        try:
            translator = Translator()
            translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
        except Exception as e:
            return render(request, 'translation_result.html', {'translated_text': f'An error occurred: {str(e)}'})

        return render(request, 'translation_result.html', {'translated_text': translated_text})

    return HttpResponse('Method Not Allowed', status=405)
