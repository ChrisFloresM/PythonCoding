if __name__ == '__main__':

    student_list = []
    student_names = []
    student_scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
        student_scores.append(score)

    second_lowest = sorted(set(student_scores))[1]

    for i in range(len(student_list)):
        if (student_list[i].pop(1) == second_lowest):
            student_names.append(student_list[i][0])

    for i in range(len(student_names)):
        print(student_names[i])
