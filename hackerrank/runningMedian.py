#https://www.hackerrank.com/challenges/find-the-running-median/problem
#
# Complete the runningMedian function below.
#
def runningMedian(a):
    def mean(a, b):
        return round((a + b) / 2, 1)

    numberList = []
    result = []
    odd = True
    firstIndex = 0
    secondIndex = 1
    for number in a:
        numberList.insert(bisect.bisect(numberList, number), number)
        # inserted = False
        # for i in range(len(numberList)):
        #    if number < numberList[i]:
        #        inserted = True
        #        numberList.insert(i,number)
        #        break
        # if not inserted:
        #    numberList.append(number)

        if not odd:
            oneNumber = numberList[firstIndex]
            otherNumber = numberList[secondIndex]
            median = float(mean(oneNumber, otherNumber))
            result.append(median + 0.0)
            odd = True
            firstIndex = firstIndex + 1
            secondIndex = secondIndex + 1
        else:
            median = float(round(numberList[firstIndex], 1))
            result.append(float(median))
            odd = False
    return result
    #
    # Write your code here.
    #
