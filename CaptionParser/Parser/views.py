from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import requests
# from .models import Document

# Create your views here.

def home(request):
#     pass
#     documents = Document.objects.all()
#     context = { 'documents': documents }
    return render(request, 'Parser/home.html' )

def model_form_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(request.FILES['file'])
            print(type(file))
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
#             print(filename)
#             print(type(filename))
            uploaded_file_url = fs.url(filename)
            handle_uploaded_file(request.FILES['file'],uploaded_file_url)
            return render(request, 'Parser/model_form_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
#             handle_uploaded_file(request.FILES['file'])
#             return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'Parser/model_form_upload.html', {'form': form})
class Stack:
    def __init__(self):
        self.a = []
    def Push(self, item):
        self.a.append(item)
    def Pop(self):
        return self.a.pop()
    def Peek(self):
        return self.a[len(self.a)-1]
    def Display(self):
        print(self.a)
    def IsEmpty(self):
        return self.a == []
s = Stack()
def handle_uploaded_file(f,uploaded_file_url):
    
    print('url = ', uploaded_file_url)
    print('over here = ',type(f))
    with open('C:/Users/s528358/eclipse-workspace/CaptionParser/Parser/name.txt', 'w') as destination:
#         line_count = 0
        temp_s = []
#         print(f)

        for i in f:

            print('yy = ',type(i))
            i = i.decode('ascii','ignore')
            print(i)
            temp_s = temp_s + i.split(' ')

            count = len(i)
#         print(temp_s)
        temp_s = temp_s[::-1]
        for word in temp_s:
            s.Push(word)
            s.Push(' ')

        first = []

        count = 0
        line = 0
        s.Pop()
        while not s.IsEmpty():    
            count = count + len(s.Peek())
            if count <= 42:
                first.append(s.Pop())
            elif count > 42:
        
                first = ' '.join(first)
#                 print(first)
#                 first = bytes(first,'ascii')
                first = first.split()
#                 print(first)
                destination.writelines(' '.join(first))
                count = 0
                first = []
                line = line + 1
                if line == 1:
                    destination.write('\n')
                else:
                    destination.write('\n\n')
                    if line == 2:
                        line = 0        
        destination.write(' '.join(first))
        print(first)

def uploadView(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(file.chunks())
#             for chunk in file.chunks():
#                 print(chunk)
            context = {}
            if file.multiple_chunks():
                context["uploadError"] = "Uploaded file is too big (%.2f MB)." % (file.size,)
            else:
                context["uploadedFile"] = file.read()
            return render(request,'Parser/fileUploadPage.html', context)
     
    else:
        form = UploadFileForm()
    return render(request, 'Parser/model_form_upload.html', {'form': form})