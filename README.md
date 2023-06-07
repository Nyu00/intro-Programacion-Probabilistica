# intro-Programacion-Probabilistica

![Texto alternativo](./src/IPP-img.jpg)

La programación probabilística a día de hoy tiene muchos usos, investigación científica, medicina, etc

Una de las grandes diferencias que existen entre la programación probabilística, es que la programacion probabilistica utilizamos modelos probabilisticos

- [Modelos probabilisticos](#)
    - [Regresión lineal bayesiana](#)
    - [Redes Bayesianas](#)
    - [Teorema de Bayes](#)
    - [Modelos ocultos de Markov HMM](#)
    - [Procesos de Dirichlet](#)


Este tipo de programacion es tan importante que  existen lenguajes especificos para programas de este tipo de indole al igual que librerias

- [Lenguajes probabilisticos](#)
    - [Stan](#)
    - [Pyro](#)
    - [Church](#)
    - [Anglican](#)
    - [WeebPPL](#)

Uno de los mejores ejemplo que podemos usar para desarrolar nuestro pensamiento probabilistico es:

## Juan el Musico

Juan es un musico que le gusta desvelarse, el rock and rol, el heavy metal, y esta de parranda de lunes a sabado

Ahora, si te preguntaran hipoteticamente que es mas probable, ¿Que es mas probable que Juan sea un musico, o que sea musico y use drogas?

-----------------------------------------

La mayoria de las personas hubieran dicho que Juan es musico y ademas usa drogas.

Pero algo que tenemos que empezar a entender es que cuando utilizamos la palabra [y](#) hace que la probabilidad de que eso cierto, siempre será menor

![Probabilidad de ser Muisco y usar drogas](./src/musico-drogas.jpg)

En este ejemplo tenemos visualmente mostrando en un circulo azul TODOS los musicos y en un circulo verde los musicos que usan drogas

![Probabilidad de ser Muisco y usar drogas y ademas jugar pokemon](./src/musico-drogas-pokemon.jpg)

Ahora en ese ejemplo se muestra las personas que ademas de ser musicos y usar drogas tambien juegan pokemon

Un punto muy importante a tener en cuenta es que cada vez que le agregagos una condicional a algo siempre resa menor o menos probable