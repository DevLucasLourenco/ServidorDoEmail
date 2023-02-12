def encontrar_servidor_email(item: str) -> str:
    arromba = item.index('@')

    if arromba:
        pos_email = item[arromba + 1:]
        ponto = pos_email.index('.')
        
        servidor = item[arromba+1 : arromba + ponto + 1]
        print(servidor)
        


encontrar_servidor_email('dev.lucaslourenco@gmail.com')
