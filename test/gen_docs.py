""" Generates docs for testing 

All documents come from Wikipedia
"""

import minillm as ml
import json

planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]

with open("test/planets.json", "w") as f:
    docs = [{"name": p, "content": ml.get_wiki(f"Planet {p}")} for p in planets]
    json.dump(docs, f)
