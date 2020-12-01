# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Getting started 
#
# ## Python Install
#
# ### Anaconda
#
# Is is strongly advised to install Python by using [Anaconda](https://www.anaconda.com/):
#
# - Ready to go Python, with the main libraries installed (Numpy, Scipy, Matplotlib)
# - Possibility to create multiple environments with different versions of Python and packages ([conda](https://conda.io/en/latest/)).
#
# In practice:
#    
# - Download the distribution corresponding to your system (cf. [Download](https://www.anaconda.com/distribution/#download-section))
# - Install it in a place where you have read and write access.
#
#
#
#
# ## Running Python
#
# ### Python console
#
# To run Python in normal mode, type in a terminal: 
#
# ```
# python
# ```
#
# <img src="figs/console.png" width="70%">
#
# ### Interactive Python console
#
# To run Python in interactive mode, type in a terminal: 
#
# ```
# ipython
# ```
#
# <img src="figs/ipython.png" width="70%">
#
# ### Spyder (IDE)
#
# To run the Python IDE, type in a terminal:
#
# ```
# spyder &
# ```
#
# <img src="figs/spyder.png" width="70%">
#
#
# ### Jupyter Notebook
#
# To run the Jupyter Notebook, type in a terminal:
#
# ```
# jupyter notebook &
# ```
#
# <img src="figs/notebook.png" width="70%">

# ## Running scripts
#
# Open a text editor and type in:
#
# ```
# import sys
#
# # my first program (comment)
# print('hello ', sys.argv)
# ```
#
# Save as ```hello.py```
#
# ### Running using python
#
# From the terminal type:
#
# ```
# python hello.py arg1 arg2 arg3
# ```
#
# You should see:
#
# ```
# hello  ['hello.py', 'arg1', 'arg2', 'arg3']
# ```
#
# <div class='alert alert-info'>
#     <strong>Note: </strong>The <i>sys.argv</i> statements returns the list of arguments, with the 1st element the name of the script.
# </div>
#
#
# ### Running using ipython
#
# Open `ipython` from the terminal, then type:
#
# ```
# run hello.py arg1 arg2 arg3
# ```
#
# To check the environment, type `whos`. You should see:
#
# ```
# In [2]: whos
# Variable   Type      Data/Info
# ------------------------------
# sys        module    <module 'sys' (built-in)>
# ```
#
# ### Running from Spyder
#
# Open `spyder`, open the file and click on the **Run -> Configuration per file** menu. Add arguments to the program as follows:
#     
# <img src="figs/args_spyder.png" width="40%">
#
# Then, click on the **Run file** button to run all the program or the **Run selection** button to run the current line 
#
# <br>  
# <figure>
#     <center>
#     <img src="figs/run_file.png" width="50" text-align=center>
#     <figcaption text-align=center><i>Run file button</i></figcaption>
# </figure>
#
# <br>    
# <figure>
#     <center>
# <img src="figs/run_sel.png" width="50">
#         <figcaption text-align=center><i>Run selection button</i></figcaption>
# </figure>
