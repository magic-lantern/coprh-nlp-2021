---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
from fastai.text.all import *
```

```python
who
```

```python
Path.cwd()
```

```python
data_path = Path.cwd() / Path('data')
```

```python
mtsamples = pd.read_csv(str(data_path) + '/mtsamples.csv')
mtsamples.head()
```

```python
mtsamples.transcription.str.len()
```

```python
mtsamples.medical_specialty.value_counts()
```

<!-- #region -->
This is one way to load the data for training

```python
TextDataLoaders.from_df(mtsamples,
                        valid_pct=0.2,
                        seed=42,
                        text_col='transcription',
                        label_col='medical_specialty',
                        seq_len=72)
```
<!-- #endregion -->

```python
get_imdb = partial(get_text_files, folders=['train', 'test', 'unsup'])

dls_lm = DataBlock(
    blocks=TextBlock.from_folder(path, is_lm=True),
    get_items=get_imdb, splitter=RandomSplitter(0.1)
).dataloaders(path, path=path, bs=128, seq_len=80)
```

```python
dls_lm = DataBlock(
    blocks=(TextBlock.from_df('transcription', is_lm=True), CategoryBlock),
    get_x=ColReader('transcription'), 
    get_y=ColReader('medical_specialty'),
    splitter=TrainTestSplitter(test_size=0.2,
                               random_state=42,
                               stratify=mtsamples.medical_specialty)
)
```

```python
dls_lm = DataBlock(
    blocks=TextBlock.from_df('transcription', is_lm=True),
    get_x=ColReader('text'),
    #get_y='medical_specialty',
    splitter=TrainTestSplitter(test_size=0.2,
                               random_state=42,
                               stratify=mtsamples.medical_specialty)
)
```

```python
# setting max transcription length to 128 words
dls_lm = dls_lm.dataloaders(mtsamples, bs=64, seq_len=128)
```

```python
dls_lm.show_batch(max_n=2)
```

```python
learn = language_model_learner(
    dls_lm,
    AWD_LSTM,
    drop_mult=0.3, 
    metrics=[accuracy, Perplexity()]).to_fp16()
```

```python
learn.fit_one_cycle(1, 2e-2)
```

```python
learn.save('1epoch')
```

```python

```
