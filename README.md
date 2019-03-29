# Starting the Jupyter Notebook

## Start Steps

1. Install Python3.6 however suits you
    ```
    sudo dnf install python36
    ```

1. Clone this project
    ```
    git clone git@git.sp.darkwolf.io:will/brewwolf-python.git
    ```

1. Go into the project and create the virtual-environment
    ```
    cd brewwolf-python
    python3 -m venv venv
    source venv/bin/activate
    ```

1. Update pip and install requirements
    ```
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

1. Start the notebook
    ```
    jupyter notebook
    ```