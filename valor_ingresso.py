def valor_cinema_opcional(idade, carteirinha_estudante=False):
    valor_ingresso = 15  # valor normal
    valor_crianca = 11  # para pessoas com menos de 10 anos
    valor_idoso = 10  # para pessoas com mais de 60 anos
    valor_ingresso_final = None
    if carteirinha_estudante or idade <= 10:  # para quem tem carteirinha de estudante ou é criança
        valor_ingresso_final = valor_crianca
    elif 10 < idade < 60:
        valor_ingresso_final = valor_ingresso
    elif idade >= 60:
        valor_ingresso_final = valor_idoso
    return valor_ingresso_final
