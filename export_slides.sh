#! /usr/bin/bash

# Export to slides
jupyter nbconvert MultiAgentDemoPresentation.ipynb --to slides --no-input --no-prompt

# Export to PDF
jupyter nbconvert MultiAgentDemoPresentation.ipynb --to pdf --no-input --no-prompt