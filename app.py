# This application uses the FastText library for language recognition.
# FastText is based on the work of A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov.
# For more details, please refer to the following papers:
# [1] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, "Bag of Tricks for Efficient Text Classification," arXiv preprint arXiv:1607.01759 (2016).
# [2] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, "FastText.zip: Compressing text classification models," arXiv preprint arXiv:1612.03651 (2016).
import os
import re

from flask import Flask, render_template, request

from language_detection import detect_language, train_own_model, load_176_model
from file_utils import process_file, process_test_set

app = Flask(__name__)

combined_file_path = 'static/combined.txt'
test_set_file_path = 'static/test_sentences.txt'
input_files = ['static/eng_sentences.tsv', 'static/pol_sentences.tsv', 'static/deu_sentences.tsv']
language_codes = ['en', 'pl', 'de']
num_records_test = 20000
num_records_learn = 50000

if os.path.exists(test_set_file_path):
    os.remove(test_set_file_path)

if os.path.exists(combined_file_path):
    os.remove(combined_file_path)

for input_file, language_code in zip(input_files, language_codes):
    process_test_set(input_file, test_set_file_path, language_code, num_records=num_records_test)
    process_file(input_file, combined_file_path, language_code, num_records=num_records_learn)

own_model = train_own_model()
model_176 = load_176_model()
own_model_test_results = own_model.test('static/test_sentences.txt')
pretrained_model_test_results = model_176.test('static/test_sentences.txt')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_text():
    text = request.form['text']
    text = re.sub(r'\n', ' ', text)
    results = detect_language(text, own_model, model_176)
    own_model_info = {
        'No. of validated records': own_model_test_results[0],
        'Precision': own_model_test_results[1],
        'Recall': own_model_test_results[2]
    }

    pretrained_model_info = {
        'No. of validated records': pretrained_model_test_results[0],
        'Precision': pretrained_model_test_results[1],
        'Recall': pretrained_model_test_results[2]
    }
    return render_template('index.html', text=text, results=results, models={
        'own_model_info': own_model_info,
        'pretrained_model_info': pretrained_model_info
    })


if __name__ == '__main__':
    app.run()
