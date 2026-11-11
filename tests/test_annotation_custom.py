import os

import pytest
from anndata import read_h5ad
from dotenv import load_dotenv

import tacco as tc

methods = [
    "NMFreg",
    # "WOT",  # Requires the optional wot package, which is not installed here.
    "OT",
    "nnls",
    "svm",
    # "RCTD",  # Requires Rscript and the RCTD/spacexr R package.
    # "SingleR",  # Requires Rscript and the SingleR R package.
    # "tangram",  # Requires the optional tangram package in the subprocess Python environment.
    # "novosparc",  # Requires the optional novosparc package, which is not installed here.
    "projection",
]
load_dotenv()
query = read_h5ad(os.getenv("QUERY_PATH"))  # type: ignore
reference = read_h5ad(os.getenv("REFERENCE_PATH"))  # type: ignore


@pytest.mark.parametrize("method", methods)
def test_annotation(method: str):
    tc.tl.annotate(query, reference, "cluster", method=method)
