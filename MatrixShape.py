def find_matrix_shape(matrix):
    """
    Returns the shape of a matrix as a tuple (rows, columns).

    Parameters:
        matrix (list of lists): The matrix whose shape is to be determined.

    Returns:
        tuple: A tuple containing the number of rows and columns (rows, columns).
    """
    if not matrix or not isinstance(matrix, list):
        return (0, 0)

    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    return (rows, columns)
