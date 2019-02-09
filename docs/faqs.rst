Frequently asked Questions
##########################

=============
Common Issues
=============


Static TLS errors
-----------------

I get an error stating::

    OSError: dlopen: cannot load any more object with static TLS

when running validation testing.


This has been known to occur in SLURM or related job-batch systems when loading the Adept library for auto-differentiation execution. To work around this, you should set the `environment variable LD_PRELOAD`_, e.g.::

    LD_PRELOAD=/path/to/adept/install/lib/libadept.so python -m pyjac.functional_tester ...


.. _environment variable LD_PRELOAD: https://stackoverflow.com/a/45640803/1667311

I get an error complaining that the function `timersub` doesn't exist!
----------------------------------------------------------------------

To fix this, add the following to your ``siteconf.py``::

    CC_FLAGS = ['-D_BSD_SOURCE -D_SVID_SOURCE -D_POSIX_C_SOURCE=200809']

I get Segmentation Faults when testing the Jacobian with nosetests!
-------------------------------------------------------------------

This issue is (likely) due to `incompatibilities in GLIBC`_ between the build servers
used by Conda-Forge used to compile the binary Adept library for distribution and your
system.  This bug has typically been reported on Ubuntu systems.

The easiest work around is to remove the Conda-Forge version of Adept::

    conda remove adept

And then build a copy locally on your machine.  The following commands will build
and install Adept to the currently active Conda environment::

    wget http://www.met.reading.ac.uk/clouds/adept/adept-2.0.5.tar.gz
    ./configure --prefix=${CONDA_PREFIX} --with-blas=openblas LDFLAGS="-L${CONDA_PREFIX}/lib -Wl,-rpath,${CONDA_PREFIX}/lib" CXXFLAGS='-g -O2 -fopenmp'
    make -j 2
    make check
    make install


.. _incompatibilties in GLIBC: https://stackoverflow.com/a/45640803/1667311
