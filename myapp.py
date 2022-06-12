#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import bottle
from bottle import route,run

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

bottle.debug(True)

@route('/')
def index():
	return "<h1>Hola Mundo, esto sera una calculadora web, probablemente!!!</h1>"


if __name__ == '__master__':
	run(host='127.0.0.1',port=8000)


#if __name__ == '__main__':
#	run(host='0.0.0.0', port=argv[1])