# This application uses the FastText library for language recognition.
# FastText is based on the work of A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov.
# For more details, please refer to the following papers:
# [1] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, "Bag of Tricks for Efficient Text Classification," arXiv preprint arXiv:1607.01759 (2016).
# [2] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, "FastText.zip: Compressing text classification models," arXiv preprint arXiv:1612.03651 (2016).


from flask import Flask, render_template, request
import fasttext

app = Flask(__name__)
own_model = fasttext.train_supervised(input='static/combined.txt', label_prefix="__label__", epoch=25, lr=0.1,
                                      wordNgrams=1, bucket=2000000, dim=300, thread=2)
model = fasttext.load_model('static/lid.176.ftz')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_text():
    text = request.form['text']
    results = detect_language(text)
    return render_template('index.html', text=text, results=results)


def detect_language(text):
    own_predictions = own_model.predict(text, k=2)
    own_results = []
    for label, probability in zip(own_predictions[0], own_predictions[1]):
        language = label.replace('__label__', '')
        own_results.append({'language': language, 'probability': probability})

    pretrained_predictions = model.predict(text, k=2)
    pretrained_results = []
    for label, probability in zip(pretrained_predictions[0], pretrained_predictions[1]):
        language = label.replace('__label__', '')
        pretrained_results.append({'language': language, 'probability': probability})

    return {'own_model': own_results, 'pretrained_model': pretrained_results}


if __name__ == '__main__':
    app.run()
