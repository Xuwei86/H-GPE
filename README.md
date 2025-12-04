H-GPE

A lightweight PyTorch implementation of H-GPE (Hybrid Global-Perception Encoder) for vision tasks — repository contains model code, configs and evaluation/training scripts.

Note: This repository currently has minimal metadata (no DESCRIPTION/website topics) and no explicit LICENSE file visible at the root.
Features (summary)

Python-based implementation of the H-GPE model (single-file model: gpe.py). 
GitHub

Training and evaluation entrypoints provided: main_train.py and main_eval.py (with main_eval_bak.py present as a backup). 
GitHub

Includes configuration file(s): gpe_config.py. 
GitHub



Quick start
1. Clone the repository
git clone https://github.com/Xuwei86/H-GPE.git
cd H-GPE

2. Environment (suggested)

Create a Python virtual environment and install dependencies. The repo does not include an explicit requirements.txt, so the following is a suggested baseline — adapt to the actual requirements in your code:

python -m venv .venv
source .venv/bin/activate   # Git Bash / Linux / macOS
# .venv\Scripts\activate     # Windows PowerShell

If you prefer, add a requirements.txt (or environment.yml) in the repo to pin exact versions.

3. Prepare data

The repository does not include dataset downloads. Modify the config in gpe_config.py (or follow the code in main_train.py) to point to your dataset paths (ImageNet / MS COCO / ADE20K.). Check gpe_config.py for default dataset/settings. 
GitHub

4. Train

Example (typical):

# basic example — modify flags / config as required by main_train.py
python main_train.py --config gpe_config.py --work-dir ./workdir/exp1


Or if the script expects a different argument style:

python main_train.py

(Inspect main_train.py for the exact CLI arguments and configuration flow.) 
GitHub

5. Evaluate

Example:

python main_eval.py --checkpoint path/to/checkpoint.pth --config gpe_config.py


Or:

python main_eval_bak.py --checkpoint path/to/checkpoint.pth


(查看 main_eval.py 以获取完整参数说明。) 
GitHub

File / Folder Overview (root)

gpe.py — model implementation (core H-GPE code). 
GitHub

gpe_config.py — configuration file(s) for training / model hyperparameters. 
GitHub

main_train.py — training entrypoint script. 
GitHub

main_eval.py, main_eval_bak.py — evaluation / inference scripts. 
GitHub

model and modules.txt — (text file) likely documents module architecture / layer list — useful as a quick reference. 
GitHub

H-ViP.pdf — paper / design doc (visual / algorithmic details). 
GitHub

visual-compare.pdf — visual comparison figures. 
GitHub

H-GPE_orig.png — original architecture / illustration. 
GitHub

How to contribute

Fork the repo and create a topic branch.

Add features, tests, or documentation.

Submit a PR with a clear description of changes.

Some suggestions to improve the repository for contributors/users:

Add README.md (this file) and a short project description in repo settings. 
GitHub

Add requirements.txt or environment.yml to pin dependency versions.

Add example commands (with exact CLI flags) or a scripts/ folder with reproducible training/eval commands.

Add a LICENSE file to clarify reuse terms. The repo currently shows no license in the root. 
GitHub

Citation

If this repo corresponds to a paper or preprint (e.g., H-ViP.pdf in this repo), please include a recommended citation block (BibTeX) in CITATION.bib or in the README itself. The repo includes H-ViP.pdf — check the PDF for official citation info. 
GitHub

Troubleshooting & tips

If main_train.py fails due to missing arguments, run:

python main_train.py --help


or open the script to see expected flags. 
GitHub

If you want to push this repo to GitHub for the first time from local and you had problems earlier (src refspec main does not match any), make sure you have at least one commit locally and that your branch name matches (e.g., main) before git push -u origin main. (This is not specific to this repo file contents but general Git usage.)

Add a LICENSE and a short CONTRIBUTING.md to make collaboration easier.

Contact / Author

Repository owner: Xuwei86 (GitHub account). For questions about code and usage, opening an issue in the repository is recommended. 
GitHub
