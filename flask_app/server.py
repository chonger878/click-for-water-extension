from flask_app import app, render_template, session

if __name__ == '__main__':

    app.route('/', methods=['POST'])
    def form():
        if 'visit' not in session:
            print('Visit record does NOT exist!')
            session['visit'] = 0
        else:
            print('Another visitor has seen this page')
            session['visit'] += 1
        return render_template('index.html')

    app.run(debug = True)