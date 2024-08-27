# Integration Using Trapezoidal Rule Numerical Method Implementation in Python

This repository contains a Python implementation of the Trapezoidal Rule for numerical integration. The code integrates a given function within specified limits and computes the area under the curve.

## Table of Contents
- [Trapezoidal Rule Theory](#trapezoidal-rule-theory)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Files in the Repository](#files-in-the-repository)
- [Input Parameters](#input-parameters)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

## Trapezoidal Rule Theory
The Trapezoidal Rule is a numerical technique to approximate the definite integral of a function. The idea is to divide the area under the curve into trapezoids rather than rectangles, which provides a more accurate estimate than the rectangular method.

### Formula:
The formula for the Trapezoidal Rule is:
   \[
   \int_{a}^{b} f(x) \, dx \approx \frac{(b - a)}{2n} \left[f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n)\right]
   \]
where \( n \) is the number of subintervals, \( a \) and \( b \) are the lower and upper limits of integration, respectively.

## Dependencies
No external libraries are required for this script.

## Installation
Simply clone the repository and run the script using any Python interpreter.

## Usage
1. Clone the repository.
2. Ensure the script is in the directory you want to work in.
3. Run the script using Python:
    ```sh
    python trapezoidal_rule.py
    ```
4. Provide the required inputs when prompted:
    - Enter the lower limit.
    - Enter the upper limit.
    - Enter the number of subintervals (\( N \)).

## Code Explanation
The code begins by defining the function to be integrated. It then takes the lower and upper limits of integration, and the number of subintervals as inputs. The script divides the interval into smaller subintervals and calculates the area of trapezoids under the curve to approximate the integral.

Below is a snippet from the code illustrating the main logic:

```python
def fnc(x):
    return x * x

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter the number of subintervals (N): "))

area = 0
a_i = a
diff = (b - a) / n

for i in range(1, n + 1):
    b_i = a_i + (diff * i)
    h = b_i - a
    area += h * (fnc(a) + fnc(b_i)) / 2
    a = b_i

print("The approximate area under the curve is:", area)
```

The code calculates and prints the approximate area under the curve using the Trapezoidal Rule formula.

## Example
Below is an example of how to use the script:

**Run the script**:
```sh
python trapezoidal_rule.py
```

**Enter the input values**:
```
Enter lower limit: 0
Enter upper limit: 1
Enter the number of subintervals (N): 10
```

**Output**:
```
The approximate area under the curve is: 0.335... (This value will vary depending on the approximation)
```

## Files in the Repository
- `trapezoidal_rule.py`: The main script for performing numerical integration using the Trapezoidal Rule.

## Input Parameters
The script prompts for the following input values:
- **Lower Limit** (`a`): The lower bound of the definite integral.
- **Upper Limit** (`b`): The upper bound of the definite integral.
- **Number of Subintervals** (`n`): The number of subintervals to divide the area under the curve.

## Troubleshooting
1. **Input Values**: Ensure that the input values are appropriate for the function being integrated and cover the range of interest.
2. **Number of Subintervals**: A higher number of subintervals will provide a more accurate approximation but may increase computation time.
3. **Python Version**: This script is compatible with Python 3. Ensure you have Python 3 installed.

## Author
Script created by sudipto3331.

---

This documentation should guide you through understanding, installing, and using the Trapezoidal Rule script for numerical integration. For further issues or feature requests, please open an issue in the repository on GitHub. Feel free to contribute by creating issues and submitting pull requests. Happy coding!
