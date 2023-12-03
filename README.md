# ai|coustics - Case Study

**Crawler**

Crawler, fetches zip files containing A noisy speech corpus (NOIZEUS) from https://ecs.utdallas.edu/loizou/speech/noizeus/ and extracts audio files.

**NISQA**

NISQA is a deep learning model/framework for speech quality prediction.

**Sorter**

Sorter is used to sort CSV file contains NISQA prediction results by descending speech quality. 

## Installation
To install requirements install [Anaconda](https://www.anaconda.com/products/individual) and then use:

```setup
conda env create -f env.yml
```

This will create a new environment with the name "nisqa". Activate this environment to go on:

```setup2
conda activate nisqa
```
## Usage

```
python .\Toolkit\Crawler.py
```
```
python .\NISQA\run_predict.py --mode predict_dir --pretrained_model NISQA\weights\nisqa.tar --data_dir .\audio-files --num_workers 0 --bs 10 --output_dir .\results
```

```
python .\Toolkit\Sorter.py
```


## NISQA
https://github.com/gabrielmittag/NISQA
## NISQA Corpus
https://github.com/gabrielmittag/NISQA/wiki/NISQA-Corpus
## NOIZEUS Corpus
https://ecs.utdallas.edu/loizou/speech/noizeus/


## References

-   [G. Mittag, B. Naderi, A. Chehadi, and S. Möller “NISQA: A Deep CNN-Self-Attention Model for Multidimensional Speech Quality Prediction with Crowdsourced Datasets,” in Proc. Interspeech 2021, 2021.](https://www.isca-speech.org/archive/pdfs/interspeech_2021/mittag21_interspeech.pdf)
-   [G. Mittag and S. Moller, “Deep Learning Based Assessment of Synthetic Speech Naturalness,” in Proc. Interspeech 2020, 2020.](https://www.isca-speech.org/archive/Interspeech_2020/abstracts/2382.html)
-   [G. Mittag and S. Möller. Full-reference speech quality estimation with attentional Siamese neural networks. In Proc. ICASSP 2020, 2020.](https://ieeexplore.ieee.org/document/9053951)
-   [G.  Mittag  and  S.  Möller,  “Non-intrusive  speech  quality  assessment  for  super-wideband  speech  communication  networks,”  in Proc. ICASSP 2019, 2019](https://ieeexplore.ieee.org/document/8683770)
-   [Hu, Y. and Loizou, P. (2007). “Subjective evaluation and comparison of speech enhancement algorithms,” Speech Communication, 49, 588-601.](https://personal.utdallas.edu/~loizou/cimplants/quality_spcom07.pdf)


The NISQA code is licensed under [MIT License](LICENSE).

The model weights are provided under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](weights/LICENSE_model_weights)

