cmake_minimum_required(VERSION 3.15...3.24)

set(Python_FIND_IMPLEMENTATIONS CPython PyPy)
if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(CMAKE_OSX_DEPLOYMENT_TARGET "10.9" CACHE STRING "Minimum OS X deployment version")
endif()

project(jarowinkler LANGUAGES C CXX)

find_package(Python COMPONENTS Interpreter Development.Module)
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
