from setuptools import setup, find_packages

setup(
    name="common-util",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cryptography",
        "fastapi",
        "pymysql"
    ],
    description="applegreen common python utility modules",
    author="boom!e",
    author_email="yellowfox07@gmail.com",
    url="https://github.com/pastelstore/common-util.git",
    license="Apache Software License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
