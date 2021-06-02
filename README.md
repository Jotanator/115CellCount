# 115A Cell Count Project

Our code is based on the code from https://github.com/matterport/Mask_RCNN.

It is recommended to use windows to run this app, it works on mac but the UI does not look like as it should.

Any other operating system we are not aware whether it will work or not so run at your at own risk.

## Installation and setup
Before cloning this repository, be sure to install git LFS (Large File System).
If on windows or Mac, download LFS from the git lfs website. If on Linux, download it using your package manager
Then, open your terminal (or git bash if you are using windows) and run the command:
```
git lfs install
```

Afterwards, clone the repository as usual. 

To install the code, you need to install anaconda.
After installing, you should be able to create a new anaconda environment.
To do this, run:

```
conda create --name NameOfEnv python=3.7
```

where "NameOfEnv" is replaced by whatever you want to name the environment.
To activate the environment, run:

```
conda activate NameOfEnv
```

where "NameOfEnv" is replaced by whatever you named the environment.
Next, cd to the 115CellCount directory and run:


```
pip install -r requirements.txt
```

## Running
First, make sure that the environment is activated.
If it is not, run:

```
conda activate NameOfEnv
```

where "NameOfEnv" is replaced by whatever you named the environment.
Next, cd to the 115CellCount directory and run:

```
python runner.py
```

The first run will take a while.

When done with the program, you may need to ctrl+c or close terminal.

## Exiting the environment
To exit a conda environment, run:

```
conda deactivate
```

## Removal
You may delete the entire 115 directory to remove the files. Removing a conda environment will require additional steps.

First, check that the conda environment is not running. If the conda environment is running, run:
```
conda deactivate
```

To get remove the conda environment, run:
```
conda env remove --name NameOfEnv
```

where "NameOfEnv" is replaced by whatever you named the environment.
