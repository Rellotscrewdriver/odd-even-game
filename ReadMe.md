# Project Template
this repo contains the boilerplate for my future projects so I don't have to create a project from scratch

## Project Structure
- `include` is for containing header files
- `docs` is to contains doxyfile for documentation generator
- `libs` is for containing external libraries' source code which builds with the main project
- `src` is containing the main program's source code
- `tests` is for containing unit tests to test various parts of the software

## Toolset
- CMake for build system generator
- Doxygen for generating documentation
- Make / Ninja are used for build system
- Googletest for testing and mocking
- Github Actons for CI/CD

## Setting up the project

### Dependencies
- CMake
- GNU make / Ninja
- GCC / Clang / MSVC
- AStyle
- Doxygen

### Setup
clone the repo with submodules
```
git clone --recurse-submodules https://github.com/Rellotscrewdriver/my-project-template.git
```

goto the cloned repo and configure the project
```
cd my-project-template
cmake -S . -B build
```

build the project
```
cmake --build build
```
then run the 'template' or 'utest' program

##  Contributions

We explicitly welcome outside contributors.
you can read our <a href="https://github.com/Rellotscrewdriver/my-project-template/blob/master/CODE_OF_CONDUCT.md">CODE_OF_CONDUCT</a> for rules</br>
and <a href="https://github.com/Rellotscrewdriver/my-project-template/blob/master/CONTRIBUTING.md">CONTRIBUTING</a> for contribution guidelines and coding style

## Screenshots
People usually like to see how it looks before downloading the product.
<img src="">

## COPYRIGHT

this project is free to use and distribute as long as you don't claim that you wrote the original software.
crediting of this project is required when it is modified and/or distributed. goto <a href="https://github.com/Rellotscrewdriver/my-project-template/blob/master/LICENSE">LICENSE</a> for more details 