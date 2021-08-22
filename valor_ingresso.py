import numpy as np

def valor_cinema_opcional(idade, carteirinha_estudante=False):
    """
    Código para calcular o valor de um ingresso dada a idade de uma pessoa e se ela possui carteirinha de estudante.

    :param idade: inteiro que representa a idade da pessoa
    :param carteirinha_estudante: booleano que indica se a pessoa tem ou não carteirinha de estudante
    :return: inteiro que representa o valor do ingresso
    """
    valor_ingresso = 15  # valor normal
    valor_crianca = 11  # para pessoas com menos de 10 anos
    valor_idoso = 9  # para pessoas com mais de 60 anos
    valor_ingresso_final = None
    if carteirinha_estudante or idade <= 10:  # para quem tem carteirinha de estudante ou é criança
        valor_ingresso_final = valor_crianca
    elif 10 < idade < 60:
        valor_ingresso_final = valor_ingresso
    elif idade >= 60:
        valor_ingresso_final = valor_idoso
    return valor_ingresso_final
