#!/usr/bin/python
# -*- coding: latin-1 -*-

import requests as req
import json
import time
import xlsxwriter


class VendasRedes:
    def __init__(self):
        self.list_of_start_date = ['2019-11-01', '2019-12-01', '2020-01-01']
        self.list_of_end_date = ['2019-11-30', '2019-12-31', '2020-01-24']
        self.list_of_pvs = [19147686, 7957190]

    # Navega ate a tela de relatorios
    def navigate_rel_vendas(self):
        print('--------------------INICIANDO GERAÇÃO DOS RELATÓRIOS--------------------')
        for pv in self.list_of_pvs:
            for idx, startDate in enumerate(self.list_of_start_date):
                self.api = 'https://meu.userede.com.br/api/ke3/prd/v1/sales/daily?size=100000&startDate={}&endDate={}&brands=&modalities=&pvs={}&terminals=&status=&pvCode=&nsuTid='.format(
                    self.list_of_start_date[idx], self.list_of_end_date[idx], pv)

                headers = {
                    'content-type': 'application/json',
                    'Authorization': 'CHAVE AQUI'
                }
                response = req.get(self.api, headers=headers)
                try:
                    json_str = json.loads(response.text)
                    values = json_str['content']['salesDaily']

                    filename = 'relatório-{}-{}-{}.xlsx'.format(self.list_of_start_date[idx], self.list_of_end_date[idx], pv)
                    workbook = xlsxwriter.Workbook(filename)
                    worksheet = workbook.add_worksheet()

                    bold = workbook.add_format({'bold': True})

                    worksheet.write('A1', 'data da venda', bold)
                    worksheet.write('B1', 'hora da venda', bold)
                    worksheet.write('C1', 'valor da venda', bold)
                    worksheet.write('D1', 'numero de parcelas', bold)
                    worksheet.write('E1', 'modalidade', bold)
                    worksheet.write('F1', 'bandeira', bold)
                    worksheet.write('G1', 'taxa MDR', bold)
                    worksheet.write('H1', 'valor descontado', bold)
                    worksheet.write('I1', 'valor liquido', bold)
                    worksheet.write('J1', 'NSU/CV', bold)
                    worksheet.write('K1', 'resumo de vendas/numero do lote', bold)
                    worksheet.write('L1', 'numero da autorizacao', bold)
                    worksheet.write('M1', 'numero do estabelicimento', bold)
                    worksheet.write('N1', 'nome do estabelicimento', bold)
                    worksheet.write('O1', 'Cnpj', bold)
                    worksheet.write('P1', 'numero do cartao', bold)
                    worksheet.write('Q1', 'id carteira digital', bold)
                    worksheet.write('R1', 'tipo de captura', bold)
                    worksheet.write('S1', 'tipo de terminal', bold)
                    worksheet.write('T1', 'codigo do terminal', bold)
                    worksheet.write('U1', 'TID', bold)
                    worksheet.write('V1', 'taxa de embarque', bold)
                    worksheet.write('W1', 'cancelada pelo estabelecimento', bold)
                    worksheet.write('X1', 'data do cancelamento', bold)
                    worksheet.write('Y1', 'valor cancelado', bold)
                    worksheet.write('Z1', 'em disputa de chargeback', bold)
                    worksheet.write('AA1', 'data em que entrou em disputa chargeback', bold)
                    worksheet.write('AB1', 'resolucacao do chargeback', bold)
                    worksheet.write('AC1', 'data da resolucao do chargeback', bold)
                    worksheet.write('AD1', 'nacionalidade do cartao', bold)
                    row = 1

                    for first in values:
                        for second in first['sales']:
                            worksheet.write(row, 0, second['date'])
                            worksheet.write(row, 1, second['hour'])
                            worksheet.write(row, 2, second['amount'])
                            worksheet.write(row, 3, second['installmentQuantity'])
                            worksheet.write(row, 4, second['modality'])
                            worksheet.write(row, 5, second['brandCode'])
                            worksheet.write(row, 6, second['mdrFee'])
                            worksheet.write(row, 7, second['discountAmount'])
                            worksheet.write(row, 8, second['netAmount'])
                            worksheet.write(row, 9, second['nsu'])
                            worksheet.write(row, 10, second['rvNumber'])
                            worksheet.write(row, 11, second['authorizationCode'])
                            worksheet.write(row, 12, second['pvCode'])
                            worksheet.write(row, 13, second['pvName'])
                            worksheet.write(row, 14, second['pvCnpj'])
                            worksheet.write(row, 15, second['cardNumber'])
                            worksheet.write(row, 16, 'nao encontrei esse valor')
                            worksheet.write(row, 17, second['captureType'])
                            worksheet.write(row, 18, second['equipmentCode'])
                            worksheet.write(row, 19, second['terminal'])
                            worksheet.write(row, 20, 'TID tambem nao encontrei')
                            worksheet.write(row, 21, second['departureFeeAmount'])
                            worksheet.write(row, 22, 'Cancelado pelo estabelicimento nao achei')
                            worksheet.write(row, 23, 'Data do cancelamento')
                            worksheet.write(row, 24, 'Valor cancelado')
                            worksheet.write(row, 25, 'Em disputa de chargeback nao achei')
                            worksheet.write(row, 26, 'Data em que entrou em disputa')
                            worksheet.write(row, 27, 'resolucao do chargeback')
                            worksheet.write(row, 28, 'Data da resolucao tambem nao encontrei')
                            worksheet.write(row, 29, 'internacional' if second['international'] else 'nacional')
                            row += 1
                    workbook.close()
                    print('Relatório {} gerado com sucesso'.format(filename))
                except:
                    print('Não foi possível gerar o relatório do pv {} na data {} - {}'.format(pv,
                                                                                               self.list_of_start_date[idx],
                                                                                               self.list_of_end_date[idx]))

        print("------------------GERAÇÃO CONCLUÍDA-------------------")


vendas = VendasRedes()

time.sleep(8)
vendas.navigate_rel_vendas()


