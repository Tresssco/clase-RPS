## Estructura do proxecto / rubrica

1.**Entorno de tareas**

En este apartado especificaremos las características del entorno de tareas del RPS (Rock, Paper, Scissors), basandonos en el epígrafe _"2.3.2 Properties of task environments"_ del libro _Intelligent Agents_ do libro _IA: A modern approach, Russell & Norvig_ justificaremos las respuestas.

Las características del entorno que analizaremos en este caso son las siguientes:

*   **Observable:** _Totalmente observable / Parcialmente Observable / No observable_
*   **Agentes:** _Un solo agente / Multiagente_
*   **Determinista:** _Determinista / No determinista / Estocástico_
*   **Episódico:** _Episódico / Secuencial_
*   **Estático:** _Estático / Dinámico / Semidinámico_
*   **Discreto:** _Discreto / Continuo_
*   **Conocido:** _Conocido / Desconocido_

Estas son las 7 características con sus respectivos posibles valores.

Utilizaré una tabla para mostrar visualmente los valores escogidos y, posteriormente, justificaré cada uno de ellos.

Contorno de tareas | Observable| Agentes | Determinista | Episódico | Estático | Discreto | Conocido
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 RPS | Parcialmente Observable | Multiagente | Estocástico | Episódico | Estático |  Discreto |  Conocido |

Ahora pasaré a explicar cada una de las elecciones, recordar que todas están basadas en la información proporcionada por el libro mencionado anteriormente.

- **_Parcialmente Observable_**: Un entorno es _completamente observable_ si a través de los sensores del agente tenemos la información completa siempre del entorno, en el caso de no disponer de toda la información o de esta no ser precisa sería _parcialmente observable_, si no disponemos de sensores entonces es _no observable_.<br>
En el caso del RPS, sabemos que el rival puede escoger piedra, papel o tijera, pero no tenemos ninguna forma de conocer de forma precisa la elección del rival, por eso es un entorno **parcialmente observable**

- **_Multiagente_**: Esta característica aborda el número de agentes implicados en la tarea, el RPS necesita como mínimo a dos jugadores para poder desarrollarse, aquí surge la distinción sobre el comportamiento entre estos, si _cooperan_ entre ellos o _compiten_, en nuestro caso claramente compiten entre ellos por maximizar su rendimiento, por lo que seria un entorno **multiagente competitivo**.

- **_Estocástico_**: Primeramente hay que aclarar que estocástico es un sinónimo de _No determinista_ con la diferencia de que el término _Estocástico_ trata explicitamente con las probabilidades, mientras que _No determinista_ son posibilidades sin ser cuantificadas (_pág 64 del libro_). 
En el caso del RPS sabemos con anterioridad que el rival solo puede sacar 3 resultados posibles: Piedra, papel o tijera, por lo que tendriamos un 1/3 de probabilidades de ganar, empatar o perder.

- **_Episódico_**: Un entorno episódico tiene como caracteristica más importante que las decisiones tomadas no afectan a decisiones futuras. 
El juego RPS en su forma más esencial es episódico, por ejemplo: Sacar piedra en la primera ronda no afecta directamente a la decision tomada en la quinta ronda, las reglas son las mismas y las probabilidades tambien. Sin embargo *podría llegar a ser secuencial* si tu oponente opera con estrategias en base a tus decisiones anteriores, ya que en este caso tus decisiones si tendrían un impacto en las decisiones del rival y por ende del resultado.
Pese a eso me parece que el RPS debería ser tratado como episódico, ya que cada ronda es independiente y no influye directamente en las demás.

- **_Estatico_**: Aqui nos encontramos en una tesitura similar a la anterior. El RPS es un juego estático porque las reglas, el escenario y las selecciones no varian en ningún momento mientras decides que acción tomar. Sin embargo si un agente emplea estrategias creando un historial de jugadas observable el juego se tornaria dinámico ya que no se jugaria de forma aleatoria sino en base a una estrategia _dinámica_ adaptándose al rival.

