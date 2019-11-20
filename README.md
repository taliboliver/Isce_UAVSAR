# ISCE UAVSAR
This repository contains some basic instructions to process and unwrap UAVSAR images using the InSAR Scientific Computing Environment version 2 [ISCE2](https://github.com/isce-framework/isce2) software. To see the full example step by step please go to the [jypiter notebook example](Isce_UAVSAR/IsceUAVSARprocessing.ipynb). Follow the instructions step by step. 

# Notes about ISCE installation
The full software package as well as installation instructions can be found [here](https://github.com/isce-framework/isce2.
### Some notes
 - If you are installing ISCE2 on OSX I suggest to use **Homebrew installation** that Jose Uribe put together and shared within the [ISCE forum](http://earthdef.caltech.edu/boards/4/topics/2636) as well as on [github](https://github.com/juribeparada/homebrew-isce). To install Homebrew [go here](https://brew.sh/).
 
 - **MacPorts installation** also works well, first [install MacPorts](https://www.macports.org/install.php) and then follow the instructions provided in the [ISCE repository](https://github.com/isce-framework/isce2#with-macports). Also an easier installation can be done using py36-isce2 and py37-isce2 ports. Visit here for more [information](http://earthdef.caltech.edu/boards/4/topics/2906).
 Run the following command
 ```
 sudo port install py37-isce2 +gcc7
 ```
 
 - **Anaconda installation** For linux, its very convenient and allows to have ISCE2 as an [environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
 
 To install conda modified from [yunjunz github](https://github.com/yunjunz): 
 Add to the .bash_profile
 ```
 export PYTHON3DIR=~/python/miniconda3
 export PATH=${PATH}:${PYTHON3DIR}/bin
 ```
 Run the following in your terminal to install miniconda:
 ```
 # download and install miniconda
 # use wget or curl to download in command line or from anaconda's web brower
 # curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o Miniconda3-latest-MacOSX-x86_64.sh
 wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
 chmod +x Miniconda3-latest-MacOSX-x86_64.sh
 ./Miniconda3-latest-MacOSX-x86_64.sh -b -p $PYTHON3DIR
 ``` 
 Run the following in your terminal to install the dependencies to the default environment base:
 ```
 $PYTHON3DIR/bin/conda config --add channels conda-forge
 ```
 To create a conda environment with a specific python version do the following: 
 ```
 # Replace myenv with the desired environment name.
 conda create -n myenv python=3.6  
 
 ```
 Install ISCE2 using conda within a environment (this command will install all ISCE2 dependencies as well). 
 ```
 conda install -n myenv isce2
 ```
 The package automatically setups two environment variables. 
 1. ISCE_HOME : you might want to add ISCE_HOME/bin and ISCE_HOME/applications to your path
 2. ISCE_STACK: this points to the contrib/stack folder
 
 For more information [visit](http://earthdef.caltech.edu/boards/4/topics/2773).
 
 
    
