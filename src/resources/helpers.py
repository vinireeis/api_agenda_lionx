from uuid import uuid4


def add_contact_id(novo_contato):
    novo_contato['contact_id'] = str(uuid4())
    return novo_contato


def add_activity_attr(novo_contato):
    novo_contato['situaction'] = 'ativo'
    return novo_contato


def add_full_name(novo_contato):
    novo_contato['name'] = f"{novo_contato['firstName'], novo_contato['lastName']}"


def deactivate_activity_attr(contato):
    if contato['situacion'] == 'ativo':
        contato.update(situacao='desativado')
    return contato


def add_total_contacts_by_type(lista_contatos):
    total, total_residential, total_commercial, total_mobile = 0
    for contato in lista_contatos:
        total += 1
        if contato['type'] == 'residential':
            total_residential += 1
        elif contato['type'] == 'commercial':
            total_commercial += 1
        else:
            total_mobile += 1
        dic_retorno = {'totals': {'total': total, 'totalCommercial': total_commercial,
                                  'totalMobile': total_mobile, 'totalResidential': total_residential},
                       'contacts': lista_contatos
                       }
    return dic_retorno


# def add_totals_in_contact_dict(contatos, dic_totais):
#     contatos.update(dic_totais)
#     return contatos
