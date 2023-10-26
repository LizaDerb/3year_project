from flask_app import app, db
from flask import render_template, request
from flask_app.search import get_results

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/instruction')
def instruction():
    return render_template('instruction.html')

@app.route('/search_query', methods=['post', 'get'])
def searching():
    message = ''
    if request.method == 'POST':
        written_search = request.form.get('written_search')
        results = get_results(written_search)
    return render_template('search_results.html', message=results)