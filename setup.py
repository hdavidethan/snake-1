import pip

# Get the list of packages to install
packages = ["pygame"]

# Install the packages
for package in packages:
    pip.main(["install", package])