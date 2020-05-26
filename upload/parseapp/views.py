from django.shortcuts import render,redirect
from .forms import StudentForm
from docx import *


lin = []


def submit(request):

    if request.method == 'POST':
        file1 = request.FILES['document']
        document = Document(file1)

        lines = []
        for para in document.paragraphs:
            temp = ""
            line = para.text.split()
            c = 0
            for x in line:
                if x == ":":
                    c = 1
                if c > 1:
                    temp += x + " "
                c += 1
            lines.append(temp)
        for i in lines:
            lin.append(i)

        context = {'fname': lin[0],
                   'lname': lin[1],
                   'email': lin[2],
                   'phno': lin[3],
                   'st': lin[4],
                   'city': lin[5],
                   'state': lin[6],
                   'country': lin[7],
                   'pincode': lin[8],
                   }
        form = StudentForm(context)
        if form.is_valid():
            form.save()
            return redirect('/submit')
        return render(request,'submit.html')

