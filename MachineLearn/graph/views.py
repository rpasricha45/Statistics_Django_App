from django.shortcuts import render

# Create your views here.
# def index (request):
#     # method to display the first Webpage
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     return render(request,'graph/home.html',context=my_dict)


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Document
from .forms import DocumentForm
import pandas as pd
from django.template import loader, Context
from os import listdir
from django.http import JsonResponse
import json
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.cross_validation import train_test_split
import csv,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# to use for other methods

def home (request):
    return render(request,"index.html")


def index(request):
    if request.method == 'POST':
        #Check if the form is valid then
        #save the documentform file in the document model
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            direc = request.FILES['docfile']
            direc = str(direc)
            direc = "documents/documents/"+ direc
            # # DEBUG:
            # print("this is the directoroy selected for the initatal view file")
            # print(direc)




            newdoc.save()
            #csvimport(newdoc.docfile) # this is the issue

            #Redirect to list after POST
            # please  do somethhing after the button is clicked

            #return HttpResponseRedirect(reverse('home.html'))
            #


            dataset = pd.read_csv(direc)

            stats  = dataset.describe()
            test= stats.iloc[0:1]

            stats.to_html('templates/graph/new.html',classes="stats",justify="center")
            statsPage = loader.get_template("new.html")

            my_dict = {'insert_me':stats,'test':test,'html':statsPage.render()}
            return render(request,'graph/example.html',context=my_dict)

            # Redirect
            if request.method == 'POST':
                print("the button was clicked")
                HttpResponseRedirect("urls")



    else:
        #If there are any documents already uploaded then show them and show them the form
        form = DocumentForm()
    documents = Document.objects.all()



    return render(
        request,
        'graph/home.html',
        {'form':form,
        'documents':documents}
    )

def linearReg (request):
    # test to see if it is possible to get name of file


    print("this is the directroy for the linerar REg ")
    fileDirec = listdir("documents/documents")[0]

    print(fileDirec)
    print(" this is the list")
    print(listdir("documents"))
    # debugging
    print(fileDirec + " this is the orginal path ")

    fileDirec = "documents/documents/" + fileDirec

    print("this is the new path")
    print(fileDirec)

    dataset = pd.read_csv(fileDirec)
    # delete the file directroy
    os.remove(fileDirec)

    x = dataset.iloc[:,0].values.tolist()
    y = dataset.iloc[:, 1].values.tolist()

    # split the dataset
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)
    # fit the linar model

    regressor = LinearRegression()
    X_train = np.reshape(X_train,[len(X_train),1]).tolist()
    y_train = np.reshape(y_train,[len(y_train),1]).tolist()



    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_train).tolist()
    #
    # # Predicting the Test set results
    # y_pred = regressor.predict(X_test)


    #  linear regression model




    #dataset = pd.read_csv(d)


    response = json.dumps({"h":X_train,"y":y_train,"pred":y_pred})
    dict = { "x": response}


    print(" this is teh list now")
    print(listdir("documents"))


    return render(request,"graphing.html",context=dict)
