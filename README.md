Experimental Polylith repo setup

## Environment setup steps

### 1. Install Pyenv

Pyenv is a tool that allows you to install multiple versions of python in your system. This is useful if you want to use different versions of python for different projects.

Follow the instructions below to install pyenv correctly:

#### 1.1. Install python build dependencies:

https://github.com/pyenv/pyenv/wiki#suggested-build-environment

#### 1.2. Install pyenv itself:

https://github.com/pyenv/pyenv?tab=readme-ov-file#installation

#### 1.3. Setup your shell:

https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv

### 2. Clone this repo

```
git clone https://github.com/sykire/sykire.git
```

### 3. Install the python version for this project

First `cd` into the project directory and then run the following command:

```
pyenv install
```

### 4. Install pipx

Pipx is a tool that allow to install applications in isolated environments. This prevents conflicts between the dependencies of different applications.

Follow the instructions below to install pipx correctly:
https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx

### 5. Install Poetry

Poetry is a tool that allow to manage python projects. It is used to manage dependencies, build, and publish python packages.

```
pipx install poetry
```

### 6. Install multi-project and polylith plugins

These plugins are required to use the polylith tool. Polylith is a tool that allow you to manage multiple projects in a single repository.

```
poetry self add poetry-multiproject-plugin
poetry self add poetry-polylith-plugin
```

## Managing the polylith

### Must read

[The official Polylith documentation](https://polylith.gitbook.io/polylith)
[A Python implementation of the Polylith tool](https://github.com/DavidVujic/python-polylith)

### Basic commands

#### Create a new workspace

We won't create a new workspace because we are already in a workspace. But if you want to create a new workspace, you can use the following command:

```
poetry poly create workspace --name=your-root-namespace --theme=loose
```

#### Create a component (brick)

A brick is a component that can be used to build other components, bases, or projects.
These are the compositional elements of the Polylith architecture.

```
poetry poly create component --name=your-component-name
```

### Create a base (application, library, etc.)

Bases are applications that will serve as entry points for our systems. Example: a web application, REST API, library, etc.

```
poetry poly create base --name=your-base-name
```

### Create a project (deploying, publishing, etc.)

Projects connect bases with configurations and provide a way to build, deploy, publish or run our systems. Example: docker, kubernetes, terraform, etc.

```
poetry poly create project --name=your-project-name
```

### Info about the workspace

```
poetry poly info
```

### Diff

```
poetry poly diff --short
```

```
poetry poly diff --bricks
```
