# intro-Programacion-Probabilistica

<p align="center">
  <img src="./src/IPP-img.jpg" alt="Probabilistic Programming">
</p>

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

<img src="./src/musico-drogas.jpg" alt="Probabilidad de ser Muisco y usar drogas" style="width: 300px; height: auto;">

En este ejemplo tenemos visualmente mostrando en un circulo azul TODOS los musicos y en un circulo verde los musicos que usan drogas

<img src="./src/musico-drogas-pokemon.jpg" alt="Probabilidad de ser Muisco y usar drogas y ademas jugar pokemon" style="width: 300px; height: auto;">

Ahora en ese ejemplo se muestra las personas que ademas de ser musicos y usar drogas tambien juegan pokemon

Un punto muy importante a tener en cuenta es que cada vez que le agregagos una condicional a algo siempre resa menor o menos probable

# Clase 2

En esta clase hablaremos sobre la probabilidad condicional, Pero antes de continuar necesitamos entender un par de cosas

Calcular la probabilidad de un evento no es nada mas que la cantidad de veces que ocurre un evento dividido por la cantidad de enventos posibles

<img src="./src/calc-probabilidad.jpg" alt="DEventosx" style="width: 300px; height: auto;">


Esto nos sirve para un tipo de probabilidad muy especifica como la que hay en los jugos de azar o lanzar una moneda al aire, esta se llama [Probabilidad independiente](#)  osea que los eventos nos estan relacionados unos con los otros

Asi es es la formula de probailidad independienente de lazar una moneda y qe salgan dos cruzes

<img src="./src/eventos-independientes.jpg" alt="Eventos independientes" style="width: 400px; height: auto;">


Lo malo es que no suelen llegar a ser muy utiles

Por eso utilizamos la [Probabilidad condicional](#)

Formula para resolver probabilidades condicionales es:

<img src="./src/Formula-condiconal.jpg" alt="Formula condicional" style="width: 400px; height: auto;">

Con el ejemplo de Juan se puede demostrar como :

<img src="./src/Formula-juan.jpg" alt="Formula condicional Juan" style="width: 500px; height: auto;">

Esta formula se leeria como :

La probabilidad de que Juan use Drogas es igual a la probabilidad de que sea musico multiplicado por la probabilidad de use drogas dado que es musico mas la probabilida de que no sea musico multiplicado por la probabilidad que use drogas dado que no es musico

Esta tipo de prbabilidad es utilizada unicamente cuando un evento depende de otro evento

## Clase 3

