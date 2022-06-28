class SymbolTable:
    def __init__(self, token, lexeme, row, filename):
        self.token = token
        self.lexeme = lexeme
        self.row = row
        self.filename = filename

        self.create_report()

    # Cria o documento do .TAB
    def create_report(self):
        obj = {}
        ordered_list = []
        try:
            arq = open(self.filename.replace('.DKS', '.TAB'), 'w')
        except Exception as e:
            print('Erro ao criar o arquivo .TAB')
            return

        count = 0

        for idx, item in enumerate(self.token):
            if 'ID' not in self.token[idx]:
                continue
            
            if self.lexeme[idx] not in obj.keys():
                obj[self.lexeme[idx]] = {
                        'id': count,
                        'lexeme': self.lexeme[idx][:35],
                        'size_before':len(self.lexeme[idx]),
                        'token': self.token[idx],
                        'linhas': [self.row[idx]]

                        }
                count += 1
                ordered_list.append(obj[self.lexeme[idx]])
            else:
                for item in ordered_list:
                    if self.lexeme[idx] == item['lexeme']:
                        item['linhas'].append(self.row[idx])



        arq.write('\n@@ CODIGO IDENTIFICADOR DA EQUIPE: (EQ05) @@\n')
        arq.write('@@ ALEX BOANERGES DE SANTANA FERREIRA JUNIOR - alex.junior@aln.senaicimatec.edu.br - (71) 99280-7708 @@\n')
        arq.write('@@ JOLISAN VINICIUS DE SANTANA SANTOS - jolisan.santos@aln.senaicimatec.edu.br - (71) 98750-8235 @@\n')
        arq.write('@@ PEDRO MARIANO REIS MONNERAT VIANNA - pedro.vianna@aln.senaicimatec.edu.br - (71) 98129-7852 @@\n')
        arq.write('@@ VICTOR HUGO FALCAO MARTINS ROCHA - victor.falcao@aln.senaicimatec.edu.br - (71) 99152-8061 @@\n')
        arq.write('\n\n')

        arq.write('id, lexeme, token, qnt_antes, qnt_dps, tipo, linhas\n')
        for item in ordered_list:
            print("{:<8} {:<15} {:<10}".format(item['lexeme'], item['token'], ''.join(str(item['linhas']))))
            aux = ''
            if item['token'] == 'ID03':
                aux = 'INT'
            elif item['token'] == 'ID06':
                aux = 'FLOAT'
            else:
                aux = 'VOID'
            arq.write('{}, {}, {}, {}, {}, {}, {}\n'.format(item['id'], item['lexeme'], item['token'], item['size_before'], len(item['lexeme']), aux, item['linhas']))

        print('\n\n\n')

