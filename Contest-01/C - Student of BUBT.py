# function to check if a student passed all courses
def check_pass(min_scores, actual_scores):
    for i in range(len(min_scores)):
        if actual_scores[i][1] + actual_scores[i][2] + actual_scores[i][3] < min_scores[i]:
            return "FAIL"
    return "PASS"

t = int(input()) # number of test cases

for _ in range(t):
    n = int(input()) # number of courses
    min_scores = [] # minimum scores needed for each course
    actual_scores = [] # actual scores of the student in each course
    
    for i in range(n):
        scores = list(map(int, input().split()))
        min_scores.append(scores[0])
        actual_scores.append(scores)
    
    print(check_pass(min_scores, actual_scores))
