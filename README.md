## JaroWinkler


## Description

## Requirements

- Python 3.6 or later
- On Windows the [Visual C++ 2019 redistributable](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) is required

## Installation

There are several ways to install JaroWinkler, the recommended methods
are to either use `pip`(the Python package manager) or
`conda` (an open-source, cross-platform, package manager)

### with pip

JaroWinkler can be installed with `pip` the following way:

```bash
pip install jarowinkler
```

There are pre-built binaries (wheels) of JaroWinkler for MacOS (10.9 and later), Linux x86_64 and Windows.

> :heavy_multiplication_x: &nbsp;&nbsp;**failure "ImportError: DLL load failed"**
>
> If you run into this error on Windows the reason is most likely, that the [Visual C++ 2019 redistributable](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) is not installed, which is required to find C++ Libraries (The C++ 2019 version includes the 2015, 2017 and 2019 version).

### with conda

RapidFuzz can be installed with `conda`:

```bash
conda install -c conda-forge jarowinkler
```

### from git
JaroWInkler can be installed directly from the source distribution by cloning the repository. This requires a C++14 capable compiler.

```bash
git clone --recursive https://github.com/maxbachmann/JaroWinkler.git
cd JaroWinkler
pip install .
```

## Usage

## Benchmark
