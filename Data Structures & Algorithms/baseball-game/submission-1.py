
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        total = 0
        stack = []
        for i in range(len(operations)):
            if operations[i] == 'D':
                num = stack[-1] * 2
                total += num
                stack.append(num)
            elif operations[i] == 'C':
                total-=stack.pop()
            elif operations[i] == '+':
                number1 = stack.pop()
                number2 = stack.pop()
                stack.append(number2)
                stack.append(number1)
                total+= number1+ number2
                stack.append(number1+ number2)
            else:
                num = int(operations[i])
                total+= num
                stack.append(num)
        return total