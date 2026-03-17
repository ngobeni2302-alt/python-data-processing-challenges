# python-data-processing-challenges
# Data Processing Practice

## Overview
This project contains practice problems to help you improve your understanding of:

- Lists
- Dictionaries
- Sets
- Data transformation

You are required to complete the functions in `functions.py`.

---

# Requirements

- Python 3.x

---

# How to Run the Code

```bash
python functions.py
```

---

# Running Unit Tests

### Run all tests

```bash
python -m unittest test_functions.py
```

### Run a single test class

```bash
python -m unittest test_functions.TestFunctions
```

### Run a single test

```bash
python -m unittest test_functions.TestFunctions.test_separate_scores
```

---

# Files

- `functions.py` → You must complete these functions
- `test_functions.py` → Contains unit tests

---

# Questions

---

## Question 1A

Function name:
separate_scores(scores)

This function receives a list of tuples containing (math_score, science_score).  
It must return two separate lists.

### Input

```python
[(70, 80), (60, 90)]
```

### Expected Output

```python
([70, 60], [80, 90])
```

---

## Question 1B

Function name:
split_coordinates(coords)

This function receives a list of (x, y) coordinates.  
It must return two lists: x-values and y-values.

### Input

```python
[(1, 2), (3, 4)]
```

### Expected Output

```python
([1, 3], [2, 4])
```

---

## Question 2A

Function name:
build_student_index(students)

This function receives a list of student names.  
It must return a dictionary mapping names to their index.

### Input

```python
["Alice", "Bob"]
```

### Expected Output

```python
{"Alice": 0, "Bob": 1}
```

---

## Question 2B

Function name:
map_items_to_position(items)

This function receives a list of items.  
It must return a dictionary mapping each item to its position.

### Input

```python
["x", "y"]
```

### Expected Output

```python
{"x": 0, "y": 1}
```

---

## Question 3A

Function name:
normalize_tags(tags)

This function receives a list of strings.  
It must return a set of lowercase unique values.

### Input

```python
["PYTHON", "python"]
```

### Expected Output

```python
{"python"}
```

---

## Question 3B

Function name:
clean_usernames(usernames)

This function receives a list of usernames.  
It must return lowercase usernames without duplicates.

### Input

```python
["Admin", "admin"]
```

### Expected Output

```python
{"admin"}
```

---

## Question 4A

Function name:
group_by_city(people)

This function receives a list of dictionaries with name and city.  
It must group names by city.

### Input

```python
[
    {"name": "Alice", "city": "Cape Town"},
    {"name": "Bob", "city": "Cape Town"}
]
```

### Expected Output

```python
{
    "Cape Town": ["Alice", "Bob"]
}
```

---

## Question 4B

Function name:
categorize_books(books)

This function receives a list of dictionaries with title and genre.  
It must group titles by genre.

### Input

```python
[
    {"title": "Book1", "genre": "Fiction"},
    {"title": "Book2", "genre": "Fiction"}
]
```

### Expected Output

```python
{
    "Fiction": ["Book1", "Book2"]
}
```

---

# Rules

- Do not change function names
- Handle empty inputs
- All tests must pass

---

# Goal

By completing this project, you will learn:

- List iteration
- Dictionary creation
- Set usage
- Data transformation
