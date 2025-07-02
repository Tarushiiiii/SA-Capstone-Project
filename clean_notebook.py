import nbformat
import sys

def clean_widget_metadata(notebook_path, output_path=None):
    # Load notebook
    nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)

    # Remove widget metadata if it exists
    if "widgets" in nb.metadata:
        print("Removing 'widgets' metadata...")
        del nb.metadata["widgets"]
    else:
        print("No 'widgets' metadata found.")

    # Save output
    output_path = output_path or notebook_path
    nbformat.write(nb, output_path)
    print(f"Notebook cleaned: {output_path}")

if __name__ == "__main__":
    input_file = sys.argv[1]  # e.g., notebook.ipynb
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    clean_widget_metadata(input_file, output_file)
