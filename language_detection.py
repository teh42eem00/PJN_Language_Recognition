import fasttext


def train_own_model():
    return fasttext.train_supervised(input='static/combined.txt', label_prefix="__label__", epoch=25, lr=0.1,
                                     wordNgrams=1, bucket=2000000, dim=300, thread=4)


def load_176_model():
    return fasttext.load_model('static/lid.176.ftz')


def detect_language(text, own_model, pretrained_model):
    own_predictions = own_model.predict(text, k=2)
    own_results = [
        {'language': label.replace('__label__', ''), 'probability': probability}
        for label, probability in zip(own_predictions[0], own_predictions[1])
    ]

    pretrained_predictions = pretrained_model.predict(text, k=2)
    pretrained_results = [
        {'language': label.replace('__label__', ''), 'probability': probability}
        for label, probability in zip(pretrained_predictions[0], pretrained_predictions[1])
    ]

    return {'own_model': own_results, 'pretrained_model': pretrained_results}
