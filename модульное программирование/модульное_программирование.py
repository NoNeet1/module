import unittest
class Calculator: #функции калькулятора
    def __init__(self):
        pass
    def add(self,x1,x2): #сложение
        return int(x1)+int(x2)
    def subtract(self,x1,x2): #вычитание
        return int(x1)-int(x2)
    def multiply(self,x1,x2): #умножение
        return int(x1)*int(x2)
    def divide(self,x1,x2):#деление
        if int(x2)!=0:
            return int(x1)/int(x2) 
        else:
            raise ZeroDivisionError("IllegalArgumentException") #вызов исключения при делении на 0
        
  
        
class TestCalculator(unittest.TestCase): #проверка функций class Calculator
    def setUp(self):
        self.calculator = Calculator()
    def test_add1(self): #проверка сложения положительных и отрицательных чисел
        self.assertEqual(self.calculator.add(5,5),10) 
        self.assertEqual(self.calculator.add(-5,-5),-10)
    def test_subtract1(self): #проверка вычитания положительных и отрицательных чисел
        self.assertEqual(self.calculator.subtract(10,5),5)
        self.assertEqual(self.calculator.subtract(-10,-5),-5)
    def test_multiply1(self): #проверка умножения положительных и отрицательных чисел
        self.assertEqual(self.calculator.multiply(10,5),50)
        self.assertEqual(self.calculator.multiply(-10,-5),50)
    def test_divide1(self): #проверка деления положительных и отрицательных чисел
        with self.assertRaises(ZeroDivisionError): #исключение для 0
            self.calculator.divide(10, 0)
        self.assertEqual(self.calculator.divide(50,2),25)
        self.assertEqual(self.calculator.divide(-50,-2),25)
       

class main: #основной код
    calc=Calculator()
    y1=input('x1= ')
    y2=input('x2= ')
    y3=input('+/-/*/% (1/2/3/4): ') #на выбор даётся сложение(цифра 1), вычитание(цифра 2), умножение(цифра 3), деление(цифра 4)
    if int(y3)==1:
        y3=calc.add(y1,y2)
        print(y3)
    elif int(y3)==2:
        y3=calc.subtract(y1,y2)
        print(y3)
    elif int(y3)==3:
        y3=calc.multiply(y1,y2)
        print(y3)
    elif int(y3)==4:
        y3=calc.divide(y1,y2)
        print(y3)
        
if __name__=="__main__":
    unittest.main()
    main()