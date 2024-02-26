def get_test_score(answer_sheet, student_answers):
    name = student_answers[0]
    student_score = 0
    for i in range(1, len(student_answers)):
        if answer_sheet[i - 1] == student_answers[i]:
            student_score += 1
    percentage = student_score / len(answer_sheet) * 100
    return name, percentage
