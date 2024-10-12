import numpy as np

def angle_to_vectors(vec_1, vec_2):
    vec_1_norm = np.linalg.norm(vec_1)
    vec_2_norm = np.linalg.norm(vec_2)
    vec_1_2_dot = np.dot(vec_1.T, vec_2)
    angle = np.arctan(vec_1_2_dot/(vec_1_norm*vec_2_norm))*360/np.pi
    return angle

def Proj_onto(vec_1, vec_2):
    vec_2_1_dot = np.dot(vec_2.T, vec_1)
    vec_2_dot = np.dot(vec_2.T, vec_2)
    proj_vec = (vec_2_1_dot/vec_2_dot)*vec_2
    return proj_vec

x = np.array([[1], [0]])
y = np.array([[4], [4]])
angle = angle_to_vectors(x, y)
projxy = Proj_onto(y, x)
print("문제 (a)")
print("x와 y가 이루는 각 = ", angle)
print("x의 x 위로의 정사영 = \n", projxy)
print("\n")

x = np.array([[1], [2], [5]])
y = np.array([[1], [-1], [2]])
angle = angle_to_vectors(x, y)
projxy = Proj_onto(y, x)
print("문제 (b)")
print("x와 y가 이루는 각 = ", angle)
print("x의 y 위로의 정사영 = \n", projxy)
print("\n")

x = np.array([[0], [-1], [2], [2]])
y = np.array([[1], [1], [3], [2]])
angle = angle_to_vectors(x, y)
projxy = Proj_onto(y, x)
print("문제 (c)")
print("x와 y가 이루는 각 = ", angle)
print("x의 y 위로의 정사영 = \n", projxy)
print("\n")