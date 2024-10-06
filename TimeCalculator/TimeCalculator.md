
# Time Calculator

Write a function named `add_time` that takes in two required parameters and one optional parameter:

- A start time in the 12-hour clock format (ending in AM or PM).
- A duration time that indicates the number of hours and minutes.
- (Optional) A starting day of the week, case insensitive.

The function should add the duration time to the start time and return the result.

## Requirements

- If the result will be the next day, it should show **(next day)** after the time.
- If the result will be more than one day later, it should show **(n days later)** after the time, where "n" is the number of days later.
- If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

## Examples

**Function Call:**

```python
add_time('3:00 PM', '3:10')
```

**Returns:**  
```plaintext
6:10 PM
```

**Function Call:**

```python
add_time('11:30 AM', '2:32', 'Monday')
```

**Returns:**  
```plaintext
2:02 PM, Monday
```

**Function Call:**

```python
add_time('11:43 AM', '00:20')
```

**Returns:**  
```plaintext
12:03 PM
```

**Function Call:**

```python
add_time('10:10 PM', '3:30')
```

**Returns:**  
```plaintext
1:40 AM (next day)
```

**Function Call:**

```python
add_time('11:43 PM', '24:20', 'tueSday')
```

**Returns:**  
```plaintext
12:03 AM, Thursday (2 days later)
```

**Function Call:**

```python
add_time('6:30 PM', '205:12')
```

**Returns:**  
```plaintext
7:42 AM (9 days later)
```

## Assumptions

- Do not import any Python libraries.
- Assume that the start times are valid times.
- The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
