
array = [1,5,3]

scoreBoard= {}
def predictWinner(start, end, total):
    key = (start, end)
    
    if key not in scoreBoard:
        if start == end:
            scoreBoard[key] = array[start]
        else:
            scoreBoard[key] = max(total - predictWinner(start+1, end, total-array[start]),
                             total - predictWinner(start, end-1, total-array[end]))
    return scoreBoard[key]

total = sum(array)
result = predictWinner(0, len(array)-1, total)
print(result >= total/2)
print(scoreBoard)