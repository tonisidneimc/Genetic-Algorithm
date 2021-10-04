# Genetic-Algorithm
A practical application of Genetic Algorithms to optimize functions.

<img src="./img/f6.png">
<p align="right">
    <i>Schaffer's F6</i>
</p>

## How-to

Consider the following function:

<p align="center">
    <img src="./img/CodeCogsEqn.png" style="width: 50%;">
</p>

<p align="center">
    <img src="./img/CodeCogsEqn2.png" style="width: 30%;">
</p>

In this case, each chromosome will have a 44-bit word, with **k_i** = 22 bits to each variable of the problem. The function to convert this representation to a real number is:

<p align="center">
    <img src="./img/CodeCogsEqn3.png">
</p>

where:

<p align="center">
    <img src="./img/min_i.png">
</p>

<p align="center">
    <img src="./img/max_i.png">
</p>

With that, we define the parameters for the algorithm (F6 as the fitness function, a fixed mutation and crossover rates, a fixed population size), and follows these steps: 

<p align="center">
    <img src="./img/gfig11.gif" style="width:70%;">
</p>

Where the termination criterion is a fixed number of generations.

## Running

```shell
$ git clone https://github.com/tonisidneimc/Genetic-Algorithm/
$ cd Genetic-Algorithm
$ make
```

### Output

![output](./img/1.png)

It may vary due to randomness in the evolution process, but running the algorithm a few more times or with higher mutation rates or higher number of generations may converge better.
