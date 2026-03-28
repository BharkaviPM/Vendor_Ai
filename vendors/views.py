from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')
from .utils import find_duplicates
from .ai_utils import generate_report


from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",   
    max_new_tokens=150
)
DATA_PATH = r"C:\Users\Dell\Downloads\vendor\comp.csv"


# 🔹 Load dataset
def load_data():
    df = pd.read_csv(DATA_PATH, encoding='latin1')

    print("Columns:", df.columns)  # debug

    # ✅ Flexible column handling
    name_col = None
    industry_col = None
    location_col = None

    for col in df.columns:
        col_lower = col.lower()

        if 'name' in col_lower:
            name_col = col
        elif 'category' in col_lower or 'industry' in col_lower:
            industry_col = col
        elif 'country' in col_lower or 'location' in col_lower:
            location_col = col

    # fallback if missing
    if not industry_col:
        industry_col = name_col
    if not location_col:
        location_col = name_col

    df = df[[name_col, industry_col, location_col]].dropna()
    df.columns = ['name', 'industry', 'location']

    return df.to_dict(orient='records')


# 📊 Generate chart
def generate_chart(duplicates):
    names = [d['vendor1'] for d in duplicates[:5]]
    savings = [d['savings'] for d in duplicates[:5]]

    os.makedirs("media", exist_ok=True)

    plt.figure()
    plt.barh(names, savings)

    path = "media/chart.png"
    plt.savefig(path)
    plt.close()

    return path


# 🏠 Main dashboard
def dashboard(request):
    vendors = load_data()
    duplicates = find_duplicates(vendors)

    chart = generate_chart(duplicates)  # ✅ FIXED

    report = generate_report(duplicates)

    return render(request, 'dashboard.html', {
        'duplicates': duplicates[:10],
        'report': report,
        'chart': chart
    })


# 📤 Upload file feature (optional but good for demo)
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        df = pd.read_csv(file)

        vendors = df.to_dict(orient='records')

        duplicates = find_duplicates(vendors)
        chart = generate_chart(duplicates)
        report = generate_report(duplicates)

        return render(request, 'results.html', {
            'duplicates': duplicates[:10],
            'report': report,
            'chart': chart
        })

    return render(request, 'upload.html')
from django.shortcuts import render
import pandas as pd
from .utils import find_duplicates
from .ai_utils import generate_report


# store last result (simple hackathon approach)
GLOBAL_DUPLICATES = []


def upload_file(request):
    global GLOBAL_DUPLICATES

    if request.method == 'POST':
        file = request.FILES['file']
        df = pd.read_csv(file)

        # auto-detect columns
        df = df.dropna()
        df.columns = [c.lower() for c in df.columns]

        name_col = [c for c in df.columns if 'name' in c][0]

        df = df[[name_col]]
        df.columns = ['name']

        vendors = df.to_dict(orient='records')

        duplicates = find_duplicates(vendors)
        GLOBAL_DUPLICATES = duplicates

        report = generate_report(duplicates)

        return render(request, 'dashboard.html', {
            'duplicates': duplicates[:10],
            'report': report,
            'chart': "media/chart.png"
        })

    return render(request, 'upload.html')
def ask_question(request):
    global GLOBAL_DUPLICATES

    answer = None

    if request.method == 'POST':
        question = request.POST.get('question').lower()

        if not GLOBAL_DUPLICATES:
            return render(request, 'ask.html', {
                'answer': "No data available. Please upload dataset first."
            })

        total_duplicates = len(GLOBAL_DUPLICATES)
        top = GLOBAL_DUPLICATES[0]
        total_savings = sum([d['savings'] for d in GLOBAL_DUPLICATES[:5]])

        # ✅ Clean deterministic answers (IMPORTANT)
        if "total" in question:
            answer = f"The system identified {total_duplicates} duplicate vendors."

        elif "saving" in question:
            answer = f"The estimated cost savings from top vendors is ₹{round(total_savings,2)}."

        elif "top" in question or "highest" in question:
            answer = f"The highest saving opportunity is between {top['vendor1']} and {top['vendor2']} with ₹{top['savings']}."

        elif "why" in question:
            answer = "Duplicate vendors increase procurement costs due to redundant contracts and overlapping services."

        else:
            answer = f"The system identified {total_duplicates} duplicate vendors, indicating significant cost optimization opportunities."

    return render(request, 'ask.html', {'answer': answer})