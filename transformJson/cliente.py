def clienteJson(cliente):
    id, documento, email, nome, username = cliente[0]
    dados = {
        "documento": documento,
        "email": email,
        "id": id,
        "nome": nome,
        "username": username
    }
    return {"dados": dados}

def clientePlataformasJson(plataformas):
    dados = {"plataformas": []}
    for plataforma in plataformas:
        id, id_cliente, email, senha, nome, api_key, secret_key = plataforma
        dados["plataformas"].append({
            "api_key": api_key,
            "email": email,
            "id": id,
            "id_cliente": id_cliente,
            "nome": nome,
            "secret_key": secret_key,
            "senha": senha
        })
    return dados

def clienteEstrategiasJson(estrategias):
    dados = {"estrategias": []}
    for estrategia in estrategias:
        id, id_cliente, nome, data, custo = estrategia
        #mudar quando o banco estiver mais organizado pois precisarei das campanhas e plataformas
        dados["estrategias"].append({
            "custo": custo,
            "data": data,
            "id": id,
            "id_cliente": id_cliente,
            "nome": nome,
        })
    return dados

def clienteCampanhasJson(campanhas):
    dados = {"campanhas": []}
    for campanha in campanhas:
        id, id_estrategia, nome, data, custo, status, tipo, plataforma = campanha
        #mudar quando o banco estiver mais organizado pois precisarei das campanhas e plataformas
        dados["campanhas"].append({
            "custo": custo,
            "data": data,
            "id": id,
            "id_estrategia": id_estrategia,
            "nome": nome,
            "plataforma": plataforma,
            "status": status,
            "tipo": tipo,
        })
    return dados