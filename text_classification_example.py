# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from fastai.text.all import *

# %%
who

# %%
Path.cwd()

# %%
data_path = Path.cwd() / Path('data')

# %%
mtsamples = pd.read_csv(str(data_path) + '/mtsamples.csv')
mtsamples.head()

# %%
mtsamples.transcription.str.len()

# %%
mtsamples.medical_specialty.value_counts()

# %% [markdown]
# This is one way to load the data for training
#
# ```python
# TextDataLoaders.from_df(mtsamples,
#                         valid_pct=0.2,
#                         seed=42,
#                         text_col='transcription',
#                         label_col='medical_specialty',
#                         seq_len=72)
# ```

# %%
get_imdb = partial(get_text_files, folders=['train', 'test', 'unsup'])

dls_lm = DataBlock(
    blocks=TextBlock.from_folder(path, is_lm=True),
    get_items=get_imdb, splitter=RandomSplitter(0.1)
).dataloaders(path, path=path, bs=128, seq_len=80)

# %%
dls_lm = DataBlock(
    blocks=(TextBlock.from_df('transcription', is_lm=True), CategoryBlock),
    get_x=ColReader('transcription'), 
    get_y=ColReader('medical_specialty'),
    splitter=TrainTestSplitter(test_size=0.2,
                               random_state=42,
                               stratify=mtsamples.medical_specialty)
)

# %%
dls_lm = DataBlock(
    blocks=TextBlock.from_df('transcription', is_lm=True),
    get_x=ColReader('text'),
    #get_y='medical_specialty',
    splitter=TrainTestSplitter(test_size=0.2,
                               random_state=42,
                               stratify=mtsamples.medical_specialty)
)

# %%
# setting max transcription length to 128 words
dls_lm = dls_lm.dataloaders(mtsamples, bs=64, seq_len=128)

# %%
dls_lm.show_batch(max_n=2)

# %%
learn = language_model_learner(
    dls_lm,
    AWD_LSTM,
    drop_mult=0.3, 
    metrics=[accuracy, Perplexity()]).to_fp16()

# %%
learn.fit_one_cycle(1, 2e-2)

# %%
learn.save('1epoch')

# %%
