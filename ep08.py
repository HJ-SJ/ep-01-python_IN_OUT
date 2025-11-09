# 모듈과 페키지
# def greet(name) -> communication_module
# def farewall(name) -> communication_module
# def add_numbers(num1, num2) - math_module
# def multiply_numbers(num1, num2) - math_module
# def divide_numbers(num1, num2) - math_module
# my_package에 communication_module와 math_module를 놓어준다
import numpy
import matplotlib.pyplot as plt
from my_package import greet, multiply_numbers
from my_package import farewell as fw
# alt+ enter 패키지 함수 가져오기
greet("국진맨")

fw("국민맨2")

multiply_numbers(2,4)
x = numpy.linspace(0,10,100);
plt.plot(x, numpy.sin(x), label='sine', color='blue')
plt.show()
