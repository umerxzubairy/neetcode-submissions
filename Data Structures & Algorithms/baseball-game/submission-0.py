
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == 'D':
                stack.append(stack[-1] * 2)
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == '+':
                number1 = stack.pop()
                number2 = stack.pop()
                stack.append(number2)
                stack.append(number1)
                stack.append(number1+ number2)
            else:
                stack.append(int(operations[i]))
        return sum(stack)