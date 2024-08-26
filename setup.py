from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="img_process",
    version="0.0.10",
    author="Charles",
    description="Processamento imagem usando Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Uandsu/img_process",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5'
)
