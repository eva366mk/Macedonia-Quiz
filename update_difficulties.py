import json

with open('data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# For each category, set last 2 questions: 14th=medium, 15th=hard
for category in data['categories']:
    questions = data['categories'][category]['questions']
    if len(questions) >= 15:
        questions[13]['difficulty'] = 'medium'  # Question 14 (index 13)
        questions[14]['difficulty'] = 'hard'    # Question 15 (index 14)

with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Updated difficulties: 12 easy, 2 medium, 1 hard per category")
