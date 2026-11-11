import os

import pytest
from anndata import read_h5ad
from dotenv import load_dotenv

import tacco as tc

methods = [
    "NMFreg",
    "WOT",
    "OT",
    "nnls",
    "svm",
    "RCTD",
    "SingleR",
    "tangram",
    "novosparc",
    "projection",
]
load_dotenv()
query = read_h5ad(os.getenv("QUERY_PATH"))  # type: ignore
reference = read_h5ad(os.getenv("REFERENCE_PATH"))  # type: ignore


@pytest.mark.parametrize("method", methods)
def test_annotation(method: str):
    tc.tl.annotate(query, reference, "cluster")
