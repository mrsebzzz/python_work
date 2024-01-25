from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What was your first programming lanauge?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("\nEneter 'q' to quit.\n")
while True:
    response = input("Lanauge: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results
print(f"\nThank you for participating.")
language_survey.show_results()