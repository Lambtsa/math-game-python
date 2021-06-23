class Question: 
    answer = None
    text = None

    def __str__(self) -> str:
        return f'{self.text}'


class Add(Question):
    def __init__(self, num1, num2):
        super().__init__()
        
        self.text = '{} + {}'.format(num1, num2)
        self.answer = num1 + num2


class Multiply(Question):
    def __init__(self, num1, num2):
        super().__init__()
        
        self.text = '{} x {}'.format(num1, num2)
        self.answer = num1 * num2

if __name__ == '__main__':
  pass
