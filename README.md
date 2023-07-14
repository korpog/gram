# Gram-Schmidt process
Gram-Schimdt process is a method that takes a finite, linearly independent set of vectors $(v_1, v_2, ... , v_k)$ in the Euclidian space $R^n (k \leq n)$ with standard inner product
and transforms it into a set of orthogonal vectors $(u_1, u_2, ... , u_k)$. The process follows this rule:

$$u_1 = v_1$$

$$w_k = v_k - \sum_{i=1}^{k-1} {\langle v_k, w_i \rangle \over \langle w_i, w_i \rangle} \cdot w_i $$

**Warning : due to rounding errors, the resulting vectors may not be truly orthogonal.**

