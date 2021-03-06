import os
import re

from setuptools import find_packages, setup

regexp = re.compile(r".*__version__ = [\'\"](.*?)[\'\"]", re.S)

base_package = "ipy_course_tools"
base_path = os.path.dirname(__file__)

init_file = os.path.join(base_path, "ipy_course_tools", "__init__.py")
with open(init_file, "r") as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError("Cannot find __version__ in {}".format(init_file))

with open("README.rst", "r") as f:
    readme = f.read()

with open("CHANGELOG.rst", "r") as f:
    changes = f.read()


def parse_requirements(filename):
    """Load requirements from a pip requirements file"""
    with open(filename, "r") as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines


requirements = parse_requirements("requirements.txt")


if __name__ == "__main__":
    setup(
        name="ipy_course_tools",
        description="IPython - Jupyter course tools",
        long_description="\n\n".join([readme, changes]),
        license="MIT license",
        url="https://github.com/edualphacruncher/ipy-course-tools",
        version=version,
        author="Kovacs Mae",
        author_email="mate.kovacs@alphacruncher.com",
        maintainer="Kovacs Mae",
        maintainer_email="mate.kovacs@alphacruncher.com",
        install_requires=requirements,
        keywords=["ipy_course_tools"],
        packages=["ipy_course_tools"],
        zip_safe=False,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    )
