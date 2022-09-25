cmake_minimum_required(VERSION 3.12...3.24)

set(SKBUILD_LINK_LIBRARIES_KEYWORD PRIVATE)
set(Python_FIND_IMPLEMENTATIONS CPython PyPy)
set(THREADS_PREFER_PTHREAD_FLAG ON)

project(jarowinkler LANGUAGES C CXX)

if(CMAKE_VERSION VERSION_LESS 3.18)
    find_package(Python COMPONENTS Interpreter Development REQUIRED)
else()
    set(Python_ARTIFACTS_INTERACTIVE TRUE)
    find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
endif()

if("${Python_INTERPRETER_ID}" STREQUAL "PyPy")
    message(STATUS "PyPy SOABI: ${Python_SOABI}")
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -c
                "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX').split('.')[1])"
        OUTPUT_VARIABLE Python_SOABI
        OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
    message(STATUS "Corrected SOABI: ${Python_SOABI}")
endif()

include(FetchContent)

set(JW_BASE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)

find_package(jaro_winkler 1.0.2 QUIET)
if (jaro_winkler_FOUND)
    message(STATUS "Using system supplied version of jaro_winkler")
else()
    message(STATUS "Using packaged version of jaro_winkler")
    add_subdirectory(extern/jarowinkler-cpp)
endif()

add_subdirectory(src/jarowinkler)
