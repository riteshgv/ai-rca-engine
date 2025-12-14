from setuptools import setup, find_packages

setup(
    name="ai-rca-engine",
    version="0.1.0",
    description="AI-powered Root Cause Analysis engine for logs",
    author="Ritesh Vishwakarma",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "chromadb",
        "sentence-transformers",
    ],
    entry_points={
        "console_scripts": [
            "rca=src.cli.rca_cli:main"
        ]
    },
)

