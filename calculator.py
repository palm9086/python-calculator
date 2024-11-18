class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        stage = 0
        if a<0 :
            a = abs(a)
            stage +=1
        if b<0 :
            b = abs(b)
            stage +=1
        for i in range(b):
            result = self.add(result, a)
        if stage == 1 :
            result = self.subtract(0, result)
        return result

    def divide(self, a, b):
        result = 0
        stage = 0
        if b != 0 :
            if a<0 :
                a = abs(a)
                stage +=1
            if b<0 :
                b = abs(b)
                stage +=1
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            if stage == 1 :
                result = self.subtract(0, result)
        else :
            result = "Error"
        return result
    
    def modulo(self, a, b):
        stage = 0
        if b !=0 :
            if a<0 :
                a = abs(a)
                stage = stage+1
            if b<0 :
                b = abs(b)
                stage = stage+2
            while a >= b:
                a = a-b
            if stage == 1 :
                a = b-a
            elif stage == 2 :
                a = a-b
            elif stage == 3 :
                a = -a
        else:
            a = "Error"
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(-10, -3))