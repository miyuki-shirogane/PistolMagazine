MESSAGE ?= "checkpoint"
DATE := $(shell date '+%Y-%m-%dT%H:%M:%S%z')

# PyPI repository URL
PYPI_REPO := https://upload.pypi.org/legacy/

# Name of your package
PACKAGE_NAME := your_package_name

# Version of your package (assuming you manage version in __init__.py)
PACKAGE_VERSION := $(shell python -c "import your_package_name; print(your_package_name.__version__)")

# Clean previous build artifacts
clean:
	@echo "Cleaning previous build artifacts..."
	@rm -rf dist
	@echo "Clean finished."

# Build the package
build: clean
	@echo "Building $(PACKAGE_NAME) version $(PACKAGE_VERSION)..."
	@python setup.py sdist bdist_wheel
	@echo "Build finished."

# Upload the package to PyPI
upload: clean build
	@echo "Uploading $(PACKAGE_NAME) version $(PACKAGE_VERSION) to PyPI..."
	@twine upload --repository-url $(PYPI_REPO) dist/*
	@echo "Upload finished."

# Commit and push code changes to remote repository
checkpoint:
	@echo "Creating a git checkpoint..."
	@git add -A
	@git commit -m "$(MESSAGE) at $(DATE)"
	@git push
	@echo "Checkpoint created and pushed to remote."

# Perform both checkpoint and upload
release: checkpoint upload
	@echo "Code committed, pushed, and package uploaded to PyPI."
