from typing import ParamSpec
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    myText = request.POST.get('text', 'default')
    punctuation = request.POST.get('punctuation', 'default')
    num_remove = request.POST.get('num_remove', 'default')
    capital = request.POST.get('capital', 'default')
    line_remove = request.POST.get('line_remove', 'default')
    extra_spaces = request.POST.get('extra_spaces', 'default')
    char_count = request.POST.get('char_count', 'default')

    print(myText)

    if punctuation == "on":
        analyzed_text = ""
        punctuations = '''~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/'''
        for i in myText:
            if i not in punctuations:
                analyzed_text += i
        params = {
            'reason': 'Removed Punctuations',
            'analyzed_text': analyzed_text
        }
        myText = analyzed_text
        
    if capital == "on":
        analyzed_text = ""
        for i in myText:
            analyzed_text += i.upper()
        params = {
            'reason': 'Converted to UPPERCASE',
            'analyzed_text': analyzed_text
        }
        myText = analyzed_text
        
    
    if line_remove == "on":
        analyzed_text = ""
        for i in myText:
            if i != "\n" and i != "\r":
                analyzed_text += i
        params = {
            'reason': 'Removed New Lines',
            'analyzed_text': analyzed_text
        }
        myText = analyzed_text
       
    if extra_spaces == "on":
        analyzed_text = ""
        for index, i in enumerate(myText):
            if not(myText[index] == " " and myText[index+1]==" "):
                analyzed_text = analyzed_text + i
        params = {
            'reason': 'Removed extra spaces',
            'analyzed_text': analyzed_text
        }
        myText = analyzed_text
    
    if num_remove == "on":
        analyzed_text = ""
        integers = '''0123456789'''
        for i in myText:
            if i not in integers:
                analyzed_text += i
        params = {
            'reason': 'Removed Numbers',
            'analyzed_text': analyzed_text
        }
        myText = analyzed_text
        
    if char_count == "on":
        analyzed_text = myText
        params = {
            'reason': 'Counted the characters',
            'analyzed_text': f"{analyzed_text}:-\nThe characters in the text are {len(myText)}"
        }
        
        

    return render(request, 'analyze.html', params)

    if punctuation == "default" and line_remove == "default" and capital == "default" and extra_spaces == "default" and num_remove == "default" and char_count == "default":
        return HttpResponse("Go back and choose some option")

def create_account(request):
    return render(request, "createAccount.html")

def create_account_success(request):
    name1 = request.POST.get('name1', 'default')
    name2 = request.POST.get('name2', 'default')
    email = request.POST.get('email', 'default')
    password = request.POST.get('password', 'default')
    city = request.POST.get('city', 'default')
    address = request.POST.get('address', 'default')
    country = request.POST.get('country', 'default')

    

    name = f"{name1} {name2}"
    print(f"{name} joined")
    with open("users.txt", 'a') as f:
        f.write(f"Name :- {name}\nEmail :- {email}\nPassword :- {password}\nCity    :-     {city}\nAddress :- {address}\nCountry :- {country}\n\n\n")

    with open("names.txt", 'a') as a:
        a.write(f"{name} from {country}\n")
    
    params = {
        'name':name
    }
    return render(request, "accountSuccess.html", params)

    
    
    

def contact(request):
    return render(request, "contact.html")

def about(request):
    with open("names.txt", 'r') as f:
        for i in f:
            var = f.read()
    params = {
        'inforamtion':var
    }
    return render(request, "about.html", params)

def contact_success(request):
    name1 = request.POST.get('text1', 'default')
    email = request.POST.get('email', 'defult')
    text = request.POST.get('text', 'default')

    with open("contact.txt", 'a') as w:
        w.write(f'''Name :- {name1}\nEmail :- {email}\nMessage is " {text} "\n\n''')
    
    return render(request, "contact_success.html")
