# Problem

To re-iterate the problem, we are attempting to solve the 1-dimensional heat
equation over a given finite domain (heat diffusion through a rod in this
case.) The heat equation is given as
<!-- $$
\large
\dfrac{\partial u}{\partial t}
= \dfrac{k}{c_p \rho} \dfrac{\partial^2 u}{\partial x^2} + \dfrac{k}{c_p \rho} \dfrac{\partial^2 u}{\partial y^2}
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A%5Cdfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20t%7D%0D%0A%3D%20%5Cdfrac%7Bk%7D%7Bc_p%20%5Crho%7D%20%5Cdfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20x%5E2%7D%20%2B%20%5Cdfrac%7Bk%7D%7Bc_p%20%5Crho%7D%20%5Cdfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20y%5E2%7D%0D"></div>

where
<!-- $$
\large
\alpha = \dfrac{k}{c_p\rho}
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A%5Calpha%20%3D%20%5Cdfrac%7Bk%7D%7Bc_p%5Crho%7D%0D"></div>

is generally referred to the **diffusivity constant**. Note that your lectures
may use the symbol <!-- $c^2$ --> <img src="https://render.githubusercontent.com/render/math?math=c%5E2"> in place of <!-- $\alpha$ --> <img src="https://render.githubusercontent.com/render/math?math=%5Calpha">.

# Workings

## Update Scheme

<!-- $$
\large
u^t_{i} \approx \Delta t c^2 \dfrac{\partial^2 u_i^t}{\partial x^2} + u^{t-1}_i
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0Au%5Et_%7Bi%7D%20%5Capprox%20%5CDelta%20t%20c%5E2%20%5Cdfrac%7B%5Cpartial%5E2%20u_i%5Et%7D%7B%5Cpartial%20x%5E2%7D%20%2B%20u%5E%7Bt-1%7D_i%0D"></div>

<!-- $$
\large
\dfrac{\partial^2 u}{\partial x^2} \approx \dfrac{u^t_{i+1} - 2u^t_i + u^t_{i-1}}{\Delta x^2}
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A%5Cdfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20x%5E2%7D%20%5Capprox%20%5Cdfrac%7Bu%5Et_%7Bi%2B1%7D%20-%202u%5Et_i%20%2B%20u%5Et_%7Bi-1%7D%7D%7B%5CDelta%20x%5E2%7D%0D"></div>

<!-- $$
\large
\dfrac{\partial^2 u}{\partial y^2} \approx \dfrac{u^t_{i+n} - 2u^t_i + u^t_{i-n}}{\Delta x^2}
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A%5Cdfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20y%5E2%7D%20%5Capprox%20%5Cdfrac%7Bu%5Et_%7Bi%2Bn%7D%20-%202u%5Et_i%20%2B%20u%5Et_%7Bi-n%7D%7D%7B%5CDelta%20x%5E2%7D%0D"></div>

where <!-- $n$ --> <img src="https://render.githubusercontent.com/render/math?math=n"> is the width of the domain

<!-- $$
\large
u^t_{i} - \sigma_x (u^t_{i+1} - 2u^t_i + u^t_{i-1}) - \sigma_y (u^t_{i+n} - 2u^t_i + u^t_{i-n}) \approx u^{t-1}_i
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0Au%5Et_%7Bi%7D%20-%20%5Csigma_x%20(u%5Et_%7Bi%2B1%7D%20-%202u%5Et_i%20%2B%20u%5Et_%7Bi-1%7D)%20-%20%5Csigma_y%20(u%5Et_%7Bi%2Bn%7D%20-%202u%5Et_i%20%2B%20u%5Et_%7Bi-n%7D)%20%5Capprox%20u%5E%7Bt-1%7D_i%0D"></div>

<!-- $$
\large
(1+2\sigma_x+2\sigma_y)u^t_{i} - \sigma_x (u^t_{i+1} + u^t_{i-1}) - \sigma_y (u^t_{i+n} + u^t_{i-n}) \approx u^{t-1}_i
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A(1%2B2%5Csigma_x%2B2%5Csigma_y)u%5Et_%7Bi%7D%20-%20%5Csigma_x%20(u%5Et_%7Bi%2B1%7D%20%2B%20u%5Et_%7Bi-1%7D)%20-%20%5Csigma_y%20(u%5Et_%7Bi%2Bn%7D%20%2B%20u%5Et_%7Bi-n%7D)%20%5Capprox%20u%5E%7Bt-1%7D_i%0D"></div>

<!-- $$
\large
A \vec{u}^{t} = \vec{u}^{t-1}
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0AA%20%5Cvec%7Bu%7D%5E%7Bt%7D%20%3D%20%5Cvec%7Bu%7D%5E%7Bt-1%7D%0D"></div>

## Boundary Nodes (Neumann)

<!-- $$
\large
\left.\dfrac{\partial u}{\partial x}\right|_\text{boundary} = 0
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A%5Cleft.%5Cdfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20x%7D%5Cright%7C_%5Ctext%7Bboundary%7D%20%3D%200%0D"></div>

### For left boundary node (i=0):

<!-- $$
\large
\left.\dfrac{\partial u}{\partial x}\right|_\text{n=0} \approx
\dfrac{-u^t_2 + 4u^t_1 - 3u^t_0}{\Delta x} = 0
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A%5Cleft.%5Cdfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20x%7D%5Cright%7C_%5Ctext%7Bn%3D0%7D%20%5Capprox%0D%0A%5Cdfrac%7B-u%5Et_2%20%2B%204u%5Et_1%20-%203u%5Et_0%7D%7B%5CDelta%20x%7D%20%3D%200%0D"></div>

<!-- $$
\large
u^t_0 = \dfrac{4u^t_1 - u_2}{3}
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0Au%5Et_0%20%3D%20%5Cdfrac%7B4u%5Et_1%20-%20u_2%7D%7B3%7D%0D"></div>

## Courant Number

<!-- $$
\large
\sigma_x = c^2 \dfrac{\Delta t}{\Delta x^2} \leq 0.5
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A%5Csigma_x%20%3D%20c%5E2%20%5Cdfrac%7B%5CDelta%20t%7D%7B%5CDelta%20x%5E2%7D%20%5Cleq%200.5%0D"></div>

<!-- $$
\large
\sigma_x = c^2 \dfrac{\Delta t}{\Delta y^2} \leq 0.5
$$ -->

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Clarge%0D%0A%5Csigma_x%20%3D%20c%5E2%20%5Cdfrac%7B%5CDelta%20t%7D%7B%5CDelta%20y%5E2%7D%20%5Cleq%200.5%0D"></div>