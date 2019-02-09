Installation
############

A setup.py file is provided with pyJac. To install pyJac, call

.. code-block:: bash

    python configure.py
    python setup.py install

This method will allow you to use the basic code-generation functionality of pyJac,
however this will not enable pyJac's unit-testing capabilities.

.. note::
    Currently pyJac relies on some custom modifications to the ``loo.py`` package,
    which are still in the process of being merged upstream.  If you wish to
    use the ``setup.py`` installation route we recommend installing the dependencies
    from the requirements.txt file .. code-block:: bash

        pip install -r requirements.txt

    before running the ``setup.py`` installation command above, so that you get the
    correct version of ``loo.py`` installed.

Alteratively, you may install pyJac via ``conda`` to easily obtain the full list
of depenencies required for unit-testing and native ``OpenCL`` execution ..code-block:: bash

    conda create -y -n pyjac python=3 llvmdev clangdev cantera ocl-icd=*=h14c3975_1001 islpy pyyaml scipy pyopencl numpy Cython pytables flake8 pep8-naming pocl adept=*=he6fcbdd_3
    source activate pyjac
    export OCL_ICD_VENDORS=$CONDA_PREFIX/etc/OpenCL/vendors
    pip install -r requirements.txt
    pip install -r optional-requirements.txt
    python configure.py --cl-inc-dir="$CONDA_PREFIX/include" --cl-lib-dir="$CONDA_PREFIX/lib" --adept-lib-dir="$CONDA_PREFIX/lib" --adept-inc-dir="$CONDA_PREFIX/include"
    cp siteconf.py pyjac/
    pip install .

Finally, regular ``pip`` and ``conda`` package installations are forthcoming.


The Site Conf(ig) File
######################

pyJac borrows the very useful "siteconf" tool from ``pyopencl`` makes it relatively easy for the user to adjust paths, compilation flags, etc.

The siteconf.py file can be generated using ..code-block::

    python configure.py

where addition arguments can be include to:
* Set the OpenCL version to be used (``--cl-version``)
* Set the path to the OpenCL headers (``--cl-inc-dir``)
* Set the name of the OpenCL library to use (``--cl-libname``), defaults to ``libOpenCL.so``
* Set the path to the OpenCL library (``--cl-lib-dir``)
* Set the path to the Adept headers (``--adept-inc-dir``)
* Set the path to the Adept library (``--adept-inc-dir``)
* Specify additional flags to pass to the C-compiler (``--cc-flags``)
* Specify additional flags to pass to the C++-compiler (``--cxxflags``), defaults to ``-std=gnu++11``
* Specfiy additional flags to pass to the OpenCL-compiler (``--cl-flags``), and finally
* Specify any linker flags (``--ldflags``)
