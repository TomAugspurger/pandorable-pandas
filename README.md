# Pandorable Pandas

Materials for my Anaconda tutorial on clean and efficient data analysis.

## Setup

0. Make sure you have [Anaconda Individual Edition](https://www.anaconda.com/products/individual) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.
1. Clone or download the contents of this repository and navigate to it

```
# using git
git clone https://github.com/TomAugspurger/pandorable-pandas.git
```

Or click the green "Code" button and "Download Zip". Extract the repository from the zip archive.

2. Navigate to the repository (`cd pandorable-pandas`) in a terminal with `conda` on your `PATH`.
3. Create the environment

```console
$ conda env create -f binder/environment.yml
```

4. Activate the environment

```console
$ conda activate pandorable-pandas
```

5. Start the notebook server

```console
$ jupyter notebook
```

And open "Introduction.ipynb".

## Alternative Setup

I recommend following the setup above to get a local environment running.
As a backup, you can visit this Binder link to get an interactive session graciously hosted by [mybinder.org](http://mybinder.org).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TomAugspurger/pandorable-pandas/HEAD)
