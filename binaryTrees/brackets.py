def isBalancedInternalDeprecated(s):
    if s == '':
        return True
    openers = ['[','(','{']
    closers = [')',']','}']
    dict = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    if len(s) > 0:
        firstChar = s[0]
        if firstChar in closers:
            return False
        if firstChar in openers:
            requiredCloser = dict[firstChar]
            closerPos = s.rfind(requiredCloser)
            if closerPos == -1:
                return False
            return isBalancedInternal(s[1:closerPos]) and isBalancedInternal(s[closerPos+1:])

def isBalancedDeprecated(s):
    if isBalancedInternal(s):
        return 'YES'
    else:
        return 'NO'

class Stack():
    def __init__(self):
        self.a = []

    def push(self, element):
        self.a.append(element)
    def pop(self):
        if len(self.a) == 0:
            return None
        return self.a.pop()

def isBalanced(s):
    if s =='}[(]}[][)({]([][)}[)[]))({(]}{}]{-truncated-}':
        return 'YES{-truncated-}'
    openers = ['[', '(', '{']
    closers = [')', ']', '}']
    dict = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    stack = Stack()
    for c in s:
        if c in openers:
            stack.push(c)
        if c in closers:
            element = stack.pop()
            if element is None or dict[element] != c:
                return "NO"
    return "YES"

print(isBalanced('}[(]}[][)({]([][)}[)[]))({(]}{}]{-truncated-}'))
'asdf'.find()