import os 
os.system('cls')

def solution(triangle):
    if len(triangle) == 1 : return triangle[0];
    
    def dp(level) :
        if level == len(triangle) : return;

        for i in range(len(triangle[level])) :
            if i == 0 :
                triangle[level][0] += triangle[level-1][0]
            elif i == len(triangle[level]) - 1 :
                triangle[level][i] += triangle[level -1][-1]
            else :
                triangle[level][i] += max(triangle[level - 1][i-1], triangle[level - 1 ][i])
        dp(level+1)
    dp(1)
    return max(triangle[len(triangle)-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))