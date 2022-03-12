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

set(JAROWINKLER_BASE_DIR ${CMAKE_CURRENT_SOURCE_DIR})

add_subdirectory(jarowinkler)
