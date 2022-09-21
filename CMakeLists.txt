cmake_minimum_required(VERSION 3.12...3.24)

set(SKBUILD_LINK_LIBRARIES_KEYWORD PRIVATE)

set(THREADS_PREFER_PTHREAD_FLAG ON)

project(jarowinkler LANGUAGES C CXX)

find_package(PythonExtensions REQUIRED)
if(CMAKE_VERSION VERSION_LESS 3.18)
    find_package(Python COMPONENTS Interpreter Development REQUIRED)
else()
    find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
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
