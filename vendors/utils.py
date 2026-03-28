from rapidfuzz import fuzz

def find_duplicates(vendors):
    duplicates = []

    for i in range(len(vendors)):
        for j in range(i+1, len(vendors)):

            name1 = vendors[i]['name']
            name2 = vendors[j]['name']

            if name1 == name2:
                continue  # ❌ skip exact same names

            score = fuzz.ratio(name1, name2)

            if score > 85:
                duplicates.append({
                    "vendor1": name1,
                    "vendor2": name2,
                    "score": score,
                    "savings": round((score/100)*10000, 2)
                })

    return duplicates