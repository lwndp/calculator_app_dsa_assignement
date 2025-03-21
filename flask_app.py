from flask import Flask, render_template, request

from helper import perform_calculation, convert_to_float

from classes import Circle

app = Flask(__name__)  # create the instance of the flask class

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/calculate', methods=['GET', 'POST'])  # associating the GET and POST method with this route
def calculate():
    if request.method == 'POST':
        # using the request method from flask to request the values that were sent to the server through the POST method
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        # make sure the input is one of the allowed inputs (not absolutely necessary in the drop-down case)
        if operation not in ['add', 'subtract', 'divide', 'multiply']:
            return render_template('calculator.html',
                                   printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

        try:
            value1 = convert_to_float(value=value1)
            value2 = convert_to_float(value=value2)
        except ValueError:
            return render_template('calculator.html', printed_result="Cannot perform operation with this input")

        try:
            result = perform_calculation(value1=value1, value2=value2, operation=operation)
            return render_template('calculator.html', printed_result=str(result))

        except ZeroDivisionError:
            return render_template('calculator.html', printed_result="You cannot divide by zero")

    return render_template('calculator.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    if request.method == 'POST':
        try:
            # Get radius and convert to float
            radius = request.form['radius']
            radius = convert_to_float(value=radius)
            
            # Check if radius is positive
            if radius <= 0:
                return render_template('circle.html', error="Radius must be a positive number")
                
            circle = Circle(radius=radius) # create a circle object
            result = {
                "perimeter": round(circle.calculate_perimeter(), 3),
                "area": round(circle.calculate_area(), 3),
                "radius": round(radius, 3)
            }
            
            return render_template('circle.html', result=result)
            
        except ValueError:
            return render_template('circle.html', error="Please enter a valid number for radius")
        except Exception as e:
            return render_template('circle.html', error=f"An unexpected error occurred: {str(e)}")

    return render_template('circle.html')