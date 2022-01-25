from uuid import uuid4


def adciona_id_no_contato(novo_contato):
    novo_contato['contato_id'] = str(uuid4())
    return novo_contato


def adciona_situacao_no_contato(novo_contato):
    novo_contato['situacao'] = 'ativo'
    return novo_contato


def desativa_contato(contato):
    if contato['situacao'] == 'ativo':
        contato.update(situacao='desativado')
    return contato


def total_de_contatos_e_por_tipo(lista_contatos):
    total, total_residential, total_commercial, total_mobile = 0
    for contato in lista_contatos:
        total += 1
        if contato['type'] == 'residential':
            total_residential += 1
        elif contato['type'] == 'commercial':
            total_commercial += 1
        else:
            total_mobile += 1
        dic_retorno = {'totais': {'total': total, 'totalCommercial': total_commercial,
                                  'totalMobile': total_mobile, 'totalResidential': total_residential}}
    return dic_retorno


def adciona_totais_no_dic_contato(contatos, dic_totais):
    contatos.update(dic_totais)
    return contatos