from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="liguagem_do_L",
    version="0.0.1",
    author="Felipe",
    author_email="massigna@gmail.com",
    description="Troca do 'R'pelo 'L'",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/felipemassignan/linguagem_do_L.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)