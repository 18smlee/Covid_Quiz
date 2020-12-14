from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from quizApp.models import quizUser, Quiz, Question,Response
from django import forms
from django.http import JsonResponse
#from chartit import DataPool, Chart

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

        currUser.covidScore = userScore
        currUser.save()
        print("after setting ", currUser.covidScore)


        labels = []
        data = []
        queryset = quizUser.objects.filter(covidScore__lte = currUser.covidScore)
        for user in queryset:
            labels.append(user.id)
            print("in query for loop")
            data.append(user.covidScore)


    args = {'user': currUser, 'labels':labels, 'data':data }
    return render(request, 'dataVis.html',args)

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)

    

def write_covidQuiz_questions(userID):
    currUser = quizUser.objects.get(id=userID)
    covidQuiz = Quiz.objects.get(title="Covid Quiz")
    
    q1 = Question.objects.create(
        quiz=covidQuiz,
        body="Attend a social gathering of 3 - 5 people",
    )

    q2 = Question.objects.create(
        quiz=covidQuiz,
        body="Hang out with friends",
    )
    q3 = Question.objects.create(
        quiz=covidQuiz,
        body="Attend a social gathering of 5-10 people",
    )
    q4 = Question.objects.create(
        quiz=covidQuiz,
        body="Attend a social gathering of 15+ people",
    )
    q5 = Question.objects.create(
        quiz=covidQuiz,
        body="Travel to Penn’s campus and did not quarantine",
    )
    q6 = Question.objects.create(
        quiz=covidQuiz,
        body="Eat at a restaurant (outdoors)",
    )
    q7 = Question.objects.create(
        quiz=covidQuiz,
        body="Eat at a restaurant (indoors)",
    )
    q8 = Question.objects.create(
        quiz=covidQuiz,
        body="Attended a large protest/parade",
    )

    q9 = Question.objects.create(
        quiz=covidQuiz,
        body="Traveled on plane ",
    )
    q10 = Question.objects.create(
        quiz=covidQuiz,
        body="Went outside without a mask",
    )
    q11 = Question.objects.create(
        quiz=covidQuiz,
        body="Been to a bar",
    )
    q12 = Question.objects.create(
        quiz=covidQuiz,
        body="Been clubbing",
    )
    q13 = Question.objects.create(
        quiz=covidQuiz,
        body="Hosted a 'COVID Party'",
    )
    q14 = Question.objects.create(
        quiz=covidQuiz,
        body="Tested positive for covid ",
    )
    q15 = Question.objects.create(
        quiz=covidQuiz,
        body="Went to a party ",
    )
    q16 = Question.objects.create(
        quiz=covidQuiz,
        body="Know a family member/friend who tested positive for covid ",
    )
    q17 = Question.objects.create(
        quiz=covidQuiz,
        body="Got arrested for breaking social distancing guidelines ",
    )
    q18 = Question.objects.create(
        quiz=covidQuiz,
        body="Went out in public knowing I had covid",
    )
    q19 = Question.objects.create(
        quiz=covidQuiz,
        body="Went to a party knowing I had covid",
    )
    q20 = Question.objects.create(
        quiz=covidQuiz,
        body="Hooked up with someone knowing I had covid",
    )
    q21 = Question.objects.create(
        quiz=covidQuiz,
        body="Hooked up with someone knowing they had Covid",
    )
    q22 = Question.objects.create(
        quiz=covidQuiz,
        body="Broke quarantine",
    )
    q23 = Question.objects.create(
        quiz=covidQuiz,
        body="Went out for Halloweekend",
    )
    q24 = Question.objects.create(
        quiz=covidQuiz,
        body="Refused to wear a mask when someone told you to",
    )
    q25 = Question.objects.create(
        quiz=covidQuiz,
        body="Hosted an apartment/house party",
    )
    q26 = Question.objects.create(
        quiz=covidQuiz,
        body="Got hospitalized from COVID",
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
