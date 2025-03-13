import numpy as np
import pandas as pd

def numpy():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[4, 5, 6], [7, 8, 9]])
    vert_stack = np.vstack([A, B])
    horiz_stack = np.hstack([A, B])
    common_elements = np.intersect1d(A, B)
    filtered_numbers = A[(A >= 5) & (A <= 10)]
    filtered_rows = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]
    print(A)
    print(B)
    print(vert_stack)
    print(horiz_stack)
    print(common_elements)
    print(filtered_numbers)
    print(filtered_rows)
def pandas():
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
    filtered_df = df.loc[::20, ['Manufacturer', 'Model', 'Type']]

    df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
    df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

    df2 = pd.DataFrame(np.random.randint(1, 50, size=(25, 4)))
    filtered_df2 = df2[df2.sum(axis=1) > 100]
numpy()
pandas()

