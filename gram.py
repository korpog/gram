import numpy as np

def get_vectors() -> list:
    list_of_vecs = []
    dim = int(input("Enter space dimension:"))
    while True:
        print(f"Enter {dim} space-separeted values of a vector. Enter 'q' to quit. ")
        vals = input()
        if (vals == "q"):
            break
        vec = [int(x) for x in vals.split()]
        if (len(vec) != dim):
            raise ValueError("Number of values in the vector must be equal to the space dimension!")
        list_of_vecs.append(np.array(vec))
    return list_of_vecs

def orthogonalization(vectors) -> list:
    ortho_vectors = []
    for k in range(len(vectors)):
        if k == 0:
            ortho_vectors.append(vectors[0])
        else:
            for i in range(k):
                dot = vectors[k].dot(ortho_vectors[i]) / ortho_vectors[i].dot(ortho_vectors[i])
                projection_operator  = dot * ortho_vectors[i]
                vectors[k] = vectors[k] - projection_operator
            ortho_vectors.append(vectors[k])
    return ortho_vectors

if __name__ == "__main__":
    vecs = get_vectors()
    result = orthogonalization(vecs)
    print("Your new orthogonal set of vectors: ")
    for r in result:
        print(r.tolist())
