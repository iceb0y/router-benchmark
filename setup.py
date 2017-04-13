from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name = 'router-benchmark',
    ext_modules = cythonize([
        Extension(
            '_r3',
            ['_r3.pyx'],
            libraries=['r3'],
        ),
    ]),
)
