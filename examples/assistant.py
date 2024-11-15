""" A simple assistant

The assistant uses information retrieval to obtain context from a small set
of stored documents. The included information is the current weather, current
date, and a brief summary of the Python programming language and the planet
Saturn.

A number of demonstration question are completed to demonstrate the available
functionality.
"""

import minillm as ml


def assist(question):
    context = ml.get_doc_context(question)

    return ml.do(f"Answer using context: {context} Question: {question}")


lat, lon = (41.8, -87.6)

ml.store_doc(ml.get_wiki("Python language"), "Python")
ml.store_doc(ml.get_wiki("Planet Saturn"), "Saturn")
ml.store_doc(ml.get_weather(lat, lon), "Weather")
ml.store_doc(ml.get_date(), "Time")

questions = [
    "What day of the week is it?",
    "Is it going to rain today?",
    "What time is it?",
    "Who created Python?",
    "How many moon does Saturn have?",
]

for question in questions:
    print(f"{question} {assist(question)}")
