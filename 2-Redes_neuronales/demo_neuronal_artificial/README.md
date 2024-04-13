# Demo neurona artificial

Esta demo está tomada de [How to build a simple neural network in 9 lines of Python code](https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1). En el programa se entrena un única neurona artificial que tiene tres conexiones de entrada y una de salida. La neurona utiliza la función de activación sigmoide.

La neurona se entrena para resolver un problema concreto, que consiste en, recibiendo las siguientes entradas ofrecer la salida indicada (si os fijáis, es símplemente el valor del dígito de más a la izquierda):

[0, 0, 1] -> 0

[1, 1, 1] -> 1

[1, 0, 1] -> 1

[0, 1, 1]] ->0

Y verifica cuál es la salida para una nueva situación, concretamente [1, 0, 0].

Ejecuta el programa y verifica si ofrece la solución correcta.

Realiza modificaciones en el programa:

- Verifica el valor de salida para una entrada diferente
- Cambia el problema a resolver
