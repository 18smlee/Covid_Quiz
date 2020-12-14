from django.shortcuts import render, redirect, get_object_or_404
from quizApp.models import quizUser, Quiz, Question,Response
from django import forms

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})

def covidQuiz_view(request,):
    # will only write questions if a user is made --- change later?? not super safe
    if request.method == 'POST':
        user = quizUser.objects.create(
            school=request.POST['School'],
            year_in_school=request.POST['Year'],
            on_campus_housing=request.POST['onCampusHousing'],
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
        
        # calculates score for Covid Quiz
        numQuestions = 0
        score = 0
        highestScore = 0
        for question in Question.objects.filter(quiz__title="Covid Quiz"):
            currresponse = Response.objects.create(
                question = question,
                userChoice = request.POST.get(str(question.id),'default'),
                user = currUser
            )
            userChoice = currresponse.userChoice
            numQuestions += 1
            highestScore += 3 * question.weight
            score += convertToNum(userChoice) * question.weight
        currUser.covidScore = int((score / highestScore) * 100)
        currUser.save()

    args = {'user': currUser}
    return render(request, 'dataVis.html',args)

def write_covidQuiz_questions(userID):
    currUser = quizUser.objects.get(id=userID)
    covidQuiz = Quiz.objects.get(title="Covid Quiz")
    
    q1 = Question.objects.create(
        quiz=covidQuiz,
        body="Attend a social gathering of 3-5 people including your usual contacts",
        weight=2
    )

    q2 = Question.objects.create(
        quiz=covidQuiz,
        body="Attend a social gathering of 5-10 people including your usual contacts",
        weight=3
    )
    q3 = Question.objects.create(
        quiz=covidQuiz,
        body="Attend a social gathering of 15+ people",
        weight=4
    )
    q4 = Question.objects.create(
        quiz=covidQuiz,
        body="Eat at a restaurant outdoors",
        weight=2
    )
    q5 = Question.objects.create(
        quiz=covidQuiz,
        body="Eat at a restaurant indoors",
        weight=3
    )
    q6 = Question.objects.create(
        quiz=covidQuiz,
        body="Go grocery shopping",
        weight=2
    )
    q7 = Question.objects.create(
        quiz=covidQuiz,
        body="Go to a bar or clubbing",
        weight=4
    )
    q8 = Question.objects.create(
        quiz=covidQuiz,
        body="Go to the gym",
        weight=4
    )

    q9 = Question.objects.create(
        quiz=covidQuiz,
        body="Eat dinner at a friend's house",
        weight=2
    )
    q10 = Question.objects.create(
        quiz=covidQuiz,
        body="Hug or shake hands with a friend",
        weight=3
    )
    q11 = Question.objects.create(
        quiz=covidQuiz,
        body="Go to the hair salon or barbershop",
        weight=2
    )
    q12 = Question.objects.create(
        quiz=covidQuiz,
        body="Study with 2 or more friends outside",
        weight=2
    )
    q13 = Question.objects.create(
        quiz=covidQuiz,
        body="Study with 2 or more friends inside",
        weight=3
    )
    q14 = Question.objects.create(
        quiz=covidQuiz,
        body="Go on a walk with a friend who doesn't live with you",
        weight=2
    )
    q15 = Question.objects.create(
        quiz=covidQuiz,
        body="Watch a movie at the movie theater",
        weight=4
    )

def convertToNum(userChoice):
    if ( "optionNever" in userChoice):
        numericalChoice = 3
    elif("optionOncePM" in userChoice):
        numericalChoice = 2
    elif ("optionOncePW" in userChoice):
        numericalChoice = 1
        print("this is if statement\n")
    elif("optionEveryday" in userChoice):
        numericalChoice = 0
    else:
        numericalChoice = 3
        
    print(userChoice," the number is ",numericalChoice)
    return numericalChoice

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)
