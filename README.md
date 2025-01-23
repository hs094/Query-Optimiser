# <div align="center">Query Optimiser</div>

<br />
<div align="center">
    <i>Compiling queries</i>
    <br />
    <br />
    <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=C%2B%2B&logoColor=white" />
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white">
    <br />
    <br />
    <a href="https://github.com/outer-rim/Query-Optimiser/issues">Report Bug</a>
    ·
    <a href="https://github.com/outer-rim/Query-Optimiser/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#directory-structure">Directory structure</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

Query Optimiser is a compiler project designed to optimize and execute queries efficiently. The project leverages C++ for core compilation tasks, Python for scripting, and Streamlit for a user-friendly web interface. The goal is to provide a robust solution for compiling and optimizing queries, making it easier for users to handle complex query operations.

### Features
- **Compilation**: Efficiently compiles queries using C++.
- **Optimization**: Implements various optimization techniques to enhance query performance.
- **User Interface**: Provides a web-based interface using Streamlit for easy interaction.
- **Extensibility**: Designed to be easily extendable with additional features and optimizations.

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

A quick introduction of the minimal setup you need to get the application up and running.

### Prerequisites
Install the gcc package along with flex and bison (following commands are applicable for Ubuntu-based systems):

A quick introduction of the minimal setup you need to get the application up

Install the gcc package along with flex and bison (following commands are applicable for Ubuntu based systems)

```shell
sudo apt install build-essentials
sudo apt install flex bison
make run
pip install -r requirements.txt
streamlit run deploy.py
```

## Installation
1. Clone the repository:
```
git clone https://github.com/outer-rim/Query-Optimiser.git
cd Query-Optimiser/translator
```
2. Build and run the project:
```
make run
```
3. Install Python dependencies:
```
pip install -r requirements.txt
```
4. Run the Streamlit application:
```
streamlit run deploy.py
```

### Directory Structure

```shell
.
├── call.py
├── deploy.py
├── inp.txt
├── Makefile
├── README.md
├── requirements.txt
├── test.l
├── test_target_translator.cxx
├── test_translator.cxx
├── test_translator.h
├── test.y
└── tmp
    ├── in.txt
    └── out.txt

```
