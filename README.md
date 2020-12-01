# Python training

## Author

Nicolas Barrier, IRD, UMR Marbec ([www.nicolasbarrier.fr/](https://www.nicolasbarrier.fr/))

## How to use class materials

### With notebooks

Download and install [Anaconda](https://www.anaconda.com/products/individual) for **Python 3.7**.

When done, open a Terminal and type: 

```
conda install jupytext
```

**Be sure that the `conda` exectuable is visible by your Shell!**

Download the Notebooks (clone the file or download the zip archive). Then, open
any of the `.py` file using the `jupyter notebook`. For instance, to open the class about object programming, type in a terminal:

```
cd oop
jupyter notebook oop.py &
```

Then annotate the file at will.

### With Spyder

Launch `Spyder` and open any of the `.py` file. Then run code selections or the entire code.

## Program

### Introduction
- [Introduction](introduction/intro.py) (description, applications)
- [Getting started](introduction/start.py) (install, running)
- [Installing libraries](introduction/libinstall.py)

### Data types
- [Variable definition](data_types/vars.py)
- [Numerical variables](data_types/numerics.py)
- [List](data_types/list.py)
- [Dictionaries](data_types/dict.py)
- [String](data_types/string.py)
- [Numpy arrays](data_types/numpy.py) (Scipy, Numpy libraries)

### Conditional statements, loops, functions (blocks)
- [Conditional statements](blocks/ifsta.py)
- [Loops](blocks/loops.py)
- [Functions](blocks/functions.py)

### Graphics ([Matplotlib](https://matplotlib.org/))

- [XY](plots/xy.py)
- [Contours](plots/contours.py)
- [Geometrical shapes](plots/geometrical_shapes.py)
- [Panels](plots/panels.py)
- [Quivers](plots/quivers.py)
- [Scatter plots](plots/scatters.py)
- [Text and maths](plots/text.py)
- [Axes management](plots/axes.py)
- [Configutation](plots/pyplot_settings.py)

### Object oriented programming
- [Class definition](oop/oop.py)

### IO
- [Text](io/text.py)
- [CSV](io/pand.py) (*pandas*)
- [NetCDF](io/xar.py) (*xarray*)

### Maps
- [Cartopy](maps/cartopy.py)
- [PyNGL](maps/pyngl.py)
