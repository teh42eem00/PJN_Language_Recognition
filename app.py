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
    results = detect_language(text)
    return render_template('index.html', text=text, results=results)


def detect_language(text):
    predictions = model.predict(text, k=2)
    results = []
    for label, probability in zip(predictions[0], predictions[1]):
        language = label.replace('__label__', '')
        results.append({'language': language, 'probability': probability})
    return results


if __name__ == '__main__':
    app.run()
