from python:3

env TRAINING_EPOCHS=300

run apt-get install -y git

run git clone https://github.com/RasaHQ/rasa_core.git  && \
    cd rasa_core                                       && \
    pip install -r requirements.txt                    && \
    pip install -e .

run git clone https://github.com/RasaHQ/rasa_nlu.git                && \
    cd rasa_nlu                                                     && \
    pip install -r alt_requirements/requirements_spacy_sklearn.txt  && \
    pip install -e .                                                && \
    python -m spacy download en


add ./bot /bot

cmd python -m rasa_nlu.train                \
           --config /bot/config.yml         \
           --data   /bot/data/nlu_data.md   \
           --fixed_model_name current       \
           --path /models                   \
           --project nlu                    && \
    python -m rasa_core.train      \
           -s /bot/data/stories.md \
           -d /bot/domain.yml      \
           -o /models/dialogue     \
           --epochs ${TRAINING_EPOCHS}      && \
    python -m rasa_core.run        \
           -d /models/dialogue     \
           -u /models/nlu/current
