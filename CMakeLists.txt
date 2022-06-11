cmake_minimum_required(VERSION 3.12.0)

cmake_policy(SET CMP0054 NEW)
set(SKBUILD_LINK_LIBRARIES_KEYWORD PRIVATE)

set(THREADS_PREFER_PTHREAD_FLAG ON)
if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(CMAKE_OSX_DEPLOYMENT_TARGET "10.9" CACHE STRING "Minimum OS X deployment version")
endif()

project(jarowinkler LANGUAGES C CXX)

find_package(PythonExtensions REQUIRED)
find_package(Python COMPONENTS Interpreter Development)
include(FetchContent)

set(JW_BASE_DIR ${CMAKE_CURRENT_SOURCE_DIR})

find_package(jaro_winkler 1.0.0 EXACT QUIET)
if (jaro_winkler_FOUND)
    message("Using system supplied version of jaro_winkler")
else()
    message("Using FetchContent to load jaro_winkler")
    FetchContent_Declare(
        jaro_winkler
        GIT_REPOSITORY https://github.com/maxbachmann/jarowinkler-cpp.git
        GIT_TAG 09f221c6b21d266823d5d9ea73b4673b6de2e80f # v1.0.0
        GIT_SHALLOW TRUE
    )
    FetchContent_MakeAvailable(jaro_winkler)
endif()

add_subdirectory(jarowinkler)
