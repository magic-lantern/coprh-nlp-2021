# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python [conda env:py37] *
#     language: python
#     name: conda-env-py37-py
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# # Attics, guesswork and clay. Sleuthing your way into Biomedical Natural Language Processing
#
# ## Colorado Pragmatic Research in Health 2021 Conference<br/>May 24 - 26, 2021
#
# <pre>
# Seth Russell, MS
# University of Colorado Anschutz Medical Campus
# ACCORDS Data Science Program, D2V Data Science Core
# </pre>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Learning Objectives
#
# Learners should have:
#
# 1. A general idea of what Natural Language Processing (NLP) is.
# 1. A knowledge of the ethical implications of data reuse in NLP.
# 1. Knowledge of where to get text for NLP.
# 1. How to use and learn more about some basic NLP techniques.

# %% [markdown]
# ##  “We are coming now rather into the region of guesswork,” said Dr. Mortimer.
#
# ## “Say, rather, into the region where we balance probabilities and choose the most likely. It is the scientific use of the imagination, but we have always some material basis on which to start our speculation.” 
#
# The Hound of the Baskervilles
#
# ## It is a capital mistake to theorise before one has data. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.
#
# A Scandal in Bohemia
#
# ## “Come, Watson, come!” he cried. “The game is afoot. Not a word! Into your clothes and come!”
#
# The Adventure of the Abbey Grange
#
# ## “Data! data! data!” he cried impatiently. “I can’t make bricks without clay.”
#
# The Adventure of the Copper Beeches
#
# ## I consider that a man’s brain originally is like a little empty attic, and you have to stock it with such furniture as you choose. 
#
# A fool takes in all the lumber of every sort that he comes across, so that the knowledge which might be useful to him gets crowded out, or at best is jumbled up with a lot of other things so that he has a difficulty in laying his hands upon it. Now the skilful workman is very careful indeed as to what he takes into his brain-attic. He will have nothing but the tools which may help him in doing his work, but of these he has a large assortment, and all in the most perfect order. It is a mistake to think that that little room has elastic walls and can distend to any extent. Depend upon it there comes a time when for every addition of knowledge you forget something that you knew before. It is of the highest importance, therefore, not to have useless facts elbowing out the useful ones.
#
# A Study In Scarlet
#
# Sir Arthur Conan Doyle
#

# %% [markdown]
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # ACM Code of Ethics and Professional Conduct
#
# #### Association for Computing Machinery, 2018
#
# Computing professionals' actions change the world. To act responsibly, they should reflect upon the wider impacts of their work, consistently supporting the public good. The ACM Code of Ethics and Professional Conduct ("the Code") expresses the conscience of the profession...

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# ## 1. GENERAL ETHICAL PRINCIPLES.
#
# A computing professional should...
#
# 1. Contribute to society and to human well-being, acknowledging that all people are stakeholders in computing
# 1. Avoid harm.
# 1. Be honest and trustworthy.
# 1. Be fair and take action not to discriminate.
# 1. Respect the work required to produce new ideas, inventions, creative works, and computing artifacts.
# 1. Respect privacy.
# 1. Honor confidentiality.

# %% [markdown] slideshow={"slide_type": "fragment"}
# ## 2. PROFESSIONAL RESPONSIBILITIES.
# ...
#
# Continued at https://www.acm.org/code-of-ethics

# %% [markdown] slideshow={"slide_type": "slide"}
# # Overview
#
# 1. What is Natural Language Processing?
# 1. Document Retrieval?
# 1. Information Extraction
# 1. Information Retrieval
# 1. Word/Concept/Abbreviation disambiguation
#

# %% [markdown] slideshow={"slide_type": "slide"}
# The goal:
#
# Natural-language understanding (NLU) or natural-language interpretation (NLI) is a subtopic of natural-language processing in artificial intelligence that deals with machine reading comprehension. Natural-language understanding is considered an AI-hard problem.
#
# * Linguistics-focused approaches
# * Statistics-focused approaches
# * The annotation problem
#
# language translation, question answering, text summarization, etc...
#
# Source: [Natural language processing: State of the art and prospects for significant progress, a workshop sponsored by the National Library of Medicine](https://doi.org/10.1016/j.jbi.2013.06.004)

# %% [markdown]
# openai gpt-3 training at least 4.6 million in hardware costs + many people
#
# https://bdtechtalks.com/2020/09/21/gpt-3-economy-business-model/

# %% [markdown]
# Examples of items to present:
#
# * https://www.fast.ai/2019/07/08/fastai-nlp/
# * https://towardsdatascience.com/introduction-to-clinical-natural-language-processing-predicting-hospital-readmission-with-1736d52bc709
#
# Types of NLP
#
# * Word disambiguation:
#   * https://www.kaggle.com/xhlulu/medal-emnlp
#   * https://zenodo.org/record/4482922
# * Note Type: https://www.kaggle.com/tboyle10/medicaltranscriptions
#   * Code demonstrating use: https://www.kaggle.com/ritheshsreenivasan/clinical-text-classification
#   * Appears to be similar - https://www.kaggle.com/c/medicalnotes-2019/overview
# * Mixed bag: https://github.com/socd06/medical-nlp
# * Deep learning applied to MIMIC https://github.com/lsy3/clinical-notes-diagnosis-dl-nlp 

# %%
#steming/lemmatization is no longer used with deep learning
# labeling problem. See https://arxiv.org/abs/1904.12848 "Unsupervised Data Augmentation for Consistency Training" IMDB with 20 labeled examples
#
# importance of good data:
# "A Chat with Andrew on MLOps: From Model-centric to Data-centric AI" https://youtu.be/06-AZXmwHjo 

# %% [markdown]
# Data from: https://www.kaggle.com/tboyle10/medicaltranscriptions
# Can get from https://github.com/socd06/medical-nlp/raw/master/data/mtsamples.csv as well

# %%
import fastai

# %%
untar_data(url, fname=None, dest=None, c_key='data', force_download=False, extract_func=file_extract, timeout=4)

# %%
