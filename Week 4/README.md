# Solution

This week's problems are mainly related to plotting the Fourier series
approximations of given functions. As this numerical method is already
implemented with `scipy.fft` (see
https://docs.scipy.org/doc/scipy/reference/fft.html), there's not much to teach
in regards to that.

So, this week the code focuses on:
1. **How to customise plots to be more readable.** In this case, we've changed
   the x-axis to be in terms of `\pi`, which is more suitable to trigonometric
   functions. Have a go at changing it to show fractions of `\pi`!

   The `FuncFormatter` from `matplotlib.ticker` can be used in many other ways,
   to customise how the numbers on your display are formatted.
   ```python
   ax.xaxis.set_major_formatter(FuncFormatter(
        lambda val, _: f'{val/np.pi:.0g}$\pi$' if val else '0'
                        # +------------      # +--------------
                        # |                  # |
                        # |                  # Use the format if the value
                        # |                  # is non-zero, otherwise just
                        # |                  # put '0'
                        # |
                        # |
                        # Divide the value by pi, and then round to an integer
                        # (equivalent to showing zero decimals with .0g)
   ))
   ```


2. **How to use default values and if statements.** While it may be overkill
   for this task, the `approx` function demonstrates how you can use the inline
   `if` statement to switch out different values within computation. This can
   make it a lot easier for you to reuse code within functions.

   The best example of this is the `parity` variable. Note how we can switch
   between `sin` and `cos` functions with to allow us to approximate simple odd
   **and** even functions.
   ```python
   trig = np.cos if parity == 'even' else np.sin
   ```
