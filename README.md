# Python

## Setup

1. Install Python 3
    * On a Unix-based OS, the system's default Python installation is normally Python 2. Check this by running `python --version` on a terminal. If this is so, install Python 3 but **DO NOT REMOVE / OVERWRITE / UNINSTALL** the old Python 2. The system uses Python 2 for its internal scripts and removing it may break the OS installation.
    * For Linux, either install it from `apt` or from source
        * [How to install Python3.7 on Ubuntu18.04?](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
    * For Mac, use Homebrew
        * [Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)
        * [How is Python handled by Homebrew](https://docs.brew.sh/Homebrew-and-Python)
    * Verify the Python installation by running
        ```shell
        $ which python3
        $ python3 --version

        ```
1. Setup and use a [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
    * There are [many different modules](https://stackoverflow.com/q/41573587/2745495) for creating a virtual environment
    * If Python 2 support is needed, use the [virtualenv](https://virtualenv.pypa.io/en/stable/) module
    * If Python 3 only, use the built-in [venv](https://docs.python.org/3/library/venv.html) or [poetry](https://python-poetry.org/)
        * For `venv`
            * Set `VENV_DIR` to directory for virtual environments (ex. `$HOME/.venvs`)
            * Copy the [bash aliases for using venv](../bash/bash_aliases)
                * `mkvenv PROJECT_NAME`
                * `upvenv PROJECT_NAME`
                * `dnvenv`
                * `rmvenv PROJECT_NAME`
                * `lsvenv`
        * For `poetry`
            * Set [`poetry config cache-dir`](https://python-poetry.org/docs/configuration/#cache-dir)

1. For each Python project
    * For `virtualenv` and `venv`
        * Create/Activate a virtual environment
            ```shell
            $ mkvenv NAME /path/to/python

        * When switching environments:
            ```shell
            $ pip install -r requirements.txt
            ```
1. execute the script
   * When switching environments:
     ```shell
       $ python recognition.py
     ```
