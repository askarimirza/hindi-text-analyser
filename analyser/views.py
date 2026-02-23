from django.shortcuts import render
from collections import Counter
import re

def home(request):
    result = None
    cleaned_sentence = ""

    if request.method == "POST":
        text = request.POST.get("text")

        if text:
            text = re.sub(r'[^\u0900-\u097F\s]', '', text)
            words = text.split()

            stopwords = ["है", "की", "और", "का", "एक"]

            filtered_words = [word for word in words if word not in stopwords]

            cleaned_sentence = " ".join(filtered_words)

            result = dict(Counter(filtered_words))   # 🔥 IMPORTANT

    return render(request, "home.html", {
        "result": result,
        "cleaned_sentence": cleaned_sentence
    })