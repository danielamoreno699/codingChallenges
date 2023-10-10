def multiply(self, num1: str, num2: str) -> str:
            num = ['0','1','2','3','4','5','6','7','8','9']
            start1 = 1
            start2 = 1
            first = 0
            second = 0
            for i in reversed(num1):
                first+= start1 * num.index(i)
                start1 = start1 * 10
            for i in reversed(num2):
                second+= start2 * num.index(i)
                start2 = start2 * 10
            return str(first * second)