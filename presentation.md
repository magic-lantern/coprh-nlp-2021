---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.1
  kernelspec:
    display_name: 'Python 3.8.5 64-bit (''nlp'': conda)'
    language: python
    name: python38564bitnlpconda558de9a36abb4155bca9bf25b4c81369
---

```python slideshow={"slide_type": "skip"}
from IPython.display import Image
```

<!-- #region slideshow={"slide_type": "slide"} -->
# Attics, guesswork and clay. Sleuthing your way into Biomedical Natural Language Processing

## Colorado Pragmatic Research in Health 2021 Conference<br/>May 24 - 26, 2021

<pre>
Seth Russell, MS
University of Colorado Anschutz Medical Campus
ACCORDS Data Science Program, D2V Data Science Core
</pre>
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Learning Objectives

Learners should have:

1. A general idea of what Natural Language Processing (NLP) is.
1. A knowledge of the ethical implications of data reuse in NLP.
1. Knowledge of where to get text for NLP.
1. How to use and learn more about some basic NLP techniques.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"} hide_input=true
Image(filename='./pictures/natgeo_2011.png') 
```

<!-- #region slideshow={"slide_type": "notes"} -->
Some of you may have heard of the many successes of Natural Language Processing. It has been highly lauded in the popular news as well as more academic circles for many years. One popular event about - described in this 2011 national geograpic article from 10 years ago was the match up of Jeopardy champion vs IBM's Question Answering system called "Watson" named for IBMs founder and first CEO Thomas J. Watson
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
Image(filename='./pictures/nyt_2020.png')
```

<!-- #region slideshow={"slide_type": "notes"} -->
More recently companies such as OpenAI - this image is from 2020 - have made additional breakthroughs that have caught popular imagination and fear in some cases for the ability for software to generate and appear to understand text.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"} hide_input=true
Image(filename='./pictures/wsj_2021.png')
```

<!-- #region slideshow={"slide_type": "notes"} -->
As with any technology sometimes the hype doesn't live up to reality and as shown in this February 2021 article, even the amazing Watson may have to be put to pasture like a has been race horse.

openai gpt-3 training at least 4.6 million in hardware costs + many people

https://bdtechtalks.com/2020/09/21/gpt-3-economy-business-model/
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## “Come, Watson, come!” he cried. “The game is afoot. Not a word! Into your clothes and come!”

The Adventure of the Abbey Grange  
Sir Arthur Conan Doyle
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "notes"} -->
After seeing and hearing of the amazing things NLP can do, everyone wants to get into the game and see immediate advantages.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## So what *is* Natural Language Processing ?

* Document Retrieval
* Information Extraction
* Knowledge Representation
* Word/Concept/Abbreviation disambiguation
* Automated reasoning
* Classification
* Sentiment Analysis
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "notes"} -->
* Document Retrieval - Google
* Information Extraction - This also can be seen in Google
* Knowledge Representation
* Word/Concept/Abbreviation disambiguation
* Automated reasoning
* Classification and sentiment analysis - Content management systems to identify problem videos, posts, etc. Youtube, Facebook, Twitter and others are doing this

<!-- #endregion -->

```python slideshow={"slide_type": "subslide"} hide_input=true
Image(filename='./pictures/google_information_extraction.png')
```

```python slideshow={"slide_type": "subslide"} hide_input=true
Image(filename='./pictures/wapost_2021.png')
```

<!-- #region slideshow={"slide_type": "slide"} -->
# Some common techniques

* Regular expressions
* Stemming
* Lemmatization
* Stop word removal
* Word to vector representations
* Language Modeling
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "notes"} -->
* Regular expressions - Text pattern matching language
* Stemming - Removing common endings to words such as 's', 'ed', 'ing' to get the word stem
* Lemmatization - 'to walk' may appear as 'walk', 'walked', 'walks' or 'walking'
* Stop word removal - Removing high frequency, low meaning words.
* Word to Vector - Most machine learning techniques require numeric input. There are various algorithms for converting words to numbers in a high dimensional vector space
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
##  “We are coming now rather into the region of guesswork,” said Dr. Mortimer.

## *Holmes' reply:* “Say, rather, into the region where we balance probabilities and choose the most likely. It is the scientific use of the imagination, but we have always some material basis on which to start our speculation.”

The Hound of the Baskervilles
Sir Arthur Conan Doyle
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "notes"} -->
What that little bit of information on what is considered NLP, where do we go now?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# ACM Code of Ethics and Professional Conduct

#### Association for Computing Machinery, 2018

Computing professionals' actions change the world. To act responsibly, they should reflect upon the wider impacts of their work, consistently supporting the public good. The ACM Code of Ethics and Professional Conduct ("the Code") expresses the conscience of the profession...
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->

## 1. GENERAL ETHICAL PRINCIPLES.

A computing professional should...

1. Contribute to society and to human well-being, acknowledging that all people are stakeholders in computing
1. Avoid harm.
1. Be honest and trustworthy.
1. Be fair and take action not to discriminate.
1. Respect the work required to produce new ideas, inventions, creative works, and computing artifacts.
1. Respect privacy.
1. Honor confidentiality.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
## 2. PROFESSIONAL RESPONSIBILITIES.
...

Continued at https://www.acm.org/code-of-ethics
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## I consider that a man’s brain originally is like a little empty attic, and you have to stock it with such furniture as you choose. 

A fool takes in all the lumber of every sort that he comes across, so that the knowledge which might be useful to him gets crowded out, or at best is jumbled up with a lot of other things so that he has a difficulty in laying his hands upon it. Now the skilful workman is very careful indeed as to what he takes into his brain-attic. He will have nothing but the tools which may help him in doing his work, but of these he has a large assortment, and all in the most perfect order. It is a mistake to think that that little room has elastic walls and can distend to any extent. Depend upon it there comes a time when for every addition of knowledge you forget something that you knew before. It is of the highest importance, therefore, not to have useless facts elbowing out the useful ones.

A Study In Scarlet  
Sir Arthur Conan Doyle
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "notes"} -->
Historically, NLP systems were rule based - either rules based on grammar or rules based on matching specific words and phrases. Any domain expert can identify common words and phrases that could be used to identify specific elements in text for example. More specialized NLP experts where often Linguists - computational linguists - who codified rules of English and created complex sentence parse trees to then identify where information of a certain type would be found. It's my semi-educated guess that the rule based type of NLP is probably the most common and most popular.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
import re

get_subsections_pat = re.compile(r'(^[\w\s]+$)|(^[^\n:]+):[ \t]*([\s\S]*?(?=(?:^[^\n:]*:)|\Z))', flags=re.M)
# patterns for matching concepts
dimension_pat = re.compile(r'^[\d.xX\s]+(cm)?$')
def no_spec_char(input):
    return re.sub(r'[-(),:]', '', input.lower()).strip()

def no_spec_char_space(input):
    return re.sub(r'\s+', ' ', re.sub(r'[-(),:]', ' ', input.lower())).strip()

def no_paren(input):
    return re.sub(r'\([^)]*\)', '', input.lower()).strip()
# end pattern matching stuff

def get_sections(instr):
    return {m.group(1).strip() : m.group(3).strip() for m in get_sections_pat.finditer(instr)}
```

