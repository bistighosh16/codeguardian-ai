"""
Setup configuration for CodeGuardian
Made with 💜 by Vivi
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codeguardian-ai",
    version="0.1.0",
    author="Vivi (Bisti Ghosh)",
    author_email="your.email@example.com",
    description="AI-powered code review assistant for your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bistighosh16/codeguardian-ai",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Tools",
    ],
    python_requires=">=3.11",
    install_requires=[
        "typer==0.9.4",
        "rich==13.7.0",
        "groq==0.4.1",
        "gitpython==3.1.41",
        "pyyaml==6.0.1",
        "python-dotenv==1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "codeguardian=codeguardian.cli:main",
        ],
    },
)