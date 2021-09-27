from flask import Flask, request
from flask_restful import Resource, Api
from random import randrange
from time import sleep

MEGA=1024*1024

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/error/<int:number>')
def error_load(number):
  returnString = 'Hello World!' 
  if randrange(number) == 1:
    returnString = returnString, 418
  return returnString

@app.route('/loop/<int:number>')
def loop_load(number):
  i = 0
  while i < number:
     j = 0 
     while j < MEGA:
       j += 1  
     i += 1  
  return 'Hello World!'

@app.route('/memory/<int:number>')
def memory_load(number):
  i = 0
  while i < number:
    try:
      a = ' ' * (i * MEGA)
      del a
    except MemoryError:
      break
    i += 1
  return 'Hello World!'

@app.route('/slow/<int:number>')
def slow_load(number):
  sleep(randrange(number)/1000)
  return 'Hello World!'

if __name__ == '__main__':
  app.run('0.0.0.0','3333')
