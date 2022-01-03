def solution(genres, plays):
    genreName = []
    genreName.append([genres[0]])

    classifyGenre(genreName, genres, plays)
    genrePlays = sumPlays(genreName)
    answer = makeAnswer(genrePlays, genreName, plays)

    return answer

def classifyGenre(genreName, genres, plays):
    # genres = [genre0, genre1, genre2, ...]
    # genreName = [[genre0, plays0, plays1, ...], ... ]
    for i in range(len(genres)):
        for m in range(len(genreName)):
            if genres[i] == genreName[m][0]:
                genreName[m].append(plays[i])
                break
            if m == (len(genreName) - 1):
                genreName.append([genres[i], plays[i]])
    return genreName

def sumPlays(genreName):
    # genreName = [[genre0, plays0, plays1, ...], ... ]
    # genrePlays = [sum1, sum2, ...]
    sumPlays = []
    for j in genreName:
        sum = 0
        for k in range(1, len(j)):
            sum += j[k]
        sumPlays.append(sum)

    return sumPlays

def makeAnswer(genrePlays, genreName, plays):
    answer = []
    # genreName = [[genre0, index0, index1, ...], ... ]
    # genrePlays = [sum1, sum2, ...]
    for l in range(len(genrePlays)):
        genreIndex = genrePlays.index(max(genrePlays))
        genreName[genreIndex].pop(0)
        genreName[genreIndex].sort(reverse=True)
        indexes = genreName[genreIndex]

        # if the genre has only 1 music
        if len(indexes) == 1:
            answer.append(plays.index(indexes[0]))
            print(plays.index(indexes[0]))
        else:
            answer.append(plays.index(indexes[0]))
            plays[plays.index(indexes[0])] = 0

            answer.append(plays.index(indexes[1]))

        genreName.pop(genreIndex)
        genrePlays.pop(genreIndex)
    return answer



inputA = ["classic", "pop", "classic", "a", "classic", "pop"]
inputB = [800, 600, 500, 1, 800, 2500]


print(solution(inputA, inputB))