#! /usr/bin/bash

# Export to slides
jupyter nbconvert  MultiAgentDemoPresentation.ipynb --to slides --output-dir='./docs' --output='index' --no-input --no-prompt
mv ./docs/index.slides.html ./docs/index.html

# Export to PDF
jupyter nbconvert MultiAgentDemoPresentation.ipynb --to pdf --no-input --no-prompt