def get_test_score(answer_sheet, student_answers):
    student_score = 0
    for i in range(0, len(student_answers)):
        if student_answers[i] == answer_sheet[i]:
            student_score += 1
            
    return (student_score / len(answer_sheet)) * 100
