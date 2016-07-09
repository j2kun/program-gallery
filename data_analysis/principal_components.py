import numpy


def principalComponents(matrix):
    # Columns of matrix correspond to data points, rows to dimensions.

    deviationMatrix = (matrix.T - numpy.mean(matrix, axis=1)).T
    covarianceMatrix = numpy.cov(deviationMatrix)
    eigenvalues, principalComponents = numpy.linalg.eig(covarianceMatrix)

    # sort the principal components in decreasing order of corresponding eigenvalue
    indexList = numpy.argsort(-eigenvalues)
    eigenvalues = eigenvalues[indexList]
    principalComponents = principalComponents[:, indexList]

    return eigenvalues, principalComponents
