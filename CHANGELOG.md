## Changelog

### [2.0.1] - 2023-11-02
#### Fixed
- fix version requirement for rapidfuzz

### [2.0.0] - 2023-11-01
#### Changed
- use rapidfuzz to deduplicate the implementations
- add support for Python 3.11 and Python 3.12
- remove support for Python 3.6 and 3.7

### [1.2.3] - 2022-08-27
#### Fixed
- fix support for cmake versions below 3.17

### [1.2.2] - 2022-08-25
#### Changed
- modernize cmake build to fix most conda-forge builds

### [1.2.1] - 2022-08-12
#### Changed
- Added support for Python3.11

### [1.2.0] - 2022-07-19
#### Changed
- added in-tree build backend to install cmake and ninja only when it is not installed yet
  and only when wheels are available

### [1.1.2] - 2022-07-11
#### Fixed
- remove incorrect module import

### [1.1.1] - 2022-07-09
#### Fixed
- fix missing type stubs

### [1.1.0] - 2022-07-04
#### Changed
- change src layout to make package import from root directory possible
- added pure python fallback for all implementations with the following exceptions:
  - no support for sequences of hashables. Only strings supported so far

#### Fixed
- fixed type hints of jarowinkler_similarity

### [1.0.5] - 2022-06-29
#### Fixed
- treat hash for -1 and -2 as different

### [1.0.4] - 2022-06-23
#### Changed
- add fallback implementations of `jarowinkler-cpp` back to wheel,
  since some package building systems like piwheels can't clone sources

## [1.0.3] - 2022-06-11
#### Added
- add wheels for PyPy3.9
- added tests to sdist

#### Changed
- Allow installation from system installed version of jarowinkler-cpp
- use system version of cmake on arm platforms, since the cmake package fails to compile

## [1.0.2] - 2022-03-13
#### Fixed
- only depend on cython when it is actually required

## [1.0.1] - 2022-03-06
#### Fixed
- type hints are now correctly packaged in the wheels
