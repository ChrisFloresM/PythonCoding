if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # El asterisco significa que es posible pasar multiples argumentos (packaging)
        name, *line = input().split()
        # Tomamos los score, con map los convertimos en float y con list obtenemos la lista de floats
        scores = list(map(float, line))
        # Al elemento del diccionario con el nombre, le asignamos la lista de scores
        student_marks[name] = scores

    query_name = input()
    sum = 0
    # iteramos en la lista de scores para sumar los valores en ella
    for i in range(len(student_marks[query_name])):
        sum += student_marks[query_name][i]
    # calculamos el promedio
    avg = sum / len(student_marks[query_name])
    print(f"{avg:.2f}")
