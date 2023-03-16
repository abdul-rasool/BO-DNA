
import numpy
import math

# define the function blocks
def prod(it):
    p = 1
    for n in it:
        p *= n
    return p


def Ufun(x, a, k, m):
    y = k * ((x - a) ** m) * (x > a) + k * ((-x - a) ** m) * (x < (-a))
    return y


def F1(x):
    s = numpy.sum(x ** 2)
    return s



def F6(x):
    o = numpy.sum(abs((x + 0.5)) ** 2)
    return o


def F9(x):
    dim = len(x)
    o = numpy.sum(x ** 2 - 10 * numpy.cos(2 * math.pi * x)) + 10 * dim
    return o



def F13(x):
    if x.ndim==1:
        x = x.reshape(1,-1)

    o = 0.1 * (
        (numpy.sin(3 * numpy.pi * x[:,0])) ** 2
        + numpy.sum(
            (x[:,:-1] - 1) ** 2
            * (1 + (numpy.sin(3 * numpy.pi * x[:,1:])) ** 2), axis=1
        )
        + ((x[:,-1] - 1) ** 2) * (1 + (numpy.sin(2 * numpy.pi * x[:,-1])) ** 2)
    ) + numpy.sum(Ufun(x, 5, 100, 4))
    return o


def F16(L):
    o = (
        4 * (L[0] ** 2)
        - 2.1 * (L[0] ** 4)
        + (L[0] ** 6) / 3
        + L[0] * L[1]
        - 4 * (L[1] ** 2)
        + 4 * (L[1] ** 4)
    )
    return o


def F19(L):
    aH = [[3, 10, 30], [0.1, 10, 35], [3, 10, 30], [0.1, 10, 35]]
    aH = numpy.asarray(aH)
    cH = [1, 1.2, 3, 3.2]
    cH = numpy.asarray(cH)
    pH = [
        [0.3689, 0.117, 0.2673],
        [0.4699, 0.4387, 0.747],
        [0.1091, 0.8732, 0.5547],
        [0.03815, 0.5743, 0.8828],
    ]
    pH = numpy.asarray(pH)
    o = 0
    for i in range(0, 4):
        o = o - cH[i] * numpy.exp(-(numpy.sum(aH[i, :] * ((L - pH[i, :]) ** 2))))
    return o
