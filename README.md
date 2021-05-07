# coprh-nlp-2021
Colorado Pragmatic Research in Health 2021 Conference: May 24 - 26, 2021

Natural Language Processing

## Notes about presentation

* Pragmatic approach to research - reuse existing data where possible; avoid primary data collection
* Uses of NLP - not necessarily how to do NLP
* How to apply NLP to audience's research
* Who can help attendees learn more about NLP or use NLP in their research project.
* Dr. Kwan speaking about social media for research at same time as my presentation
* Should have quiz questions, questions to ponder, exercises, etc. to keep audience engaged.
## How to setup python

Download Anaconda python distribution from: https://www.anaconda.com/products/individual#Downloads

Then run the following steps

```bash
conda create -n coprh python=3.7
conda activate coprh
conda config --add channels conda-forge
#conda install -c fastai fastbook sentencepiece
conda install -c conda-forge rise jupyter_nbextensions_configurator jupytext jupyterlab
conda install -c fastchan fastai
jupyter nbextension enable hide_input/main
```

## Items to improve

* Explain more detail about how Deep Learning works - language model building step by step.
* Sentence detection is an important part of NLP
* NLP is a multi-step process. Show a diagram and explain. See email from Chris RE: UIMA
* NLP is not simple or easy. You wont be an NLP expert after this presentation.
* Maybe include something about http://bionlp-corpora.sourceforge.net/CRAFT/ or similar projects
