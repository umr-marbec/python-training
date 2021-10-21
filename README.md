# Python training

## Author

Nicolas Barrier, IRD, UMR Marbec ([www.nicolasbarrier.fr/](https://www.nicolasbarrier.fr/))

## How to use class materials

Download and install [Anaconda](https://www.anaconda.com/products/individual) for **Python 3**.

Create a Conda environment as follows:

```
conda create --name python-training
conda activate python-training
```

When done, open a Terminal and install the libraries:

```
conda install -c conda-forge -y netCDF4
conda install -c conda-forge -y xarray
conda install -c conda-forge -y dask
conda install -c conda-forge -y pandas
conda install -c conda-forge -y jupytext
conda install -c conda-forge -y jupyter
conda install -c conda-forge -y cartopy
conda install -c conda-forge -y shapefile
conda install -c conda-forge -y eofs
conda install -c conda-forge -y nc-time-axis
conda install -c conda-forge -y python-graphviz
```

Now, navigate to the folder containing the training sessions and type:

```
jupyter notebook &
```

Then open/run/annotate the file at will.

## Program

### Introduction
- Introduction (introduction/intro.py) (description, applications)
- Getting started (introduction/start.py) (install, running)
- Installing libraries (introduction/libinstall.py)

### Data types
- Variable definition (data_types/vars.py)
- Numerical variables (data_types/numerics.py)
- List (data_types/list.py)
- Dictionaries (data_types/dict.py)
- String (data_types/string.py)
- Numpy arrays (data_types/nmp.py) (Scipy, Numpy libraries)

### Conditional statements, loops, functions  (blocks)
- Conditional statements (blocks/ifsta.py)
- Loops (blocks/loops.py)
- Functions (blocks/functions.py)

### Graphics  (Matplotlib(https://matplotlib.org/))

- XY (plots/xy.py)
- Contours (plots/contours.py)
- Geometrical shapes (plots/geometrical_shapes.py)
- Panels (plots/panels.py)
- Quivers (plots/quivers.py)
- Scatter plots (plots/scatters.py)
- Text and maths (plots/text.py)
- Axes management (plots/axes.py)
- Configutation (plots/pyplot_settings.py)

### Object oriented programming
- Class definition (oop/oop.py)

### IO
- Text (io/text.py)
- CSV (io/pand.py) (*pandas*)
- NetCDF (io/xar.py) (*xarray*)

### Maps
- Cartopy (maps/carto.py)
- PyNGL (maps/pyngl.py)
