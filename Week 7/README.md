# Problem

To re-iterate the problem, we are attempting to solve the 1-dimensional heat
equation over a given finite domain (heat diffusion through a rod in this
case.) The heat equation is given as
$$
\frac{\partial u}{\partial t}
= \frac{k}{c_p \rho} \frac{\partial^2 u}{\partial x^2}
$$
where
$$
\alpha = \frac{k}{c_p\rho}
$$
is generally referred to the **diffusivity constant**. Note that your lectures
may use the symbol $c^2$ in place of $\alpha$.

# Workings

## Update Scheme

$$
u^{t+1}_{i} \approx \Delta t c^2 \frac{\partial^2 u}{\partial x^2} + u^t_i
$$

$$
\frac{\partial^2 u}{\partial x^2} \approx \frac{u^t_{i+1} - 2u^t_i + 2u^t_{i-1}}{\Delta x^2}
$$

## Boundary Nodes (Neumann)

$$
\left.\frac{\partial u}{\partial x}\right|_\text{boundary} = 0
$$

### For left boundary node (i=0):

$$
\left.\frac{\partial u}{\partial x}\right|_\text{n=0} \approx
\frac{-u^t_2 + 4u^t_1 - 3u^t_0}{\Delta x} = 0
$$

$$
u^t_0 = \frac{4u^t_1 - u_2}{3}
$$

## Courant Number

$$
\sigma = c^2 \frac{\Delta t}{\Delta x^2} \leq 0.5
$$