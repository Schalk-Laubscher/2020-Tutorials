# Solutions

Two sets of solutions are provided to the Week 1 ICT exercises. The
[beginner](beginner.py) file demonstrates the solution a naive engineer would
be expected to program. This is the level we hope you retain from MECH2700.

The [advanced](advanced.py) file demonstrates how you could program a solution
using improved programming techniques, with a goal of maintainable and
explainable code.

Note the use of:
- For loops to iterate over a group of items (in this case functions)
- Functions to allow for code to be separated
- Comments describing _what_ is done, not _how_

Some more _subtle_ Python features used are:
- Function doc-strings, created by the triple quotation marks (`"""`)
- `f` strings, used to **format** values in string
  - Text within the `{}` braces is executed as Python code (i.e. variables)
  - Text after the `:` is used to specify formatting. For example, `:.2e`
    specifies `e`xponential format, with `2` decimal places.
- Use of the `if __name__ == __main__` to separate functions / definitions from
  the specific script to be run.
  - Code within this `if` statement will **not** be run if you import the file
    into another Python program. This is useful when you want to re-use a file
    from a previous project.