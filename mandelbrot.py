# Example: Computing Mandelbrot set
import numpy as np

def mandelbrot(h, w, max_iters):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y*1j
    z = c
    divtime = max_iters + np.zeros(z.shape, dtype=int)

    for i in range(max_iters):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iters)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Set parameters
    width, height, max_iters = 800, 600, 256

    # Compute Mandelbrot set
    mandelbrot_set = mandelbrot(height, width, max_iters)

    # Display the result
    plt.imshow(mandelbrot_set, extent=(-2, 0.8, -1.4, 1.4), cmap='hot')
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()