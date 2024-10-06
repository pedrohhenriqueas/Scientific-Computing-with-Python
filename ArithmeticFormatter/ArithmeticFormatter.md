
# Arithmetic Formatter

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

```plaintext
  235
+  52
-----
```

## Function Description

Finish the `arithmetic_arranger` function that receives a list of strings representing arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.

### Example

**Function Call:**

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

**Output:**

```plaintext
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

**Function Call:**

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

**Output:**

```plaintext
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Rules

The function will return the correct conversion if the supplied problems are properly formatted. Otherwise, it will return a string that describes an error that is meaningful to the user.

### Situations that will return an error:

1. If there are too many problems supplied to the function. The limit is five, anything more will return:  
   **`Error: Too many problems.`**

2. The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. The error returned will be:  
   **`Error: Operator must be '+' or '-'.`**

3. Each number (operand) should only contain digits. Otherwise, the function will return:  
   **`Error: Numbers must only contain digits.`**

4. Each operand (number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:  
   **`Error: Numbers cannot be more than four digits.`**

### Formatting Rules:

- There should be a single space between the operator and the longest of the two operands.
- The operator will be on the same line as the second operand, with both operands in the same order as provided (the first will be the top one, and the second will be the bottom).
- Numbers should be right-aligned.
- There should be four spaces between each problem.
- There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.
