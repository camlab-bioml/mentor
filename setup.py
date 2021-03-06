import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="margo",
    version="0.0.5",
    author="Jinyu Hou",
    author_email="jhou@lunenfeld.ca",
    description="A tool that generates yaml cell type marker which maps cell types to gene expression.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/camlab-bioml/margo",
    packages=["margo"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="GPLv2",
    install_requires=["pandas", "pyyaml", "argparse", "rootpath", "requests", "anndata"],
    include_package_data=True,
    scripts=["bin/margo"],
)
