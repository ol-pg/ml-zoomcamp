import requests

url = 'http://localhost:9696/predict'

data = {"question": 'How much of an effort would it be to use AWS instead of GCP for assignments?',
        "candidate_answers": ['No, you cannot.',
                              "Yeah. I am a data scientist and, as a part of my role, I quite often needed to create data pipelines. Knowing data engineering, knowing Spark, and things like workflow orchestrators was really helpful, especially when I worked in a startup and we didn't have a data engineering team that could support us. We needed to do everything on our own and this is how I picked up these data engineering skills and they were immensely useful. If you're in data science and machine learning, knowing how to build data pipelines is extremely useful. Maybe knowledge of data warehousing and analytics engineering and dashboarding is a bit less relevant, at least to what I do as a data scientist, but I think it could still be useful.",
                              'I think I already showed you. If you go to our YouTube channel, and search for “data engineering,” you will see a lot of interesting videos. There’s this Getting a Data Engineering Job video and then this one could also be quite relevant.',
                              "I don't know. I never tried to do it there. Maybe you can just go and try it. If it works, let us know. And if it doesn't, also let us know so we know the answer.",
                              "Alexey\nProbably more than you want to put in. I mean, if you have time, why not? But we will not be able to support you. I struggle to come up with an estimate. Does anyone here on this call have an estimate?\nVictoria\nI think the hardest part is – you shouldn't be a data engineer if you’re taking this course. You shouldn't have the knowledge that we're teaching. And if you don't have the knowledge, you're trying to learn it, and then everything is showing you something else. On top of that, you want to learn something new on your own that you won't have support for. That's going to be really hard. If you really want AWS because they use AWS at your work, they're going to help you with that one. It's probably not going to be worth it. It's going to be very, very stressful. I would add at least two hours on top of the normal hours."]

        }

response = requests.post(url, json=data)
print(response)
print(response.json())
