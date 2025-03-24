# Note: You can use any Debian/Ubuntu based image you want.
FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm
RUN sudo apt-get update && sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
