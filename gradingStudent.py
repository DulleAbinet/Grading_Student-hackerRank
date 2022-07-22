def gradingStudents(grades):
    # Write your code here
    new_grade = []
    for i in range(len(grades)):
        if grades[i] % 5 == 0 and grades[i]>=40:
            new_grade.append(grades[i])
        elif grades[i] > 37 and grades[i] %5 != 0:
            k=1
            temp = grades[i]
            while k < 3 and (temp - grades[i]) < 3 :
                
                temp = grades[i] + k
                k +=1
                if temp % 5 == 0 :
                    new_grade.append(temp)
                    break
            else:
                new_grade.append(grades[i])
               
        else:
            new_grade.append(grades[i])
    return new_grade
                
