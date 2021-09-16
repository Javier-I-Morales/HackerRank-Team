import statistics as stats
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(float(stats.mean(list(student_marks[query_name])))))


#print('{:.2f}'.format(n))

#print(f'{n:.2f}')

#print(f"{n:.{decimals}f}")