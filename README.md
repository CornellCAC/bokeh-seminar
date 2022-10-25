### Interactive Data Visualization with Bokeh

This repository contains a jupyter notebook, along with associated figures and source code files, that provide an introduction to Bokeh (bokeh.org), a Python package supporting interactive data visualization within web browsers.

The notebook was used as the basis for a CAC Research Computing Seminar on 10/26/2022 at Cornell University.  The notebook will also be linked to an upcoming online training roadmap showcasing Bokeh as part of the Cornell Virtual Workshop (cvw.cac.cornell.edu).

To run the code in this notebook, the following Python packages are required:

* bokeh
* pandas
* jupyter
* networkx

In addition, to be able to run the notebook in slide mode, the following package is also needed, but it is not required to run the notebook in typical browser mode:

* rise

If you have the default Anaconda Python Distribution installed, the required packages are probably already installed as part of the large collection of packages managed by Anaconda.

If you have conda installed and want to create a conda environment to run this notebook, execute this command to create a new environment called "bokeh_env":

```conda create -n bokeh_env bokeh pandas jupyter networkx     # and optionally add rise to the list if desired```

If you want to create a python virtual environment instead, and want to use pip to install the packages, do the following:

```python -m venv bokeh_env ; source bokeh_env/bin/activate ; pip install bokeh pandas jupyter networkx```

