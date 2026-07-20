"""Setup configuration for AI Career Mentor"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ai-career-mentor',
    version='1.0.0',
    author='Yash Kunjir',
    author_email='yashkunjir2006@gmail.com',
    description='AI-powered career guidance platform for students',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yashkunjir2006-commits/ai-career-mentor',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Flask>=2.3.0',
        'Flask-SQLAlchemy>=3.0.0',
        'Flask-JWT-Extended>=4.4.0',
        'scikit-learn>=1.3.0',
        'pandas>=2.0.0',
        'numpy>=1.24.0',
    ],
)
