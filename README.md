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


2.**Identificación do tipo de axente e estrutura**







Selecciona un tipo de axente adecuado para o RPS e debuxa un modelo preciso da estrutura do axente, incluíndo os compoñentes específicos do tipo elixido, baseándoche nos conceptos do capítulo 2 _"Intelligent Agents"_.

É moi importante que ademáis da figura escribas un texto enumerando e xustificando a presenza dous comppñentes recollidos na figura anterior. Sen explicacións a figura non se avalía.

3.**Implementación en Python**

Implementa en Python todos os compoñentes da estrutura do axente de forma correcta e eficiente, creando unha función axente que xoga ao RPS seguindo a lóxica do tipo de axente seleccionado. O código cumpre cos principios SOLID, especialmente SRP e OCP, permitindo estender a lóxica a outras versións do xogo. **A estratexia implementada en `get_computer_action()` é creativa e busca maximizar o rendemento do axente**.

O teu código pode e debe ser modular seguindo o principio SRP, pero **a execución da lóxica ten que invocarse dende a función `get_computer_action()`.

A rúbrica da implementación Python [na segunda folla "RPS" deste libro de cálculo.](https://docs.google.com/spreadsheets/d/1r93uZnPmioY0U1D7EDtV1uveKYIOlenkz8uuqks4KXM/) Loguéate antes na túa conta de gmail con acceso ao noso Drive.

4.**Extensión ao RPS + Lizzard Spock**

- Estende a lóxica do axente para xogar á versión "pedra, papel, tesoiras, lagarto, Spock" correctamente, mantendo a calidade do código e a coherencia co tipo de axente seleccionado. 

- A documentación no README do proxecto en GitHub/GitLab deber estar completa seguindo a orde especificada nesta rúbrica, explicando o problema, a contorna de tarefas, a estrutura do axente, a implementación e a extensión, cun formato Markdown axeitado.
