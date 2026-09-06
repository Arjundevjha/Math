# Graph Report - Math-Supreme  (2026-09-04)

## Corpus Check
- 193 files · ~37,874 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1445 nodes · 2288 edges · 127 communities (111 shown, 16 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 30 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `648ca3c8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Newton-Raphson & Root Finding
- Binomial Theorem
- Differentiation Chain & Second Derivative Rules
- Test Algebra Testevaluatepolynomial Module
- Trigonometric Integration
- Factor Theorem Testing
- Linear Equation Solvers
- Factor Theorem Testing
- Test Calculus Testformatpolynomialchainrule Module
- Calculus Quotient Rule
- Trigonometry Cosine Rule
- Euler's Number Constants
- Remainder Theorem Algebra
- Simple Polynomial Differentiation
- Pascal's Triangle Combinatorics
- Trigonometric Tangent Functions
- Remainder Theorem Algebra
- Test Quadratic Testsolvequadratic Module
- Factorial Discrete Module
- Greatest Common Divisor (GCD)
- Calculus Chain Rule
- Least Common Multiple (LCM)
- Descriptive Statistics (Mode)
- Descriptive Statistics (Mean)
- Calculus Chain Rule
- Partition Test Discretetest Module
- Trigonometric Tangent Functions
- Binomial Theorem
- Test Slope Testcalculateslope Module
- Euclidean Area (Triangle)
- Euclidean Volume (Cone)
- Euclidean Volume (Cylinder)
- Calculus Quotient Rule
- Simple Interest Math
- Integration Format Module
- Euclidean Area (Rectangle)
- Euclidean Volume (Sphere)
- Descriptive Statistics (Median)
- Test Calculus Testcalculusdifferentiation Module
- Integrate Polynomial Module
- Trigonometric Integration
- Approximation Partition Module
- Trigonometric Tangent Functions
- Test Intersection Intersection Module
- From Points Module
- Test Midpoint Testmidpointformula Module
- Polynomial Format Module
- Euclidean Area (Circle)
- Euclidean Area (Square)
- Euclidean Area (Square)
- Euclidean Volume (Cuboid)
- Inverse Trigonometry (Arctan)
- Trigonometric Tangent Functions
- Compound Interest Math
- Trinomial General Module
- Euclidean Area (Triangle)
- Trigonometric Sine Functions
- Inverse Trigonometry (Arctan)
- Inverse Trigonometry (Arctan)
- Trigonometric Tangent Functions
- Trigonometric Tangent Functions
- Geometry Volume Module
- Linear Equation Solvers
- Project Documentation & Guidelines
- Project Documentation & Guidelines
- Project Documentation & Guidelines
- Project Documentation & Guidelines
- Project Documentation & Guidelines
- Style Guide Module
- Style Guide Module
- Style Guide Module
- Style Guide Module
- Style Guide Module

## God Nodes (most connected - your core abstractions)
1. `evaluate_polynomial()` - 77 edges
2. `quotient_rule_derivative()` - 43 edges
3. `check_factor()` - 36 edges
4. `TestQuotientRule` - 33 edges
5. `chain_rule_derivative()` - 32 edges
6. `TestFormatPolynomialChainRule` - 30 edges
7. `compute_polynomial_derivative()` - 29 edges
8. `compute_polynomial_derivative_str()` - 28 edges
9. `nth_root()` - 25 edges
10. `TestEvaluatePolynomial` - 25 edges

## Surprising Connections (you probably didn't know these)
- `cubic_formula()` --implements--> `Dependency Elimination`  [EXTRACTED]
  Math/Algebra/Polynomials/cubic_formula.py → handoff.md
- `nth_root()` --implements--> `Newton-Raphson method`  [EXTRACTED]
  Math/Numerical_Methods/Functions/nth_root/nth_root.py → handoff.md
- `nth_root()` --implements--> `Precision Modes`  [EXTRACTED]
  Math/Numerical_Methods/Functions/nth_root/nth_root.py → handoff.md
- `test_NumericalMethods` --references--> `nth_root()`  [EXTRACTED]
  handoff.md → Math/Numerical_Methods/Functions/nth_root/nth_root.py
- `No Standard Math Module Rule` --semantically_similar_to--> `Number One Principle`  [INFERRED] [semantically similar]
  AGENTS.md → Style_Guide.MD

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Coding Restrictions and Dependency Policies** — agents_no_standard_math_module_usage, agents_internal_imports_first, style_guide_number_one_principle [EXTRACTED 1.00]
- **Standard Math Dependency Elimination** — math_numerical_methods_functions_nth_root_nth_root_nth_root, math_algebra_polynomials_cubic_formula_cubic_formula, math_algebra_polynomials_factor_theorem_factor_theorem, handoff_dependency_elimination [EXTRACTED 1.00]

## Communities (127 total, 16 thin omitted)

### Community 0 - "Newton-Raphson & Root Finding"
Cohesion: 0.09
Nodes (41): Dependency Elimination, Newton-Raphson method, Precision Modes, cubic_formula(), Solve cubic equations of the form ax³ + bx² + cx + d = 0 using the cubic formula, factor_theorem, nth_root(), Decimal (+33 more)

### Community 1 - "Binomial Theorem"
Cohesion: 0.06
Nodes (38): binomial_coefficient(), expand_binomial(), Expand the binomial (a + b)^n using the binomial theorem.      Parameters:     a, Calculate the binomial coefficient C(n, r).      Parameters:     n (int): The po, nCr(), Calculate combinations (nCr) using the formula: nCr = n! / (r! * (n - r)!)., expand_trinomial(), Calculate the general term in the trinomial expansion of (a + b + c)^n.      Par (+30 more)

### Community 3 - "Test Algebra Testevaluatepolynomial Module"
Cohesion: 0.04
Nodes (27): Test evaluating at x=0 with negative powers, expecting ZeroDivisionError, Test that zip handles mismatched list lengths by truncating to the shortest, Test with floating point values that might cause precision issues, Test with a simple quadratic polynomial: x^2 + 2x + 1 at x=2, Test polynomial at x=0, Test polynomial at x=-1, Test with fractional powers (square root), Test with float coefficients and float x (+19 more)

### Community 4 - "Trigonometric Integration"
Cohesion: 0.11
Nodes (10): integrate_cos(), Calculate the definite integral of cos(x) from a to b.      Parameters:     a (U, Test integral of cos(x) from pi/2 to 0 = -1, Test integral of cos(x) from pi/6 to pi/3 = (sqrt(3)/2 - 1/2), Test integral of cos(x) from 0 to pi = 0, Test integral of cos(x) over multiple periods, Test integral of cos(x) from 0 to 2*pi = 0, Test integral of cos(x) from -pi/2 to pi/2 = 2 (+2 more)

### Community 5 - "Factor Theorem Testing"
Cohesion: 0.09
Nodes (20): check_factor(), Check if (x - a) is a factor of a polynomial using the Factor Theorem.      Para, test_check_factor_empty(), test_check_factor_float(), test_check_factor_irrational(), test_check_factor_negative_powers(), test_check_factor_precision(), test_check_factor_true() (+12 more)

### Community 6 - "Linear Equation Solvers"
Cohesion: 0.12
Nodes (30): evaluate_polynomial(), format_polynomial(), Format a polynomial as a string.      Parameters:     coefficients (List[Union[i, Evaluate a polynomial at a given value of x.      Parameters:     coefficients (, test_evaluate_polynomial_all_zero_coeffs(), test_evaluate_polynomial_basic(), test_evaluate_polynomial_empty(), test_evaluate_polynomial_floating_point() (+22 more)

### Community 7 - "Factor Theorem Testing"
Cohesion: 0.09
Nodes (9): Test polynomial at x=0, Test polynomial at x=-1, Test with fractional powers (square root), Test with float coefficients and float x, Test with empty coefficients and powers, Test with negative powers, Test floating-point precision evaluation., Test evaluation with very large numbers. (+1 more)

### Community 9 - "Calculus Quotient Rule"
Cohesion: 0.06
Nodes (20): quotient_rule_derivative(), Apply the quotient rule to find the derivative of u(x) / v(x).      Parameters:, test_quotient_rule_derivative_basic(), test_quotient_rule_derivative_both_empty_edge(), test_quotient_rule_derivative_constant_denominator(), test_quotient_rule_derivative_constant_numerator(), test_quotient_rule_derivative_empty_denominator_edge(), test_quotient_rule_derivative_empty_lists() (+12 more)

### Community 10 - "Trigonometry Cosine Rule"
Cohesion: 0.07
Nodes (36): area_of_polygon(), Calculate the area of a regular polygon with n sides.      Parameters:     n (in, arcsin_numerical(), Calculate arcsine using numerical approximation by finding angle where sin(angle, cosine_taylor(), Calculate cosine using Taylor series expansion iteratively.      Parameters:, Calculate sine using Taylor series expansion iteratively.      Parameters:     r, sine_taylor() (+28 more)

### Community 11 - "Euler's Number Constants"
Cohesion: 0.09
Nodes (20): compute_eulers_number(), Decimal, Compute Euler's number (e) using the series expansion: e = Σ(1/n!) for n=0 to in, factorial_decimal(), Decimal, Calculate factorial as a Decimal for high precision.      Parameters:     n (int, Test factorial of zero is 1., Test factorial of one is 1. (+12 more)

### Community 12 - "Remainder Theorem Algebra"
Cohesion: 0.13
Nodes (12): Find the remainder when a polynomial is divided by (x - a) using the Remainder T, remainder_theorem(), Test with zero x and negative power, Test with mismatched lengths of coefficients and powers, Test P(x) = x^2 - 3x + 2 divided by (x - 3). Remainder = P(3)., Test division by exact factor where remainder should be 0., Test dividing by (x - a) where a is negative, i.e., (x + 2) -> a = -2., Test with float values. (+4 more)

### Community 13 - "Simple Polynomial Differentiation"
Cohesion: 0.15
Nodes (4): differentiate_polynomial(), Differentiate a polynomial using the power rule.      Parameters:     coeffs (Li, TestDifferentiatePolynomial, TestDifferentiatePolynomial

### Community 14 - "Pascal's Triangle Combinatorics"
Cohesion: 0.11
Nodes (15): generate_pascals_triangle(), print_pascals_triangle(), Print Pascal's triangle in a formatted way.      Parameters:     triangle (List[, Generate Pascal's triangle with num_rows rows.      Parameters:     num_rows (in, Test printing a normal Pascal's triangle., Test printing an empty Pascal's triangle., Test generating a valid Pascal's triangle., Test generating an invalid Pascal's triangle with negative rows. (+7 more)

### Community 15 - "Trigonometric Tangent Functions"
Cohesion: 0.11
Nodes (9): compute_polynomial_derivative_str(), Compute the derivative of a polynomial and return as string.      Parameters:, test_compute_polynomial_derivative_str_constant_term(), test_compute_polynomial_derivative_str_empty(), test_compute_polynomial_derivative_str_mixed_terms(), test_compute_polynomial_derivative_str_multiple_terms(), test_compute_polynomial_derivative_str_negative_powers_and_floats(), test_compute_polynomial_derivative_str_single_term() (+1 more)

### Community 16 - "Remainder Theorem Algebra"
Cohesion: 0.08
Nodes (13): Test with a simple quadratic polynomial: P(x) = x^2 + 2x + 1 at x=2, Test polynomial at x=0, Test polynomial at x=-1, Test with fractional powers, Test with float coefficients and float x, Test with empty coefficients and powers, Test with negative powers, Test dividing by zero raises an exception when power is negative (+5 more)

### Community 17 - "Test Quadratic Testsolvequadratic Module"
Cohesion: 0.15
Nodes (10): Return the real roots of ax² + bx + c = 0.      Parameters:     a (Union[int, fl, solve_quadratic(), Test with an equation that has two distinct real roots: x^2 - 3x + 2 = 0, Test with an equation that has one repeated real root: x^2 - 4x + 4 = 0, Test with an equation that has no real roots: x^2 + x + 1 = 0, Test that a=0 raises ValueError, Test with float coefficients: 0.5x^2 - 1.5x + 1 = 0, Test with b=0: x^2 - 4 = 0 (+2 more)

### Community 18 - "Factorial Discrete Module"
Cohesion: 0.13
Nodes (20): factorial(), Calculate the factorial of a number.      Parameters:     n (int): The number to, test_factorial(), Test that factorial of 0 is 1., Test that factorial of 1 is 1., Test factorial calculation for positive integers., Test factorial calculation for a slightly larger number., Test factorial with a negative number, which should raise RecursionError due to (+12 more)

### Community 19 - "Greatest Common Divisor (GCD)"
Cohesion: 0.19
Nodes (24): _compute_base_u(), _compute_branch_roots(), _compute_invariants(), _compute_residual_error(), quartic_formula(), Calculate residual sum of absolute evaluation errors for candidate roots.      P, Solve quartic equations of the form ax⁴ + bx³ + cx² + dx + e = 0     using Lande, Compute the base core cube-root term U before branch selection.      Parameters: (+16 more)

### Community 20 - "Calculus Chain Rule"
Cohesion: 0.10
Nodes (17): chain_rule_derivative(), Apply the chain rule to find the derivative of [g(x)]^n.      Parameters:     in, test_chain_rule_derivative_basic(), test_chain_rule_derivative_constant_inner(), test_chain_rule_derivative_empty(), test_chain_rule_derivative_empty_inner(), test_chain_rule_derivative_exponent_one(), test_chain_rule_derivative_float_coefficients() (+9 more)

### Community 21 - "Least Common Multiple (LCM)"
Cohesion: 0.14
Nodes (14): compute_gcd(), Compute the Greatest Common Divisor (GCD) of two numbers using the Euclidean alg, compute_lcm(), Compute the Least Common Multiple (LCM) of two numbers.      Parameters:     a (, Test compute_gcd against Python's built-in math.gcd with a wide range     of ran, test_compute_gcd_against_math_gcd(), test_compute_gcd_common_factors(), test_compute_gcd_coprime() (+6 more)

### Community 22 - "Descriptive Statistics (Mode)"
Cohesion: 0.08
Nodes (19): mode(), Calculate the mode of a list of numbers.      Parameters:     data (List[Union[i, Test mode with a single element list., Test mode with a single mode., Test mode with multiple modes., Test mode when all elements have the same frequency., Test mode with float values., Test mode with negative numbers. (+11 more)

### Community 23 - "Descriptive Statistics (Mean)"
Cohesion: 0.24
Nodes (3): mean(), Calculate the mean (average) of a list of numbers.      Parameters:     data (Li, TestMean

### Community 24 - "Calculus Chain Rule"
Cohesion: 0.07
Nodes (35): Calculate the second derivative of a polynomial.      Parameters:     coeffs (Li, second_derivative(), compute_polynomial_derivative(), Compute the derivative of a polynomial.      Parameters:     coefficients (List[, TestComputePolynomialDerivative, test_basic_polynomial(), test_empty_inputs(), test_fractional_and_float_inputs() (+27 more)

### Community 25 - "Partition Test Discretetest Module"
Cohesion: 0.17
Nodes (15): binomial_general_term(), Calculate the general term in the binomial expansion of (a + b)^n.      Paramete, partition_approximation(), Calculate an approximation of the number of partitions p(n) using Ramanujan's fo, Test edge cases for partition approximation., Test small values to ensure the formula computes successfully., Test larger values to ensure the formula produces expected output., Test that the approximation improves relative to the exact partition function. (+7 more)

### Community 26 - "Trigonometric Tangent Functions"
Cohesion: 0.10
Nodes (11): Test integral of sin(x) from -pi/2 to 0 = -1, Test integral of sin(x) from a to a = 0, Test integral of sin(x) from pi to 0 = -2, Test integral of sin(x) from 0 to pi/3 = 0.5, Test integral of sin(x) from 0.5 to 1.5, Test integral of cos(x) from 0 to pi/2 = 1, Test integral of cos(x) from -pi/2 to 0 = 1, Test integral of cos(x) from a to a = 0 (+3 more)

### Community 27 - "Binomial Theorem"
Cohesion: 0.43
Nodes (6): prime_factorization(), Find the prime factorization of a number.      Parameters:     number (int): The, test_prime_factorization_composite_numbers(), test_prime_factorization_edge_case(), test_prime_factorization_invalid_input(), test_prime_factorization_prime_numbers()

### Community 28 - "Test Slope Testcalculateslope Module"
Cohesion: 0.27
Nodes (3): calculate_slope(), Calculate the slope of the line connecting two points.      Parameters:     x1 (, TestCalculateSlope

### Community 29 - "Euclidean Area (Triangle)"
Cohesion: 0.27
Nodes (3): area_of_triangle(), Calculate the area of a triangle given its base and height.      Parameters:, TestAreaOfTriangle

### Community 30 - "Euclidean Volume (Cone)"
Cohesion: 0.07
Nodes (14): n_permute_r(), Calculate permutations (nPr) using the formula: nPr = n! / (n - r)!.      Parame, area_of_circle(), Calculate the area of a circle given its radius.      Parameters:     radius (Un, Calculate the volume of a cone given its radius and height.      Parameters:, volume_of_cone(), Calculate the volume of a cylinder given its radius and height.      Parameters:, volume_of_cylinder() (+6 more)

### Community 31 - "Euclidean Volume (Cylinder)"
Cohesion: 0.12
Nodes (22): linear_eqn(), Calculate the equation of a line given two points (x1, y1) and (x2, y2)., test_linear_eqn_all_negative(), test_linear_eqn_floats(), test_linear_eqn_fractional_slope(), test_linear_eqn_identical_points(), test_linear_eqn_large_coordinates(), test_linear_eqn_negative_slope() (+14 more)

### Community 32 - "Calculus Quotient Rule"
Cohesion: 0.06
Nodes (11): product_rule_derivative(), Apply the product rule to find the derivative of u(x) * v(x).      Parameters:, format_polynomial(), Format a polynomial as a string.      Parameters:     coefficients (List[Union[i, test_format_polynomial_basic(), test_format_polynomial_empty(), test_format_polynomial_floats(), test_format_polynomial_negative_powers_and_coeffs() (+3 more)

### Community 33 - "Simple Interest Math"
Cohesion: 0.36
Nodes (8): Calculate the total amount after applying simple interest.      Parameters:, simple_interest(), test_simple_interest_basic(), test_simple_interest_floats(), test_simple_interest_negative_principal(), test_simple_interest_negative_rate(), test_simple_interest_negative_time(), test_simple_interest_zero_values()

### Community 34 - "Integration Format Module"
Cohesion: 0.13
Nodes (8): Test with a simple quadratic polynomial: x^2 + 2x + 1 at x=2, Test polynomial at x=0, Test polynomial at x=-1, Test with fractional powers (square root), Test with float coefficients and float x, Test with empty coefficients and powers, Test with negative powers, TestEvaluatePolynomial

### Community 35 - "Euclidean Area (Rectangle)"
Cohesion: 0.29
Nodes (3): area_of_rectangle(), Calculate the area of a rectangle given its length and width.      Parameters:, TestAreaOfRectangle

### Community 36 - "Euclidean Volume (Sphere)"
Cohesion: 0.22
Nodes (7): Calculate the volume of a sphere given its radius.      Parameters:     radius (, volume_of_sphere(), Test volume with zero radius., Test volume with a positive integer radius., Test volume with a positive float radius., Test that negative radius raises ValueError., TestVolumeOfSphere

### Community 37 - "Descriptive Statistics (Median)"
Cohesion: 0.29
Nodes (3): median(), Calculate the median of a list of numbers.      Parameters:     data (List[Union, TestMedian

### Community 39 - "Integrate Polynomial Module"
Cohesion: 0.16
Nodes (21): format_polynomial_integration(), integrate_polynomial(), Format an integrated polynomial as a string.      Parameters:     coefficients (, Integrate a polynomial term by term.      Parameters:     coefficients (List[Uni, test_format_polynomial_integration_basic(), test_format_polynomial_integration_empty(), test_format_polynomial_integration_multiple_terms(), test_format_polynomial_integration_negative_coefficients() (+13 more)

### Community 40 - "Trigonometric Integration"
Cohesion: 0.20
Nodes (9): integrate_sin(), Calculate the definite integral of sin(x) from a to b.      Parameters:     a (U, cosine(), Calculate the cosine of an angle using Taylor series expansion.      Parameters:, test_cosine_large_angles(), test_cosine_negative_angles(), test_cosine_standard_angles(), Test integral of sin(x) from 0 to 2*pi = 0 (+1 more)

### Community 41 - "Approximation Partition Module"
Cohesion: 0.26
Nodes (10): partition(), Calculate the number of partitions of a positive integer n.      Parameters:, test_partition_negative(), test_partition_positive(), test_partition_zero(), test_partition_exceeds_upper_bound(), test_partition_invalid_type(), test_partition_negative() (+2 more)

### Community 42 - "Trigonometric Tangent Functions"
Cohesion: 0.31
Nodes (3): distance_formula(), Calculate the distance between two points (x1, y1) and (x2, y2) using the distan, TestDistanceFormula

### Community 43 - "Test Intersection Intersection Module"
Cohesion: 0.31
Nodes (3): find_intersection(), Find the intersection point of two lines given their equations in the form y = m, TestFindIntersection

### Community 44 - "From Points Module"
Cohesion: 0.31
Nodes (3): line_from_points(), Return the equation of the line passing through two points in slope-intercept fo, TestLineFromPoints

### Community 45 - "Test Midpoint Testmidpointformula Module"
Cohesion: 0.31
Nodes (3): midpoint_formula(), Calculate the midpoint of a line segment in a 2D plane.      Parameters:     x1, TestMidpointFormula

### Community 47 - "Euclidean Area (Circle)"
Cohesion: 0.18
Nodes (19): arccos_series(), cosine_rule_for_angle(), cosine_rule_for_side(), Calculate arccos using series approximation.      Parameters:     x (Union[int,, Calculate the length of side c using the cosine rule: c² = a² + b² - 2ab×cos(C)., Calculate angle C using the cosine rule: cos(C) = (a² + b² - c²) / (2ab).      P, Calculate square root using Newton's method.      Parameters:     x (Union[int,, sqrt_newton() (+11 more)

### Community 48 - "Euclidean Area (Square)"
Cohesion: 0.33
Nodes (3): area_of_square(), Calculate the area of a square given the length of its side.      Parameters:, TestAreaOfSquare

### Community 49 - "Euclidean Area (Square)"
Cohesion: 0.33
Nodes (3): pythagorean_theorem(), Calculate the length of the hypotenuse of a right triangle using the Pythagorean, TestPythagoreanTheorem

### Community 50 - "Euclidean Volume (Cuboid)"
Cohesion: 0.33
Nodes (3): Calculate the volume of a cuboid given its length, width, and height.      Param, volume_of_cuboid(), TestVolumeOfCuboid

### Community 51 - "Inverse Trigonometry (Arctan)"
Cohesion: 0.08
Nodes (17): calculate_arctan(), Decimal, Calculate the arctangent of (1/x) in radians with specified precision using Tayl, calculate_arctan_series(), calculate_pi_machin(), Decimal, Calculate Pi using Machin's formula: π/4 = 4×arctan(1/5) - arctan(1/239).      P, Calculate arctan(1/x) using Taylor series expansion.      Parameters:     x (int (+9 more)

### Community 53 - "Trigonometric Tangent Functions"
Cohesion: 0.18
Nodes (9): calculate_pi_nilakantha(), Decimal, Calculate Pi using Nilakantha's algorithm.          Formula: π = 3 + 4/(2×3×4) -, Test with small number of terms to check exact values, Test that the algorithm converges towards math.pi as terms increase, Test the precision parameter, Test that invalid number of terms raises ValueError, Test that invalid precision raises ValueError (+1 more)

### Community 54 - "Compound Interest Math"
Cohesion: 0.33
Nodes (9): compound_interest(), Calculate the total amount after applying compound interest.      Parameters:, test_compound_interest_float_inputs(), test_compound_interest_invalid_frequency(), test_compound_interest_negative_principal(), test_compound_interest_negative_rate(), test_compound_interest_negative_time(), test_compound_interest_regular_intervals() (+1 more)

### Community 55 - "Trinomial General Module"
Cohesion: 0.15
Nodes (11): calculate_pi_ramanujan(), Decimal, Calculate Pi using S. Ramanujan's formula.          Formula: 1/π = (2√2/9801) ×, Test suite for calculate_pi_ramanujan function., Test default arguments (num_decimal_places=50, num_terms=10)., Test calculation with high precision., Test that adding terms improves accuracy of the approximation., Test boundary conditions for num_decimal_places. (+3 more)

### Community 56 - "Euclidean Area (Triangle)"
Cohesion: 0.26
Nodes (3): herons_area_of_triangle(), Calculate the area of a triangle using Heron's formula.      Parameters:     a (, TestHeronsAreaOfTriangle

### Community 58 - "Trigonometric Sine Functions"
Cohesion: 0.40
Nodes (4): 1. Codebase Audit & Roadmap Alignment, 2. Test Verification Requirement, 3. Sandboxed Git Remote Operations (Fetch / Pull / Push), Repository Sync & Sandbox Git Workflow

### Community 60 - "Inverse Trigonometry (Arctan)"
Cohesion: 0.48
Nodes (5): Calculate the sine of an angle using Taylor series expansion.      Parameters:, sine(), test_sine_large_angles(), test_sine_negative_angles(), test_sine_standard_angles()

### Community 64 - "Trigonometric Tangent Functions"
Cohesion: 0.21
Nodes (8): calculate_pi_chudnovsky(), Decimal, Calculate Pi using the Chudnovsky algorithm.          This is one of the fastest, Test that the function returns a Decimal object., Test against the first 50 known digits of Pi to verify arbitrary precision., Test that invalid precision values raise ValueError., Test that the algorithm returns a value very close to math.pi., TestChudnovskyAlgorithm

### Community 66 - "Trigonometric Tangent Functions"
Cohesion: 0.67
Nodes (3): Internal Imports First Principle, No Standard Math Module Rule, Number One Principle

### Community 68 - "Geometry Volume Module"
Cohesion: 0.14
Nodes (11): Calculate the volume of a prism given its base area and height.      Parameters:, volume_of_prism(), Test volume with zero height., Test volume with both zero., Test volume with positive integer base area and height., Test volume with positive float base area and height., Test that negative base area raises ValueError., Test that negative height raises ValueError. (+3 more)

## Knowledge Gaps
- **12 isolated node(s):** `Polynomial Closed-Form Solvers Skill`, `1. Codebase Audit & Roadmap Alignment`, `2. Test Verification Requirement`, `3. Sandboxed Git Remote Operations (Fetch / Pull / Push)`, `linear_eqn (Example Template)` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TestFormatPolynomialChainRule` connect `Test Calculus Testformatpolynomialchainrule Module` to `Differentiation Chain & Second Derivative Rules`, `Trigonometric Integration`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Why does `nCr()` connect `Binomial Theorem` to `Partition Test Discretetest Module`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `integrate_cos()` connect `Trigonometric Integration` to `Trigonometric Integration`, `Test Calculus Testformatpolynomialchainrule Module`, `Trigonometric Tangent Functions`, `Inverse Trigonometry (Arctan)`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **What connects `Polynomial Closed-Form Solvers Skill`, `1. Codebase Audit & Roadmap Alignment`, `2. Test Verification Requirement` to the rest of the system?**
  _12 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Newton-Raphson & Root Finding` be split into smaller, more focused modules?**
  _Cohesion score 0.08585858585858586 - nodes in this community are weakly interconnected._
- **Should `Binomial Theorem` be split into smaller, more focused modules?**
  _Cohesion score 0.056051587301587304 - nodes in this community are weakly interconnected._
- **Should `Differentiation Chain & Second Derivative Rules` be split into smaller, more focused modules?**
  _Cohesion score 0.06896551724137931 - nodes in this community are weakly interconnected._