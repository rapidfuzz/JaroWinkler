# should use target_include_directories once this is supported by scikit-build
include_directories(${JAROWINKLER_BASE_DIR}/src/cython)

add_cython_target(Jaro CXX)
add_library(Jaro MODULE
    ${Jaro})
target_compile_features(Jaro PUBLIC cxx_std_14)
target_include_directories(Jaro PRIVATE
    ${JAROWINKLER_BASE_DIR}/extern/jarowinkler-cpp/
    ${RAPIDFUZZ_CAPI_PATH}
    ${JAROWINKLER_BASE_DIR}/src/cython)
python_extension_module(Jaro)
install(TARGETS Jaro LIBRARY DESTINATION src/jarowinkler)

add_cython_target(JaroWinkler CXX)
add_library(JaroWinkler MODULE
    ${JaroWinkler})
target_compile_features(JaroWinkler PUBLIC cxx_std_14)
target_include_directories(JaroWinkler PRIVATE
    ${JAROWINKLER_BASE_DIR}/extern/jarowinkler-cpp/
    ${RAPIDFUZZ_CAPI_PATH}
    ${JAROWINKLER_BASE_DIR}/src/cython)
python_extension_module(JaroWinkler)
install(TARGETS JaroWinkler LIBRARY DESTINATION src/jarowinkler)
