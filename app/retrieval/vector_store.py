import faiss
import numpy as np
import pickle
from pathlib import Path


class SHLVectorStore:

    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add(self, embeddings, metadata):

        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)

        self.metadata.extend(metadata)

    def save(self, folder):

        folder = Path(folder)

        folder.mkdir(parents=True, exist_ok=True)

        faiss.write_index(
            self.index,
            str(folder / "shl_index.faiss")
        )

        with open(folder / "metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, folder):

        folder = Path(folder)

        self.index = faiss.read_index(
            str(folder / "shl_index.faiss")
        )

        with open(folder / "metadata.pkl", "rb") as f:
            self.metadata = pickle.load(f)