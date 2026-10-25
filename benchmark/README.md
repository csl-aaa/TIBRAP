# TIBRAP-Bench

1,000 Tibetan image–question pairs. Four capabilities contain 250 records each; answer formats comprise 200 binary, 250 numeric, 150 multiple-choice and 400 short-text records.

## Data

| File | Contents |
|---|---|
| `data/test.jsonl` | All 1,000 records |
| `data/primary900.jsonl` | 900 evaluation records |
| `data/development100.jsonl` | 100 development-visible records |
| `data/provenance.jsonl` | Source records and evidence categories |
| `image_sources.csv` | Source datasets, image filenames, paths and IDs |

Each record contains `id`, `conversations`, `image`, `split`, `capability`, `answer_format`, `canonical_target` and `acceptable_targets`. Image paths are relative to `benchmark/`.

## Images

The GitHub version contains no images. Copy `benchmark/` from the with-images version into this project, or extract [FTib-data](https://huggingface.co/datasets/onedday/FTib-data/tree/main) and run:

```bash
python benchmark/scripts/restore_images.py --source /path/to/FTib-data
```

`image_sources.csv` maps every image to its source filename and record ID. Stored row indices follow their source loader's indexing convention.

## Evaluation

The evaluation split is `primary900`. Metrics are normalized reference matching, Token F1, ANLS and short-text chrF++.

Evaluation code: coming soon.

## Sources

Tibetan questions and answers come from [FTib-data](https://huggingface.co/datasets/onedday/FTib-data).

| Source | Records |
|---|---:|
| Vision-Flan | 466 |
| MultiInstruct | 283 |
| BinaryVQA2 | 150 |
| MMBench | 58 |
| COREVQA | 43 |

Images and component datasets retain their original licenses.
