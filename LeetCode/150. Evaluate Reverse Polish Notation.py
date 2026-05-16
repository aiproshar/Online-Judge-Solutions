class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        oper = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token not in oper:
                stack.append(int(token))
            else:
                num_2 = stack[-1]
                stack.pop()
                num_1 = stack[-1]
                stack.pop()
                if token == '+':
                    stack.append(num_1 + num_2)
                if token == '-':
                    stack.append(num_1 - num_2)
                if token == '*':
                    stack.append(num_1 * num_2)
                if token == '/':
                    stack.append(math.trunc(num_1 / num_2))
        return stack[-1]


# More pythonic way, this is so beautiful
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        oper = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: math.trunc(x/y),
        }
        for token in tokens:
            if token in oper:
                num_2 = stack.pop()
                num_1 = stack.pop()
                evl = oper[token](num_1, num_2)
                stack.append(evl)
            else:
                stack.append(int(token))
        return stack[0]



