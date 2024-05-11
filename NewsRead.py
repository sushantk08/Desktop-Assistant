from desktop_assistant import *
import requests
import json


def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=55a7e9bb81cc4fb5b3661e5d2ec8b374",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=55a7e9bb81cc4fb5b3661e5d2ec8b374",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=55a7e9bb81cc4fb5b3661e5d2ec8b374",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=55a7e9bb81cc4fb5b3661e5d2ec8b374",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=55a7e9bb81cc4fb5b3661e5d2ec8b374",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=55a7e9bb81cc4fb5b3661e5d2ec8b374"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")
