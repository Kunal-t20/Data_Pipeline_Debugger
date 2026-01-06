import numpy as np
import faiss
from typing import List,Dict
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.model=SentenceTransformer("all-MiniLM-L6-v2")
        self.index=None
        self.documents:List[str]=[]
    
    def build(self,documents:List[str]):
        self.documents=documents
        embedding=self.model.encode(documents)
        embedding=embedding.astype('float32')

        self.dimension=embedding.shape[1]

        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embedding)

    def search(self,query:str,k:int=3):
        
        if self.index is None:
            raise ValueError("Index not built yet")
        
        q_vec=self.model.encode([query])

        q_vec=q_vec.astype("float32")

        distances,indices=self.index.search(q_vec,k)
        
        results = []

        for score, index in zip(distances[0], indices[0]):
            if index < len(self.documents):
                results.append({
                    "text": self.documents[index],
                    "score": float(score)
                })

        return results
        
        
   