from setuptools import setup, find_packages

setup(
    name="calculatrice",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Golam Tamim",
    author_email="golam.tamim94@gmail.com",
    description="Une simple calculatrice en ligne de commande",
    keywords="calculatrice, math",
    url="https://github.com/Tamim94/Calculatrice",
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "calculatrice=calculatrice.main:main",
        ],
    },
)
