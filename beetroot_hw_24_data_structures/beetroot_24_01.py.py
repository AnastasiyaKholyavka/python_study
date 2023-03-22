'''

Task 1

Write a program that reads in a sequence of characters and prints them in 
reverse order, using your implementation of Stack.

'''

# Створити структуру стек
# Створити новий список з елементів у зворотному порядку і друкувати його 

class Numbers:
    def __init__(self, data_stack: list): # Створила стек і порожній стек, у який перекину елементи для зворотного порядку
        self.data_stack = data_stack        
        self.reversed_stack = []
             
    def reversed_stack(self):
        for elem in self.data_stack:
            while len(self.data_stack) != 0: 
                self.reversed_stack.push(elem) # Кожен елемент стеку переношу в порожній стек доти, поки попередній стек не стане порожнім
                #return self.reversed_stack
    def __str__(self) -> str:
        return str(reversed_stack)           
    
        
'''
if __name__ == 'main':
    return reversed_stack
'''

reversed_stack = Numbers([1, 5, 9, 3, 26, 7, 9])     

print(reversed_stack) # ---> Виходить таке: <__main__.Numbers object at 0x000001C709457BB0>