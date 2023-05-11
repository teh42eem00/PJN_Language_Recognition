# This application uses the FastText library for language recognition.
# FastText is based on the work of A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov.
# For more details, please refer to the following papers:
# [1] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, "Bag of Tricks for Efficient Text Classification," arXiv preprint arXiv:1607.01759 (2016).
# [2] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, "FastText.zip: Compressing text classification models," arXiv preprint arXiv:1612.03651 (2016).


from flask import Flask, render_template, request
import fasttext

app = Flask(__name__)


@app.route('/')
def index():
    en_text = "Hello, how are you doing this beautiful day?"
    detected_language = detect_language(en_text)
    print(detected_language)
    language = detected_language[0][0].replace('__label__', '')
    probability = str(detected_language[1][0])
    return "Detected languages:" + language + ", Probability: " + probability
    # return render_template('index.html')


def detect_language(text):
    # Predict the language using the predict function of the FastText object
    model = fasttext.load_model('lid.176.ftz')
    result = model.predict(text, k=1)
    # Return the detected language label and probability
    return result


if __name__ == '__main__':
    app.run()
