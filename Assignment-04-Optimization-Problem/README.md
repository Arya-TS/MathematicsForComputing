# Assignment 04 – Optimization Problem

## Optimization of an Open-Top Box

### Objective

The objective of this assignment is to develop a mathematical model for a real-life optimization problem and use derivatives to determine the optimal solution.

In this experiment, an open-top box was constructed from a rectangular A4 sheet by cutting equal squares from the four corners and folding the sides upward. The aim was to determine the cut size that maximizes the volume of the resulting box.

### Sheet Dimensions

The rectangular sheet used for the experiment had dimensions:

* Length: **29.7 cm**
* Width: **18.7 cm**

If a square of side \(x\) cm is cut from each corner, the dimensions of the box become:

$$
\text{Length} = 29.7 - 2x
$$

$$
\text{Width} = 18.7 - 2x
$$

$$
\text{Height} = x
$$

Therefore, the volume is modeled as:

$$
V(x)=x(29.7-2x)(18.7-2x)
$$

which expands to:

$$
V(x)=4x^3-96.8x^2+555.39x
$$

### Methodology

The assignment follows these steps:

1. Construct the open-top box physically.
2. Collect volume measurements for different cut sizes.
3. Record the experimental data in Excel.
4. Plot the experimental data.
5. Fit a cubic polynomial to the collected data.
6. Evaluate the goodness of fit using \(R^2\).
7. Differentiate the fitted function.
8. Find the critical points by setting the first derivative to zero.
9. Apply the feasible-domain constraint and second derivative test.
10. Determine the cut size that maximizes the volume.

### Result

The mathematical optimization gives an optimal cut size of approximately:

$$
\boxed{x \approx 3.73\text{ cm}}
$$

The corresponding maximum volume is approximately:

$$
\boxed{V_{\max}\approx933\text{ cm}^3}
$$

### Files

* **`optimization.ipynb`** – Contains the data analysis, curve fitting, mathematical calculations, plots, differentiation, and optimization.
* **`box_experiment.xlsx`** – Contains the experimentally collected data.

### Conclusion

This experiment demonstrates how a real-life physical problem can be represented using a mathematical model and optimized using derivatives. The experimental data was used to obtain a cubic model, which was then differentiated to determine the cut size that produces the maximum possible volume of the open-top box.
