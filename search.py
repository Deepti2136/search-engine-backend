import json

with open("data.json") as f:
    data = json.load(f)

def search_engine(query):
    query = query.lower().strip()
    results = []

    for item in data:
        title_words = item["title"].lower().split()

        # Match only title words (language names)
        if query in title_words:
            results.append(item)

    if len(results) == 0:
        return {}

    grouped = {}
    for r in results:
        cat = r["category"]

        if cat not in grouped:
            grouped[cat] = []

        grouped[cat].append(r)

    return grouped