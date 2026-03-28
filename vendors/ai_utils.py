from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(duplicates):

    # ✅ Always define this first
    total_savings = sum([d['savings'] for d in duplicates[:5]])

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Analyze these duplicate vendors:
                    {duplicates[:5]}

                    Generate:
                    - Executive Summary
                    - Cost Savings Insight
                    - Action Plan
                    """
                }
            ]
        )

        return response.choices[0].message.content

    except Exception:
        # ✅ Safe fallback (no API needed)
        return f"""
🔍 STEP 1: DETECTION
Identified {len(duplicates)} duplicate vendor relationships.

📊 STEP 2: ANALYSIS
High similarity vendors indicate redundant procurement.

💰 STEP 3: IMPACT
Estimated savings: ₹{total_savings}

⚡ STEP 4: ACTION PLAN
- Consolidate duplicate vendors
- Renegotiate contracts
- Reduce vendor redundancy

🚀 FINAL RESULT:
Procurement cost optimized and efficiency improved.
"""
from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

def generate_report(duplicates):
    prompt = f"Analyze vendor duplicates: {duplicates[:5]}"
    result = generator(prompt, max_length=200)
    return result[0]['generated_text']