from setuptools import setup, find_packages

setup(
    name="applegreen-common",
    version="0.1.4",
    packages=find_packages(),
    install_requires=[
        "bcrypt",
        "cryptography",
        "fastapi",
        "httpx"
        "pyjwt",
        "pymysql"
    ],
    description="applegreen common python utility modules",
    author="boom!e",
    author_email="yellowfox07@gmail.com",
    url="https://github.com/pastelstore/applegreen-common.git",
    license="Apache Software License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
