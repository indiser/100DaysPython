import nbformat

# Load bad notebook
nb = nbformat.read("pdftoaudiobook.ipynb", as_version=4)

# Remove widgets metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Save fixed notebook
nbformat.write(nb, "pdftoaudiobook.ipynb")