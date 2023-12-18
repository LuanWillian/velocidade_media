def vm(SI, SF, TI, TF, MS):
    """
    Essa função descobre a Velocidade media de um objeto
    :param SI: Pega km/h ou m/s do inicio do movimento do objeto
    :param SF: Pega km/h ou m/s do fim do movimento do objeto
    :param TI: Pega o inicio da hora ou segundos que o objeto se locomoveu
    :param TF: Pega o fim da hora ou segundos que o objeto se locomoveu
    :param MS: Pega o km/h ou m/s para formata junto com o resultado
    :return: Retorna a velocidade media do objeto
    """
    si = int(SI) #Converte a string em numero inteiro
    sf = int(SF) #Converte a string em numero inteiro
    ti = int(TI) #Converte a string em numero inteiro
    tf = int(TF) #Converte a string em numero inteiro
    distancia = sf - si
    deltaS = distancia
    tempo = tf - ti
    deltaT = tempo
    vm = deltaS / deltaT
    return f'A velocidade media foi: {vm} {MS}'.replace('.',',')
