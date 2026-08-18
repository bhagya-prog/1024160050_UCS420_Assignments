import pandas as pd 

# Q1 :Build your personalized knowledge base
fixed_enteries = [
    {"question":"What is the annual fee", "answer":"The annual fee is Rs.500",
    "keywords":"fee cost price charge", "category":"billing"},
    {"question":"how to reset password", "answer":"Go to Settings > Reset Password.",
    "keywords":"password reset login","category":"account"},
    {"question":"What are your working hours", "answer":"We are open 9 AM to 5 PM",
    "keywords":"hours timing open time","category":"general"},
    {"question":"how can I pay the fee","answer":"You can pay via UPI, card or net banking",
    "keywords":"pay paymnt upi fee", "category":"billing"},
]
roll_number = "1024160050"
last_two_digits = roll_number[-2:]
categories = ["billing", "account", "general"]
d1 = int(last_two_digits[0])
d2 = int(last_two_digits[1])
cat1 = categories[d1 % 3]  #5 % 3 = 2 => general
cat2 = categories[d2 % 3] #0 % 3 = 0 => billing
personalized_entries = [
    {"question":"How do I contact support?", "answer":"You can contact support via email or phone.",
    "keywords":"support help contact", "category":cat1},
    {"question":"What is the refund policy?", "answer":"You can request a refund within 30 days of purchase.",
    "keywords":"refund policy return", "category":cat2},
]
df = pd.DataFrame(fixed_enteries + personalized_entries)
print("Hence the final DataFrame is:")
print(df)

#Q2: Generate and score a hypothesis
def score_hypothesis(df, question):
    question_lower = question.lower()
    scores = []
    for index, row in df.iterrows():
        score = 0
        if row['question'].lower() == question_lower:
            score += 10  
        elif question_lower in row['question'].lower():
            score += 5 
        if any(keyword in question_lower for keyword in row['keywords'].lower().split()):
            score += 3 
        scores.append((row['question'], row['answer'], score))
    return sorted(scores, key=lambda x: x[2], reverse=True)

# Q3: Write a function that returns all questions belonging to a given category
def same_category(category_name, df):
    return df[df['category'] == category_name][['question']]

sample_category = personalized_entries[0]['category']
sample_questions = same_category(sample_category, df)
print(f"Questions in category '{sample_category}':")
print(sample_questions)

#Q4: Ask user to input new keyword and then add it to keywords and convert it to CSV file 
target = 0 
new_entry = input("Enter new keyword:")   # adding "spending" to keywords
current_keywords = df.loc[target, 'keywords']
df.loc[target, 'keywords'] = current_keywords + " " + new_entry
df.to_csv('Assignment_4/1024160050_faq_data.csv', index=False)

#Q5: How many FAQ entries are there in each category?
faq_count = df.groupby('category')['question'].count()
print(faq_count)

#Q6: Provide example of one with a tie and other without a tie query using score_hypothesis function
tie_query = "fee"
tie_results = score_hypothesis(df, tie_query)
for question, answer, score in tie_results:
    if score == tie_results[0][2]:
        print(f"  {question}: {answer} (Score: {score})")
print("Query that does not produce a tie:")
non_tie_query = "support"
non_tie_results = score_hypothesis(df, non_tie_query)
for question, answer, score in non_tie_results:
    print(f"  {question}: {answer} (Score: {score})")

