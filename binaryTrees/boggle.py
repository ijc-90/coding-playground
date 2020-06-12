import copy

class Boggle():
  def __init__(self, grid):
    self.grid = grid
    self.height = len(grid)
    self.width = len(grid[0])

  def _getNeighbours(self, i, j):
    def returnHigher(number, limit):
      if number + 1 >= limit:
        return limit-1
      else:
        return number+1

    def returnLower(number, limit=0):
      if number - 1 < limit:
        return 0
      else:
        return number - 1

    result = []
    iMin = returnLower(i)
    iMax = returnHigher(i, self.width)
    jMin = returnLower(j)
    jMax = returnHigher(j, self.height)
    for x in range (iMin, iMax+1):
      for y in range(jMin, jMax+1):
        result.append([x,y])
    return result

  def _checkWord(self, i, j, word, usedPairs = []):
    if self.grid[i][j] != word[0]:
      return False
    if self.grid[i][j] == word[0] and len(word) == 1:
      return True;
    found = False
    for n in self._getNeighbours(i,j):
      if len(list(filter( lambda x: x[0] == n[0] and x[1]== n[1],usedPairs))) == 0:
        usedPairsCopy = copy.deepcopy(usedPairs)
        usedPairsCopy.append([i,j])
        found = self._checkWord(n[0],n[1], word[1:], usedPairsCopy)
        if found: return True
    return False

  def hasWord(self, word):
    for i in range(self.width):
      for j in range(self.height):
        if self._checkWord(i,j,word):
          return True
    return False

  def hasWords(self,words):
    result = []
    for word in words:
      if self.hasWord(word):
        result.append(word)
    return result


bla = {"1": "Sachin Tendulkar", "2": "Dravid", "3": "Sehwag", "4": "Laxman", "5": "Kohli"}
print(bla)
bla =dict( {"1": "Sachin Tendulkar", "2": "Dravid", "3": "Sehwag", "4": "Laxman", "5": "Kohli"})
bla = {"1": "Sachin Tendulkar", "2": "Dravid", "3": "Sehwag", "4": "Laxman", "5": "Kohli"}
[].pop()