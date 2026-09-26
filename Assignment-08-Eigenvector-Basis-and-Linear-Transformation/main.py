import numpy as np
import matplotlib.pyplot as plt


def read_points(filename):
    points = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            values = list(map(float, line.split()))

            if len(values) == 3:
                points.append(values)

    return np.array(points)


def read_matrix():
    print("\nEnter the 3x3 transformation matrix.")
    print("Enter one row at a time.")

    matrix = []

    for i in range(3):
        while True:
            try:
                row = list(
                    map(
                        float,
                        input(f"Enter row {i + 1}: ").split()
                    )
                )

                if len(row) != 3:
                    print("Please enter exactly 3 values.")
                else:
                    matrix.append(row)
                    break

            except ValueError:
                print("Please enter numbers only.")

    return np.array(matrix)


def plot_normal_basis(ax, original_points, transformed_points):

    ax.scatter(
        original_points[:, 0],
        original_points[:, 1],
        original_points[:, 2],
        label="Original points",
        s=50
    )

    ax.scatter(
        transformed_points[:, 0],
        transformed_points[:, 1],
        transformed_points[:, 2],
        label="Transformed points",
        s=50,
        marker="^"
    )

    for p, q in zip(original_points, transformed_points):
        ax.plot(
            [p[0], q[0]],
            [p[1], q[1]],
            [p[2], q[2]],
            linestyle="--",
            alpha=0.5
        )

    axis_length = max(
        3,
        np.max(np.abs(transformed_points)) * 1.2
    )

    ax.quiver(
        0, 0, 0,
        axis_length, 0, 0,
        color="red",
        arrow_length_ratio=0.08
    )

    ax.quiver(
        0, 0, 0,
        0, axis_length, 0,
        color="green",
        arrow_length_ratio=0.08
    )

    ax.quiver(
        0, 0, 0,
        0, 0, axis_length,
        color="blue",
        arrow_length_ratio=0.08
    )

    ax.text(axis_length, 0, 0, "X")
    ax.text(0, axis_length, 0, "Y")
    ax.text(0, 0, axis_length, "Z")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_title("Normal Basis")
    ax.legend()


def plot_eigen_basis(ax, points, eigenvectors):

    eigen_coordinates = np.linalg.solve(
        eigenvectors,
        points.T
    ).T

    ax.scatter(
        eigen_coordinates[:, 0],
        eigen_coordinates[:, 1],
        eigen_coordinates[:, 2],
        s=50,
        label="Points in eigen basis"
    )

    axis_length = max(
        3,
        np.max(np.abs(eigen_coordinates)) * 1.2
    )

    ax.quiver(
        0, 0, 0,
        axis_length, 0, 0,
        color="red",
        arrow_length_ratio=0.08
    )

    ax.quiver(
        0, 0, 0,
        0, axis_length, 0,
        color="green",
        arrow_length_ratio=0.08
    )

    ax.quiver(
        0, 0, 0,
        0, 0, axis_length,
        color="blue",
        arrow_length_ratio=0.08
    )

    ax.text(
        axis_length, 0, 0,
        "Eigenvector 1"
    )

    ax.text(
        0, axis_length, 0,
        "Eigenvector 2"
    )

    ax.text(
        0, 0, axis_length,
        "Eigenvector 3"
    )

    ax.set_xlabel("Eigenvector 1 coordinate")
    ax.set_ylabel("Eigenvector 2 coordinate")
    ax.set_zlabel("Eigenvector 3 coordinate")

    ax.set_title("Eigenvector Basis")
    ax.legend()


filename = "input.txt"

A = read_matrix()

print("\nTransformation Matrix:")
print(A)

points = read_points(filename)

print("\nOriginal Points:")
print(points)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

if np.linalg.matrix_rank(eigenvectors) < 3:
    print("\nThe matrix does not have 3 linearly independent eigenvectors.")
    print("Therefore, a complete eigenvector basis does not exist.")
else:
    print("\nThe matrix has an eigenvector basis.")
    print("Therefore, the matrix is diagonalizable.")

transformed_points = points @ A.T

print("\nTransformed Points:")
print(transformed_points)

fig = plt.figure(figsize=(15, 7))

ax1 = fig.add_subplot(121, projection="3d")

plot_normal_basis(
    ax1,
    points,
    transformed_points
)

ax2 = fig.add_subplot(122, projection="3d")

if np.linalg.matrix_rank(eigenvectors) == 3:
    plot_eigen_basis(
        ax2,
        points,
        eigenvectors
    )
else:
    ax2.text(
        0.5,
        0.5,
        0.5,
        "No complete eigenvector basis",
        ha="center",
        va="center"
    )

    ax2.set_title("Eigenvector Basis")

plt.tight_layout()
plt.show()