from flask import Flask, jsonify, render_template

app = Flask(__name__)

todays_learning = [{
    'day': 1,
    'topic':
    'flask,html,css,how to get the website on browser and push changes commit in git image render ,use bootstarp',
    'leature': 1
}, {
    'day': 2,
    'topic':
    'till now i have learn is jinja some basic of it and in title it is return as cloud Deployment ',
    'leature': 2
}, {
    'day': 3,
    'topic': '''
    tried deplpymening but second time when i use it.it dose not shows image need to find out why''',
    'leature': 3
}, {
    'day': 4,
    'topic': 'needed to be updated by me today',
    'leature': 4
}, {
    'day': 5,
    'topic': 'needed to be updated by me today',
    'leature': 5
}]


@app.route('/')
def fun():
    return render_template('index.html',
                           todays_learning=todays_learning,
                           owner="Sachin")


@app.route('/learnings')
def Api_caLL():
    return jsonify(todays_learning)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
