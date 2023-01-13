# Create and set up project
mkdir $1
cd $1
mkdir external src doc
touch CMakeLists.txt readme.md version.md src/$1.cpp src/$1.h

# Set up cmake
echo "cmake_minimum_required(VERSION 3.22)\n" >> CMakeLists.txt
echo "project($1)\n" >> CMakeLists.txt
echo "add_library($1 src/$1.cpp src/$1.h)" >> CMakeLists.txt

# Set up readme
echo "# $1" >> readme.md

# Set up documentation
touch doc/requirements.md doc/design.md
echo "# $1 Requirement Specification" >> doc/requirements.md
echo "# $1 Design Document" >> doc/design.md

# Set up version
echo "# Version\n" >> version.md
echo "0\n" >> version.md
echo "0\n" >> version.md
echo "0\n" >> version.md 
