from flask import Blueprint, render_template, request, flash
import re

Templates = Blueprint('templates', __name__) 

counter = 0

@Templates.route('/', methods=['GET', 'POST'])
def home():
    global counter
    counter += 1
    data = request.form
    answer = data.get('answer')
    pattern = '\.0*'
    isOddOrEven: str = ''
    print(data)
    num = 0
    if counter > 1:
        match = re.search(pattern, answer)
        if match:
            answer = re.sub(pattern, '', answer)
        if answer == '':
            flash('Please enter a number', category='error')
        else:
            num = int(answer)
    if answer == '':
        pass
    elif (num % 2) != 0:
        isOddOrEven += f'"{num}" is ODD!'
    elif (num % 2) == 0:
        isOddOrEven += f'"{num}" is EVEN!'
    return render_template('home.html', ans=isOddOrEven, Counter=counter)
