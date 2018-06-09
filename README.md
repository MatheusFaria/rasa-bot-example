# Rasa bot test

Small test bots using rasa-core and rasa-nlu

```
sudo docker build -t bot-test .
sudo docker run --rm -it -v $PWD/bot:/bot bot-test
```
