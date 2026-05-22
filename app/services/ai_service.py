import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")


def local_farming_fallback(prompt):
    text = prompt.lower()

    if "yellow" in text or "leaf" in text or "leaves" in text:
        return """
Krishi AI cloud service unavailable.

Plant Health Guidance:
- Check soil moisture (avoid overwatering)
- Look for yellow spots or fungus
- Check nitrogen deficiency
- Inspect root health
- Remove damaged leaves
"""

    elif "pest" in text or "bug" in text or "insect" in text:
        return """
Krishi AI cloud service unavailable.

Pest Check Guidance:
- Inspect under leaves
- Look for holes or bite marks
- Check stem damage
- Remove infected leaves
- Use safe pest treatment if needed
"""

    elif "water" in text or "irrigation" in text:
        return """
Krishi AI cloud service unavailable.

Irrigation Guidance:
- Check soil moisture first
- Avoid daily overwatering
- Water near roots
- Check drainage
- Water early morning if possible
"""

    elif "fertilizer" in text or "nutrient" in text:
        return """
Krishi AI cloud service unavailable.

Fertilizer Guidance:
- Check NPK balance
- Avoid over-fertilizing
- Apply based on crop stage
- Inspect leaf color changes
- Water after fertilizer if needed
"""

    else:
        return """
Krishi AI could not reach cloud AI right now.

Basic Farming Guidance:
- Check soil moisture
- Inspect leaves for pests
- Watch for fungus or yellow spots
- Verify fertilizer balance
- Remove damaged leaves
"""


def get_ai_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Krishi AI, an agricultural assistant. "
                        "Give practical, simple farming advice. "
                        "Focus on crops, pests, irrigation, fertilizer, and plant health."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=MODEL_NAME
        )

        return chat_completion.choices[0].message.content

    except Exception:
        return local_farming_fallback(prompt)
        