from django.shortcuts import render, redirect, get_object_or_404
from quizApp.models import quizUser, Quiz, Question,Response
from django import forms

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})

def covidQuiz_view(request):
    # will only write questions if a user is made --- change later?? not super safe
    if request.method == 'POST':
        user = quizUser.objects.create(
            school=request.POST['School'],
            year_in_school=request.POST['Year'],
            quiz=Quiz.objects.get(title="Covid Quiz")
        )
        # clear questions for new user, write covid quiz questions, store in questions
        Question.objects.filter(quiz__title="Covid Quiz").delete()
        write_covidQuiz_questions(user.id)
        questions = Question.objects.filter(quiz__title="Covid Quiz")
        
    args = {'user':user, 'questions':questions}
    return render(request, 'covidQuiz.html', args)

def dataVis_view(request,userID):
    userScore = 0
    if request.method == 'POST':
        currUser = quizUser.objects.get(id=userID)

        for question in Question.objects.filter(quiz__title="Covid Quiz"):
            print("question id is ",question.id)
            currresponse = Response.objects.create(
                question = question,
                userChoice = request.POST.get(str(question.id),'default'),
                user = currUser
            )

            userChoice = currresponse.userChoice
            userScore += convertToNum(userChoice)
            print("user choice is: ", userChoice)
            print("userScore is", userScore)
        
            
               
                

    return render(request, 'dataVis.html')

def write_covidQuiz_questions(userID):
    currUser = quizUser.objects.get(id=userID)
    covidQuiz = Quiz.objects.get(title="Covid Quiz")
    
    q1 = Question.objects.create(
        quiz=covidQuiz,
        body="How often do you eat in a restaurant outside",
    )

    q2 = Question.objects.create(
        quiz=covidQuiz,
        body="How outside",
    )

def convertToNum(userChoice):
    if ( "optionNever" in userChoice):
        numericalChoice = 0
    elif("optionOncePM" in userChoice):
        numericalChoice = 1
    elif ("optionOncePW" in userChoice):
        numericalChoice = 2
        print("this is if statement\n")
    else:
        numericalChoice = 3
        
    print(userChoice," the number is ",numericalChoice)
    return numericalChoice
