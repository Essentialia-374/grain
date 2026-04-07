"""Setup.py file for grain.

Most project configs are in `pyproject.toml` -- prefer to modify
`pyproject.toml` over this file if possible.
"""

import pybind11
import setuptools
from setuptools import dist
from setuptools import Extension


class BinaryDistribution(dist.Distribution):
  """This class makes 'bdist_wheel' include an ABI tag on the wheel."""

  def has_ext_modules(self):
    return True


setuptools.setup(
    ext_modules=[
        Extension(
            "grain._src.python.experimental.index_shuffle.python.index_shuffle_module",
            sources=[
                "grain/_src/python/experimental/index_shuffle/python/index_shuffle_module.cc",
                "grain/_src/python/experimental/index_shuffle/index_shuffle.cc",
            ],
            include_dirs=[pybind11.get_include(), "."],
            extra_compile_args=["-std=c++17"],
            language="c++",
        )
    ],
    distclass=BinaryDistribution,
)
