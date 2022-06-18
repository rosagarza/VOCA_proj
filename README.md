# VOCA_proj

## Environment setup/Installation Packages
In order to run the project, we found it best to create a conda environment which can be created from the `packagelist.txt` file. 

You must also get VOCA running by referring to https://github.com/TimoBolkart/voca which you will also need to refer to https://github.com/MPI-IS/mesh in order to install a necessary package known as psbody mesh. For psbody mesh, it was difficult, but be sure to download the latest release for your OS and if it's MAC, be sure to have your Python version correspond to what's provided wihin the name of the release (ex: psbody_mesh-0.4-cp37-cp37m-macosx_10_9_x86_64.whl will need python version 3.7 which is seen with cp37).

We also found that for VOCA, you will need Python version 3.6 in order for Tensorflow 1.15 to be installed. You will also need to download the neccessary data and pretrained models for VOCA (FLAME, DeepSpeech) which can be found at https://voca.is.tue.mpg.de/download.php . Mind you, you will also need to create an account to Accept Terms & Conditions for using their models.

Follow VOCA to train the model in order to run the model with our code.

## Running our project

Run the .sh file provided where you will specify `./voca_pipeline.sh user_output.wav`. The .wav file will be the recorded output from the user and this will be scripted to run a pipeline where it will send the input .wav audio to the pipeline.py file where this will use GPT3 to produce an output. After, VOCA should take the .mp3 output and show the .mp4 file of the talking head on the GUI once the "Listen to recording" button is pushed.
