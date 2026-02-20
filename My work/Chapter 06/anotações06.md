# Guia de Referência Rápida: Classes em Python (Módulo 6)

Este módulo introduz a Programação Orientada a Objetos (POO), englobando criação de classes, propriedades, métodos mágicos, herança e polimorfismo [1], [2].

## 1. Dicionário de Sintaxe
Comandos e funções fundamentais para o trabalho com classes e objetos.

| Comando/Keyword | O que faz (Descrição Curta) | Exemplo de código |
| :--- | :--- | :--- |
| `class` | Define um novo tipo de dado personalizado (uma classe) [1], [3]. | `class Student:` |
| `self` | Referência explícita à instância atual do objeto. Deve ser o primeiro parâmetro de métodos de instância [4]. | `self.name = name` |
| `__init__()` | Método construtor especial. É chamado automaticamente ao instanciar o objeto para inicializar dados [5], [4]. | `def __init__(self, name):` |
| `@property` | Decorator que transforma um método em um *getter*, permitindo acesso ao atributo como se fosse uma variável [6], [7]. | `@property` <br> `def name(self):` |
| `@x.setter` | Decorator para definir o *setter* de uma propriedade "x", possibilitando validações de atribuição [6], [7]. | `@name.setter` <br> `def name(self, val):` |
| `super()` | Retorna um objeto proxy para chamar métodos herdados da classe pai (superclasse) [8], [9]. | `super().__init__(name)` |
| `type()` | Função embutida que identifica o tipo (classe) de uma variável no momento da execução [10]. | `type(obj) == Student` |
| `isinstance()` | Verifica se um objeto é uma instância de uma classe específica ou de suas derivadas [11]. | `isinstance(obj, Manager)` |
| `issubclass()` | Verifica se uma classe é derivada (subclasse) de outra classe diretamente ou indiretamente [11]. | `issubclass(Executive, Employee)` |

---

## 2. Operadores, Símbolos e Regras

### Métodos Especiais (Operator Overloading)
As classes podem implementar métodos com nomes especiais (entre sublinhados duplos) para redefinir como operadores padrão funcionam com aqueles objetos [12].

*   `__str__(self)`: Invocado pelas funções embutidas `str()` e `print()` para retornar uma representação em formato de string legível do objeto [12], [13].
*   `__del__(self)`: Chamado quando a instância está prestes a ser destruída (quando a contagem de referências chega a zero) [12].
*   `__eq__(self, other)`: Sobrecarga do operador de igualdade `==` [12], [14].
*   `__lt__(self, other)`: Sobrecarga do operador menor que `<` [15], [14].
*   `__mul__(self, other)`: Sobrecarga do operador de multiplicação `*` [15].

### Variáveis de Instância vs. Classe
*   **Variáveis de Instância:** Usam `self.` e contêm dados únicos para cada objeto criado (ex: o nome de um aluno) [16].
*   **Variáveis de Classe:** Definidas diretamente dentro da classe, mas fora de qualquer método. São compartilhadas por **todas** as instâncias dessa classe [16].

---

## 3. Estrutura de Código (Visual)

### Esqueleto de Classe com Getters e Setters
O uso do decorator `@property` é a forma "Pythônica" de aplicar encapsulamento [6].

```python
class Student:
    # Variável de Classe (compartilhada)
    quantity = 0 
    
    def __init__(self, name):
        self.name = name          # Aciona o setter indiretamente
        Student.quantity += 1     # Atualiza variável de classe
        
    @property
    def name(self):
        return self._name         # Convenção: _nome indica atributo privado
        
    @name.setter
    def name(self, name):
        # Lógica de validação entraria aqui
        self._name = name
        
    def __str__(self):
        return "Estudante: {}".format(self.name)
Esqueleto de Herança e super()
As subclasses herdam os atributos e métodos da classe pai e podem estendê-los,.
class GradStudent(Student): # (Student) indica a SuperClasse
    def __init__(self, name, stipend):
        # Chama o construtor da classe pai usando super()
        super().__init__(name)
        self.stipend = stipend # Atributo específico da subclasse
        
    def __str__(self):
        # Substitui (Override) o método do pai, mas reutiliza parte dele
        return "{} - Bolsa: {}".format(super().__str__(), self.stipend)

--------------------------------------------------------------------------------
4. Checklist de Aplicação
• Precisa inicializar atributos no momento que o objeto é criado?
    ◦ Implemente o método def __init__(self, ...):.
• Quer que seu objeto não imprima um código estranho de memória ao usar print(obj)?
    ◦ Defina o método especial def __str__(self): retornando uma string.
• Precisa interceptar e validar dados toda vez que alguém modifica um atributo?
    ◦ Use os decorators @property para ler e @nomedapropriedade.setter para modificar.
• Deseja manter uma contagem de quantos objetos da sua classe já foram criados?
    ◦ Use uma Class Variable (declarada fora do __init__).
• Precisa criar um tipo de dado novo que já faz tudo o que um tipo anterior faz, mas com funcionalidades extras?
    ◦ Use Herança (class Filha(Pai):) e aproveite o construtor original através do super().__init__(),.
• Precisa checar se os dados de dois objetos são iguais (obj1 == obj2)?
    ◦ Implemente o método mágico de sobrecarga def __eq__(self, obj): para ensinar o Python a compará-los.
• Deseja validar se a variável atual é do tipo "Manager" antes de executar uma ação?
    ◦ Use a função embutida isinstance(variavel, Manager)