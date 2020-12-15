# Covid Purity Test
## Final Project
> By Sam Lee & Nadine Wain

## Description
The Covid Purity Test serves as indicator for how covid prone your current lifestyle and behaviors are.
The higher your score, the safer your lifestyle! 
After your score is calculated, you can compare your score to other Penn students on campus! Share with your friends and stay safe :) 
> Inspired by the Rice Purity Test https://www.ricepuritytest.com
 
## Installation Requirements
1. Ensure you have python installed, if not follow these intructions https://www.python.org/downloads/
2. Ensure you have django installed, if not follow these instructions https://docs.djangoproject.com/en/3.1/topics/install/
3. Download the code file
4. On your terminal, navigate to "covid_app"
5. Run "python manage.py runserver" 
6. Go to localhost:8000 to view and starting using the web app
7. Follow instructions on https://cis192.github.io/django1 if you face difficulties up until then

## Using the App

1. The project is a webapp and goes in the sequence: HomePage -> Quiz -> Results and Visualizations
2. Once you have the webapp running you will need to fill out a few details on the homepage and then press "Take Quiz"
3. This will take you to the quiz page where you can fill out the quiz (format inspired by the Rice Purity Test)
4. If you don't fill out a question, we will assume your answer is "Never" for that question.
5. Some questions weigh heigher due to the severity of the behavior mentioned in the question.
5. Once you have filled out the questions you can press the "Calculate Score" button to find out how pure you are on a scale of 1-100
6. You will also be able to see some comparisons and visualizations which are based off the answers the website has received!
