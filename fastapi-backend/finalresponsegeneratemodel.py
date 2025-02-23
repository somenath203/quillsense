import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)


chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Analyze the following data provided by the user: {  'fullName': 'Somenath',   'age': 23.0,   'noOfHoursSleep': 5.0,   'mood': 'Experiencing intense pressure, heightened anxiety, or emotional distress.',   'exercise': 'I've been exercising continuously for the past 3 days.',   'handwritingAnalysis': 'The handwriting exhibits relatively consistent line pressure and letter sizing, suggesting a calm and controlled emotional state.  Spacing between words is even, indicating a clear thought process and organization. The slightly cursive style implies a degree of fluency and comfort in expression. Overall, the handwriting suggests a relaxed and possibly introspective personality.\n'}. Based on this data, perform the following tasks: 1) Provide detailed handwriting insights. 2) Analyze the correlation between mood and potential stress triggers. 3) Generate personalized recommendations to improve overall well-being. 4) Summarize the analysis with a concise conclusion, using actionable language and referring to the user as 'you' instead of their real name. 5) Generate scoring data for handwriting aspects such as depth, stress, etc., with values between 0-100. 6) Generate future mood prediction data for the next 4 days starting tomorrow, with values between 0-100. 7) Provide a description for the handwriting scores graph, explaining what each aspect (e.g., depth, stress) indicates. 8) Provide a description for the future mood prediction graph, explaining how the values represent expected changes in mood over the next 4 days. Return the result as a valid JSON object. Format the values of each key using Markdown syntax. The structure should be: {  'handwritingInsights':     '# Handwriting Insights\\n\\n    **Details:**\\n\\n    - Bullet point 1 describing handwriting insights\\n    - Bullet point 2 describing handwriting insights',   'moodStressCorrelation':     '# Mood-Stress Correlation\\n\\n    **Analysis:**\\n\\n    - Bullet point 1 analyzing mood and stress correlation\\n    - Bullet point 2 analyzing mood and stress correlation',   'personalizedRecommendations':     '# Recommendations\\n\\n    - Recommendation 1 for improving well-being\\n    - Recommendation 2 for improving well-being\\n    - Recommendation 3 for improving well-being',   'summary':     '# Summary\\n\\n    **Summary Text Here:**\\n\\n    - Key point 1 summarizing the analysis\\n    - Key point 2 summarizing the analysis',   'conclusion':     '# Conclusion\\n\\n    **Actionable Steps:**\\n\\n    - Step 1 for actionable improvement\\n    - Step 2 for actionable improvement\\n    - Step 3 for actionable improvement',   'handwritingScores':     '{      \"labels\": [\"Depth\", \"Stress\", \"Pressure\", \"Slant\", \"Speed\"],       \"datasets\": [{        \"data\": [Dynamic values generated by the model]       }],       \"description\": \"This graph evaluates handwriting aspects such as depth, stress, pressure, slant, and speed. Each score (0-100) reflects the handwriting quality and underlying factors like emotional state, attention to detail, and stress levels.\"     }',   'futureMoodPrediction':     '{      \"labels\": [\"Tomorrow\", \"Day 2\", \"Day 3\", \"Day 4\"],       \"datasets\": [{        \"data\": [Dynamic values generated by the model]       }],       \"description\": \"This graph predicts the user’s mood for the next 4 days based on current data. Each value (0-100) represents expected mood stability, positivity, or potential challenges.\"     }' }.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"handwritingInsights\": \"# Handwriting Insights\\n\\n**Details:**\\n\\n- The consistent line pressure and letter sizing suggest a generally calm and controlled emotional state, despite reported feelings of pressure and anxiety.\\n- Even spacing between words indicates a clear thought process and organization, which is a positive indicator of mental clarity.\\n- The slightly cursive style implies fluency and comfort in self-expression, suggesting a degree of confidence.\\n- Overall, the handwriting presents a somewhat paradoxical picture:  a relaxed and introspective personality is suggested, which may contrast with the reported intense pressure and anxiety.\",\n  \"moodStressCorrelation\": \"# Mood-Stress Correlation\\n\\n**Analysis:**\\n\\n- There's a clear discrepancy between the reported mood ('Experiencing intense pressure, heightened anxiety, or emotional distress.') and the handwriting analysis, which suggests a calm and controlled emotional state. This discrepancy indicates potential emotional suppression or a delay in the manifestation of emotional stress in the handwriting.\\n- The reported consistent exercise over the past 3 days could be a coping mechanism for stress, or it could be unrelated to the current emotional state. Further investigation is needed to understand the relationship between the reported mood, exercise, and sleep patterns.\",\n  \"personalizedRecommendations\": \"# Recommendations\\n\\n- **Prioritize sleep:** Aim for 7-8 hours of sleep per night to improve mood regulation and stress management.  Your current 5 hours is significantly below the recommended amount.\\n- **Mindfulness and stress management techniques:** Explore mindfulness practices like meditation or deep breathing exercises to help manage anxiety and emotional distress. Consider professional guidance if needed.\\n- **Journaling:** Regularly recording your thoughts and feelings can help process emotions and gain better self-awareness, potentially revealing underlying stressors that might not be immediately apparent.\",\n  \"summary\": \"# Summary\\n\\n**Summary Text Here:**\\n\\n- You are reporting significant emotional distress despite exhibiting handwriting characteristics suggesting a calm demeanor. This discrepancy needs further investigation.\\n- Your sleep deprivation and potentially suppressed emotions are significant factors influencing your well-being.  Regular exercise is a positive attribute, but it needs to be combined with effective stress management techniques.\",\n  \"conclusion\": \"# Conclusion\\n\\n**Actionable Steps:**\\n\\n- Prioritize improving sleep hygiene to reach 7-8 hours of sleep per night.\\n- Implement daily mindfulness practices or seek professional guidance for anxiety management.\\n- Maintain your current exercise routine and combine it with the above recommendations for a holistic approach to well-being.\",\n  \"handwritingScores\": \"{      \\\"labels\\\": [\\\"Depth\\\", \\\"Stress\\\", \\\"Pressure\\\", \\\"Slant\\\", \\\"Speed\\\"],       \\\"datasets\\\": [{        \\\"data\\\": [70, 30, 65, 50, 75]       }],       \\\"description\\\": \\\"This graph evaluates handwriting aspects such as depth, stress, pressure, slant, and speed. Each score (0-100) reflects the handwriting quality and underlying factors like emotional state, attention to detail, and stress levels.\\\"     }\",\n  \"futureMoodPrediction\": \"{      \\\"labels\\\": [\\\"Tomorrow\\\", \\\"Day 2\\\", \\\"Day 3\\\", \\\"Day 4\\\"],       \\\"datasets\\\": [{        \\\"data\\\": [60, 65, 70, 75]       }],       \\\"description\\\": \\\"This graph predicts the user’s mood for the next 4 days based on current data. Each value (0-100) represents expected mood stability, positivity, or potential challenges.\\\"     }\"\n}\n```\n",
      ],
    },
  ]
)


def generate_final_response(prompt):

    response = chat_session.send_message(prompt)

    return response.text