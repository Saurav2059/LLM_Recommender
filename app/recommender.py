from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_index(products):
    vectors = [model.encode(p.description) for p in products]
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(np.array(vectors))
    return index, vectors

def recommend_products(query, products):
    index, _ = build_index(products)
    q_vec = model.encode(query).reshape(1, -1)
    D, I = index.search(q_vec, k=5)
    return [products[i] for i in I[0]]