# Descriptive Statistics

A LaTeX Beamer presentation on **Descriptive Statistics** prepared for the **Maths for Computing** course in the **M.Tech Artificial Intelligence & Software Engineering** programme at **Cochin University of Science and Technology (CUSAT)**.

## Contents

The presentation covers the following topics:

### Foundations

* Statistics
* Data
* Information
* Knowledge
* Intelligence
* Types of Data

  * Univariate
  * Bivariate
  * Multivariate

### Descriptive Statistics

* Measures of Central Tendency

  * Mean
  * Median
  * Mode
* Measures of Dispersion

  * Range
  * Variance
  * Standard Deviation
  * Interquartile Range (IQR)
* Histogram
* Box Plot
* Outliers
* Skewness
* Kurtosis

### Sample Statistics

* Population and Sample
* Sample Mean
* Sample Variance
* Order Statistics
* Covariance
* Sample Covariance
* Correlation
* Sample Covariance Matrix

### Frequentist Statistics

* Introduction to Frequentist Statistics
* Sampling
* Sampling Distribution
* Standard Error
* Estimator, Estimate and Parameter
* Bias and Variance
* Mean Square Error
* Consistency
* Central Limit Theorem
* Confidence Intervals

### Model Estimation

* Parametric Model Estimation
* Maximum Likelihood Estimation
* Non-parametric Model Estimation
* Empirical CDF
* Kernel Density Estimation
* Parametric vs Non-parametric Model Estimation

### Applications

* Applications of Descriptive Statistics in Computing and Artificial Intelligence

## Project Structure

```text
Descriptive-Statistics/
├── main.tex
├── README.md
├── Descriptive-Statistics.pdf
│
├── sections/
│   ├── 01_foundations.tex
│   ├── 02_central_tendency.tex
│   ├── 03_dispersion.tex
│   ├── 04_data_visualization.tex
│   ├── 05_sample_statistics.tex
│   ├── 06_frequentist_statistics.tex
│   ├── 07_model_estimation.tex
│   ├── 08_applications_conclusion.tex
│   └── 09-thank-you.tex
│
├── figures/
│   ├── bivariate.jpg
│   ├── multivariate.png
│   ├── histogram.png
│   ├── boxplot.png
│   ├── outlier.png
│   ├── skewness.png
│   ├── kurtosis.jpg
│   ├── population_sample.png
│   ├── sampling_distribution.png
│   ├── clt.png
│   └── kde.jpg
│
├── references/
│   └── references.bib
│
└── screenshots/
    └── ...
```

## Files and Folders

* **`main.tex`** — Main LaTeX file that defines the presentation structure and includes the individual sections.
* **`sections/`** — Contains the LaTeX source files for each section of the presentation.
* **`figures/`** — Contains figures and diagrams used throughout the presentation.
* **`references/`** — Contains the BibTeX bibliography file used for references.
* **`screenshots/`** — Contains screenshots of the completed presentation and related work.
* **`Descriptive-Statistics.pdf`** — Compiled presentation.
* **`README.md`** — Project documentation.

## Presentation Design

The presentation is created using **LaTeX Beamer** with the **Madrid theme**.

The slides use:

* 16:9 widescreen aspect ratio
* Pastel blue and lavender colour scheme
* Mathematical notation using LaTeX
* Tables and structured layouts
* Diagrams and figures
* Bibliographic references using BibTeX

## Compilation

The presentation can be compiled using a LaTeX environment such as **Overleaf**.

The main entry point is:

```text
main.tex
```

The individual section files are included using LaTeX's `\input{}` command.

## Output

The final compiled presentation is provided as:

```text
Descriptive-Statistics.pdf
```

## Course

**Course:** Maths for Computing
**Programme:** M.Tech Artificial Intelligence & Software Engineering
**Institution:** Cochin University of Science and Technology (CUSAT)

## Author

**Arya T S**
