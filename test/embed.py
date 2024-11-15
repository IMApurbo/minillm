import minillm as ml
import numpy as np
import time
import json
import os
import psutil


def mem_used_gb():
    process = psutil.Process(os.getpid())
    bytes = process.memory_info().rss
    gigabytes = bytes * 1e-9
    return gigabytes


print(f"Memory used before loading models: {mem_used_gb():.2f}GB")

print("\n# Embedding Tests\n")

planets = json.load(open("test/planets.json"))[-4:]

# Make sure the model is loaded before testing
start = time.perf_counter_ns()
ml.docs.store("just initializing")
ml.docs.clear()
print(f"Model load time: {(time.perf_counter_ns() - start) / 1e6:.0f}ms")

start = time.perf_counter_ns()
for planet in planets:
    ml.docs.store(planet["content"], planet["name"])
ms = (time.perf_counter_ns() - start) / 1e6
print(
    f"Embedded {len(ml.docs.chunks)} chunks in {ms:.0f}ms ({ms/len(ml.docs.chunks):.0f}ms per chunk)"
)

start = time.perf_counter_ns()
print(ml.get_doc_context("Which planets have rings?"))
print(f"Search time: {(time.perf_counter_ns() - start) / 1e6:.0f}ms")
ml.docs.clear()

# Create many fake docs to benchmark search
# We create 10 unique docs then duplicate them
# A fully random set of docs would be better, but takes a long time to generate
docs = [ml.embeddings.Document(str(i), np.random.rand(384)) for i in range(10)]
start = time.perf_counter_ns()
ml.embeddings.search("Test", docs * 10000)
print(f"100k search time: {(time.perf_counter_ns() - start) / 1e6:.0f}ms")
docs = None

max_ram = ml.config["max_ram"]
print(
    f"Memory used after all tests: {mem_used_gb():.2f}GB (must be under {max_ram:.2f}GB)"
)

# Confirm that we fit in max_ram after running all tests
assert mem_used_gb() < max_ram
