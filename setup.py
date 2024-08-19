from setuptools import setup, find_packages

setup(
    name="logging-tools",
    version="0.1.1",
    url="https://github.com/KaribuLab/python-logging-tools",
    license="Apache Software License",
    author="Patricio Ascencio",
    author_email="paascencio@gmail.com",
    description="Python Logging Tools",
    python_requires=">=3.12",
    packages=find_packages(),
    include_package_data=True,
    platforms=["MacOS X", "Linux", "Windows"],
)
