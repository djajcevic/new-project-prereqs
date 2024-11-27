# Welcome to Docs Base



For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Prerequisites

### Cookiecutter

- installed Python 3
- installed `pip`
- installed latest Cookiecutter:
  
    For Cookiecutter installations instructions visit [installation](https://cookiecutter.readthedocs.io/en/stable/installation.html) page.

#### Generating project

Run following command to generate project and provide input:

**Windows**
```shell
cookiecutter.exe https://github.com/djajcevic/new-project-prereqs.git
```
**Linux**
```shell
cookiecutter https://github.com/djajcevic/new-project-prereqs.git
```

### Mkdocs

- installed Python 3
- installed `pip`
- installed `mkdocs`

#### Installation instructions

Using `pip` install required packages

```
pip install mkdocs "mkdocs-techdocs-core==1.*"
```

#### Commands

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

#### Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
