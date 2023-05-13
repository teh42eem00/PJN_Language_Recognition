# Language Recognition using FastText

This is an application used to recognize text language using FastText library. In this project we tested precision of language guessing using "176 languages model" provided by FastText and model prepared by ourselves.


## Tech Stack

Project is created with:

- Python 3.11
- Flask 2.3.2
- FastText 0.9.2
- Docker
- Docker 3.11-slim-bullseye Debian image
- HTML
- CSS - Materialize Framework

## Run Locally

Clone the project

```bash
  git clone https://github.com/teh42eem00/PJN_Language_Recognition
```

Go to the project directory

```bash
  cd PJN_Language_Recognition
```

Install docker according to your operating system

https://docs.docker.com/engine/install/

Build docker image

```bash
  docker build -t pjn_language_recognition .
```

Start the docker image

```bash
  docker run -p 5000:5000 --name pjn_language_recognition -d pjn_language_recognition
```

That's it, application should listen on port 5000 of Docker host IP address.



## Authors

- [@teh42eem00](https://www.github.com/teh42eem00)
- [@mpieczara97](https://www.github.com/mpieczara97)
- Credits for sentences to [Tatoeba](https://tatoeba.org/)
- Credits for language models to A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, [Bag of Tricks for Efficient Text Classification](https://arxiv.org/abs/1607.01759)
- Credits for language models to A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, [FastText.zip: Compressing text classification models](https://arxiv.org/abs/1612.03651)
