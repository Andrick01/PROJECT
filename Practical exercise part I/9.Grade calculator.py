def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score! Please enter a value between 0 and 100."
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

subjects=[None]*5
for i in range(5):
    subjects[i]=int(input(f"Enter mark {i+1}:"))

average_score = sum(subjects) / len(subjects)
grade = calculate_grade(average_score)

print(f"Average: {average_score:.2f}% | Final Grade: {grade}")