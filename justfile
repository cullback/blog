install:
    brew install zola

run:
    zola serve

format:
    mdformat content
    ruff format content
