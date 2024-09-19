# CLEF dataloader

This is a modified repository from [clef-dataloaders](https://github.com/rlitschk/clef-dataloaders), with extended language coverage.
We support the following languages: English, Spanish, German, French, Italian.


## Setup
- Download and unzip [The CLEF Test Suite for the CLEF 2000-2003 Campaigns – Evaluation Package](https://catalogue.elra.info/en-us/repository/browse/ELRA-E0008/).
- Set `CLEF_BASE_DIR` in `clef_paths.py` to point to the location of the unzipped dataset. (Make sure to change the path in clef_paths.py accordingly!)
- *(Optional)* Download and unzip Swahili (SW) and Somali (SO) CLEF queries [here](https://ciir.cs.umass.edu/ictir19_simulate_low_resource).
- *(Optional)* Set `CLEF_LOWRES_DIR` in `clef_paths.py` to where you unzipped the dataset.

Dataloaders expect the following structure after downloading and unzipping CLEF:
```bash
clef/
├── clef-low-resource
│         └── long_paper
├── DocumentData
│         ├── dutch
│         ├── english
│         ├── finnish
│         ├── french
│         ├── german
│         ├── italian
│         └── russian
├── RelAssess
│         ├── 2001
│         ├── 2002
│         └── 2003
└── Topics
    ├── 2001
    ├── 2002
    └── 2003
```
## Acknowledgements
We thank the authors of the original [repository](https://github.com/rlitschk/clef-dataloaders) for their work. This repository is a fork of the original repository with extended language support.

## References

```bibtex
@inproceedings{Bonab2019swahiliclef,
    author = {Bonab, Hamed and Allan, James and Sitaraman, Ramesh},
    title = {Simulating CLIR Translation Resource Scarcity Using High-Resource Languages},
    year = {2019},
    url = {https://doi.org/10.1145/3341981.3344236},
    booktitle = {Proceedings of ICTIR},
    pages = {129–136},
}
```
```bibtex
@inproceedings{braschler2003clef,
    title={{CLEF 2003--Overview of results},
    author={Braschler, Martin},
    booktitle={Workshop of the Cross-Language Evaluation Forum for European Languages},
    pages={44--63},
    year={2003},
    organization={Springer}
}
```