```python slideshow={"slide_type": "subslide"} hide_input=true
Image(filename='./pictures/regex_example.png')
```

```python slideshow={"slide_type": "subslide"}
def find_match(search_term, domain=None, candidate_order=None, previous_concept=None, debug=True):
    """
    Use substring/pattern matching to find a concept that appears to match the search_term
    """
    st_lower = search_term.lower()
    st_no_spec_char = no_spec_char(search_term)
    st_no_spec_char_space = no_spec_char_space(search_term)
    st_no_paren = no_paren(search_term)

    # hierarchy of how to match
    # exact
    if len(concept_df[concept_df.concept == search_term]) == 1:
        df = concept_df[concept_df.concept == search_term].copy()
        if debug: print('Found match based on search term')
    elif ((domain is not None) and (len(concept_df[(concept_df.concept == search_term) & (concept_df.domain_id == domain)]) == 1)):
        df = concept_df[(concept_df.concept == search_term) & (concept_df.domain_id == domain)].copy()
        if debug: print('Found match based on search term and domain')
    # lower case
    elif len(concept_df[concept_df.concept_lower == st_lower]) == 1:
        df = concept_df[concept_df.concept_lower == st_lower].copy()
        if debug: print('Found match based on search term lower cased')
    elif ((domain is not None) and (len(concept_df[(concept_df.concept_lower == st_lower) & (concept_df.domain_id == domain)]) == 1)):
        df = concept_df[(concept_df.concept_lower == st_lower) & (concept_df.domain_id == domain)].copy()
        if debug: print('Found match based on search term lower cased and domain')
    # remove special characters
    elif len(concept_df[concept_df.concept_no_spec_char == st_no_spec_char]) == 1:
        df = concept_df[concept_df.concept_no_spec_char == st_no_spec_char].copy()
        if debug: print('Found match based on search term with removing special characters')
    elif ((domain is not None) and (len(concept_df[(concept_df.concept_no_spec_char == st_no_spec_char) & (concept_df.domain_id == domain)]) == 1)):
        df = concept_df[(concept_df.concept_no_spec_char == st_no_spec_char) & (concept_df.domain_id == domain)].copy()
        if debug: print('Found match based on search term with removing special characters and domain')
```

