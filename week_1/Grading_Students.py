#QUESTION
#https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    leng = len(grades)
    for i in range(leng):
        if grades[i] < 38:
            continue
        if ((5 - (grades[i] % 5)) >= 3):
            continue
        else:
            grades[i] += (5 - (grades[i] % 5))        
    return grades
