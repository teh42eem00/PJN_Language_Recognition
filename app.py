# This application uses the FastText library for language recognition.
# FastText is based on the work of A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov.
# For more details, please refer to the following papers:
# [1] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, "Bag of Tricks for Efficient Text Classification," arXiv preprint arXiv:1607.01759 (2016).
# [2] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, "FastText.zip: Compressing text classification models," arXiv preprint arXiv:1612.03651 (2016).
import os

from flask import Flask, render_template, request

from language_detection import detect_language, train_own_model, load_176_model
from file_utils import process_file

app = Flask(__name__)

combined_file_path = 'static/combined.txt'
if os.path.exists(combined_file_path):
    os.remove(combined_file_path)

process_file('static/eng_sentences.tsv', 'en', 50000)
process_file('static/pol_sentences.tsv', 'pl', 50000)
process_file('static/deu_sentences.tsv', 'de', 50000)

own_model = train_own_model()
model_176 = load_176_model()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_text():
    text = request.form['text']
    results = detect_language(text, own_model, model_176)
    return render_template('index.html', text=text, results=results)


if __name__ == '__main__':
    app.run()
