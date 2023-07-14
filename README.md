# Gram-Schmidt process
Gram-Schimdt process is a method that takes a finite, linearly independent set of vectors $(v_1, v_2, ... , v_k)$ in the Euclidian space $R^n (k \leq n)$ with standard inner product
and transforms it into a set of orthogonal vectors $(u_1, u_2, ... , u_k)$. The process follows this rule:

$$u_1 = v_1$$

$$u_k = v_k - \sum_{i=1}^{k-1} {\langle v_k, u_i \rangle \over \langle u_i, u_i \rangle} \cdot u_i $$

**Warning : due to rounding errors, the resulting vectors may not be truly orthogonal.**

How to run this script? (Linux)

0. Make sure Python is installed on your computer
1. `git clone` or download ZIP with this repository
2. In the directory containing `gram.py` create a virtual environment and activate it
   - `python3 -m venv <MYVENV>`
   - `source MYENV/bin/activate`
3. Install numpy - `pip install numpy`
4. Run the script - `python gram.py`