- **_Discreto_**: El RPS es totalmente discreto, las posibles elecciones de cada agente y el resultado generado por estas es un *número finito*.

- **_Conocido_**: Esta característica se refiere a si el agente conoce como opera el entorno, es decir, las reglas. En el RPS se dan los resultados para todas las acciones tomadas, es decir, se saben las posibilidades de resultados.


2.**Identificación del agente y estructura**

En este apartado se elige el tipo de agente que vamos a emplear para programar las decisiones a tomar en el RPS. En el apartado 2.4 del libro se explican varios tipos de agentes y debemos escoger uno de ahí.

En mi caso elegí el "Model-based reflex agents", un agente bastante sencillo con la característica de poseer "memoria", es decir, un historial. Se ajusta bien al juego RPS porque vamos a decidir que sacar en cada ronda en base a las jugadas de nuestro oponente, intentando predecir el movimiento o extraer un patrón de juego con el objetivo de maximizar las victorias.

La estructura de nuestro agente adaptada al RPS seria la siguiente:


![Diagrama Agente RPS](./doc/Agente_RPS.png)

Primero el agente observa el entorno del RPS. En base al historial de juegos analizamos y sabemos el estado actual del juego: el numero total de rondas jugadas, que movimientos uso el rival, la frecuencia y posibles patrones de jugadas. Con esta información, a través de un algoritmo se intenta predecir el movimiento que nuestro oponente utilizará. Una vez sabiendo la jugada del rival nos falta saber que jugada deberíamos hacer, para eso habría que aplicar las reglas del RPS y saber que movimiento es el que nos dará la victoria. Sabiendo el movimiento del rival y el que el agente debe tomar solo nos queda actuar para conocer el estado en el que se queda el entorno.


3.**Implementación en Python**

El código implementado en src/RPS_implementacion funciona de la siguiente manera:

Se introduce un historial de jugadas y otro del resultado de las jugadas. En el estado inicial del mundo al no existir jugadas previas el agente tomará una elección al azar de su jugada. A partir de la primera jugada del rival ya existirán datos en el historial de jugadas. El agente jugará lo contrario a la anterior jugada del rival, por ejemplo, si el rival la anterior jugada jugó papel el agente jugará tijera.

Esta estrategia es sencilla y tiene el problema de que el rival se de cuenta de nuestra estrategia, en ese caso siempre ganaría el rival. Por eso se implementó una estrategia adicional. En caso de que el rival gane 3 rondas consecutivamente las dos próximas jugadas del agente serán idénticas a la anterior jugada del rival, esto es porque, en caso de detectar que el rival sabe nuestra estrategia, también sabremos que va a sacar y podremos contrarrestarlo. Un ejemplo: Si llevamos 3 rondas seguidas perdidas y el rival en la última jugada jugó papel, podemos intuir que sabe que sacaremos tijera y el entonces sacará piedra, por eso sacaremos papel. Esto lo repetimos 2 veces para que el rival no intuya que es simplemente una estrategia adicional.

El código sigue los principios SOLID y se podria extender la lógica a versiones más complejas del RPS.

4.**Extensión ao RPS + Lizzard Spock**

El código implementado en src/RPS_LizzardSpock es una extensión del RPS_Implementacion donde se agregan 2 variables de juego más, el lizzard y el spock. Ahora el juego tiene muchas más combinaciones de jugadas ya que un elemento gana a otros 2. Por esta razón el código necesita un diccionario donde se almacena cada elemento y sus 2 elementos a los que gana. También se necesitaba que la función que determina al ganador "asses_game" ahora emplease este diccionario, de forma que fuera un código sencillo de extender a múltiples nuevos elementos. Este cambio en la forma de manejar las victorias también se aplicará en el código original RPS_Implementación.

La estrategia se mantiene igual.
