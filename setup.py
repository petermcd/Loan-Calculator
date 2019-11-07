from setuptools import setup, find_packages

short_description = "Simple tool for working out length of loans" \
                    "based on payment amount."

with open("README.md") as readmeFile:
    readme = readmeFile.read()

additional_requirements = [
    "flake8",
    "pytest",
    "pytest-mock",
    "pytest-cov",
]

setup(
    name="Loan Calculator",
    version="0.1",
    description=readme,
    long_description=readme,
    author="Peter McDonald",
    maintainer="Peter McDonald",
    url="https://github.com/petermcd/Loan-Calculator",
    download_url="https://github.com/petermcd/Loan-Calculator",
    license="MIT",
    keywords="mortgage,loan",
    setup_requires=(
        "pytest-runner"
    ),
    tests_require=additional_requirements,
    extras_require={"test": additional_requirements},
    packages=find_packages(
        where="loan_calculator"
    ),
)
