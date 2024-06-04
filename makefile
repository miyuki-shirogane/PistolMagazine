MESSAGE ?= "checkpoint"
DATE := $(shell date '+%Y-%m-%dT%H:%M:%S%z')

# PyPI repository URL
PYPI_REPO := https://upload.pypi.org/legacy/

# Name
PACKAGE_NAME := PistolMagazine

# Version of PistolMagazine
PACKAGE_VERSION := $(shell python3 -c "import PistolMagazine; print(PistolMagazine.__version__)")

# Clean previous build artifacts
clean:
	@echo "Cleaning previous build artifacts..."
	@rm -rf build dist *.egg-info
	@echo "Clean finished."

# Build the package
build: clean
	@echo "Building $(PACKAGE_NAME) version $(PACKAGE_VERSION)..."
	@python3 setup.py sdist bdist_wheel
	@echo "Build finished."

# Upload the package to PyPI
upload: build
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

# Tag the current version
tag:
	@echo "Tagging the version $(PACKAGE_VERSION)..."
	@git tag -a v$(PACKAGE_VERSION) -m "Release version $(PACKAGE_VERSION)"
	@git push origin v$(PACKAGE_VERSION)
	@echo "Version $(PACKAGE_VERSION) tagged and pushed to remote."

# Perform both checkpoint, tag, and upload
release: checkpoint tag upload
	@echo "Code committed, tagged, pushed, and package uploaded to PyPI."
