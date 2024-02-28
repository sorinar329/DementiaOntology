from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the selected checkboxes from the form
    selected_options = request.form.getlist('checkbox')

    # Do something with the selected options (for example, print them)
    print('Selected Options:', selected_options)

    # You can process the selected options further and return a response

    return render_template('result.html', selected_options=selected_options)

if __name__ == '__main__':
    app.run(debug=True)