<!-- #region slideshow={"slide_type": "slide"} -->
## “Data! data! data!” he cried impatiently. “I can’t make bricks without clay.”

The Adventure of the Copper Beeches  
Sir Arthur Conan Doyle
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Sources of text for NLP

* CU Anschutz Health Data Compass - With IRB Approval can access many clinical notes from UC Health and Children's Hospital of Colorado https://www.healthdatacompass.org/
* PhysioNet (MIMIC et al) https://physionet.org/about/database/

## Non-medical related

* Kaggle https://www.kaggle.com/datasets
* Hugging Face https://huggingface.co/datasets
* Amazon product reviews and ratings http://jmcauley.ucsd.edu/data/amazon/
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## It is a capital mistake to theorise before one has data. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.

A Scandal in Bohemia  
Sir Arthur Conan Doyle
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# How to evaluate NLP systems

* Compare against held out training set
* Compare across time
* Compare across sites
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Error Analysis

* What errors matter?
* What concepts are matched wrong?
* What text never is mapped to concepts?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## What really matters for users of this tool?

* Ranked list of features
* Find people who have actually used the human human version of the system - what else did they want to know?
* Precision vs Recall trade off
<!-- #endregion -->

```python slideshow={"slide_type": "subslide"} hide_input=true
Image(filename='./pictures/error_analysis.png')
```

<!-- #region slideshow={"slide_type": "notes"} -->
Precision - Getting items that match class and nothing else.  
Recall - Getting all of the items that match class and some extra too.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
The goal:

Natural-language understanding (NLU) or natural-language interpretation (NLI) is a subtopic of natural-language processing in artificial intelligence that deals with machine reading comprehension. Natural-language understanding is considered an AI-hard problem.

* Linguistics-focused approaches
* Statistics-focused approaches
* The annotation problem

language translation, question answering, text summarization, etc...

Source: [Natural language processing: State of the art and prospects for significant progress, a workshop sponsored by the National Library of Medicine](https://doi.org/10.1016/j.jbi.2013.06.004)
<!-- #endregion -->

Types of NLP

* Word disambiguation:
  * https://www.kaggle.com/xhlulu/medal-emnlp
  * https://zenodo.org/record/4482922
* Note Type: https://www.kaggle.com/tboyle10/medicaltranscriptions
  * Code demonstrating use: https://www.kaggle.com/ritheshsreenivasan/clinical-text-classification
  * Appears to be similar - https://www.kaggle.com/c/medicalnotes-2019/overview
* Mixed bag: https://github.com/socd06/medical-nlp
* Deep learning applied to MIMIC https://github.com/lsy3/clinical-notes-diagnosis-dl-nlp 

```python
#steming/lemmatization is no longer used with deep learning
# labeling problem. See https://arxiv.org/abs/1904.12848 "Unsupervised Data Augmentation for Consistency Training" IMDB with 20 labeled examples
#
# importance of good data:
# "A Chat with Andrew on MLOps: From Model-centric to Data-centric AI" https://youtu.be/06-AZXmwHjo 
```

Data from: https://www.kaggle.com/tboyle10/medicaltranscriptions

Can get from https://github.com/socd06/medical-nlp/raw/master/data/mtsamples.csv as well

<!-- #region slideshow={"slide_type": "slide"} -->
## Resources

### Tutorials/Courses

* "Clinical Natural Language Processing" Laura K. Wiley, PhD Asst Prof @ CU Anschutz https://www.coursera.org/learn/clinical-natural-language-processing
* "Natural Language Processing Specialization" https://www.deeplearning.ai/program/natural-language-processing-specialization/
* "A Code-First Introduction to Natural Language Processing" https://www.fast.ai/2019/07/08/fastai-nlp/
* https://towardsdatascience.com/introduction-to-clinical-natural-language-processing-predicting-hospital-readmission-with-1736d52bc709
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Books

* "Introduction to Information Retrieval" https://nlp.stanford.edu/IR-book/
* "Speech and Language Processing" https://web.stanford.edu/~jurafsky/slp3/
* "Deep Learning for Coders with Fastai and PyTorch" https://book.fast.ai

### Libraries

* https://spacy.io/ - Python
* http://www.nltk.org/ - Python
* https://opennlp.apache.org/ - Java
<!-- #endregion -->

```python

```
