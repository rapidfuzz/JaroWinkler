## Changelog

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
