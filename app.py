# This application uses the FastText library for language recognition.
# FastText is based on the work of A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov.
# For more details, please refer to the following papers:
# [1] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, "Bag of Tricks for Efficient Text Classification," arXiv preprint arXiv:1607.01759 (2016).
# [2] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, "FastText.zip: Compressing text classification models," arXiv preprint arXiv:1612.03651 (2016).


from flask import Flask, render_template, request
import fasttext

app = Flask(__name__)
model = fasttext.load_model('lid.176.ftz')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_text():
    text = request.form['text']
    result = detect_language(text)
    return render_template('index.html', text=text, result=result)


def detect_language(text):
    prediction = model.predict(text)
    language = prediction[0][0].replace('__label__', '')
    probability = prediction[1][0]
    return {'language': language, 'probability': probability}


if __name__ == '__main__':
    app.run()
