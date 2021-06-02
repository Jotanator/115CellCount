# 115A Cell Count Project

Our code is based on the code from https://github.com/matterport/Mask_RCNN.

## Installation and setup

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
