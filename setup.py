from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="hello_world",
    version="0.0.1",
    author="mauricio",
    author_email="mauriciopicirillo@gmail.com",
    description="Entendendo como funciona os pacotes no Python",
    long_description="Criado um Hello World para entender melhor como funciona os pacotes no Python",
    long_description_content_type="text/markdown",
    url="https://github.com/mauriciopicirillo/hello_world"
    packages=find_packages('hello_world', "module1_name"),
    install_requires=requirements,
    python_requires='>=3.8',