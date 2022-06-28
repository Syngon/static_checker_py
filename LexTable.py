class LexTable:
    def __init__(self, token, lexeme, filepath):
        self.token = token
        self.lexeme = lexeme
        self.filepath = filepath

        self.create_report()
       
    # Retorna o idx do lexeme da tablea de simbolos
    def get_idx_tab(self, lexeme):
        arq_read = open("txts/"+self.filepath.split('/')[-1].replace('.DKS', '.TAB'), 'r')
        
        for line in arq_read:
            if lexeme in line and '@' not in line and 'CODIGO' not in line:
                return line.split(',')[0]
        return " - "

    # Cria o documento do .LEX
    def create_report(self):
        try:
            arq = open(self.filepath.replace('.DKS', '.LEX'), 'w')
        except Exception as e:
            print('Erro ao criar o arquivo .LEX')
            return


        arq.write('\n@@ CODIGO IDENTIFICADOR DA EQUIPE: (EQ05) @@\n')
        arq.write('@@ ALEX BOANERGES DE SANTANA FERREIRA JUNIOR - alex.junior@aln.senaicimatec.edu.br - (71) 99280-7708 @@\n')
        arq.write('@@ JOLISAN VINICIUS DE SANTANA SANTOS - jolisan.santos@aln.senaicimatec.edu.br - (71) 98750-8235 @@\n')
        arq.write('@@ PEDRO MARIANO REIS MONNERAT VIANNA - pedro.vianna@aln.senaicimatec.edu.br - (71) 98129-7852 @@\n')
        arq.write('@@ VICTOR HUGO FALCAO MARTINS ROCHA - victor.falcao@aln.senaicimatec.edu.br - (71) 99152-8061 @@\n')
        arq.write('\n\n')

        arq.write('Lexeme, Codigo atomo, Indice tabela simbolos\n')

        for idx, item in enumerate(self.token):
            idx_tab = ""

            if 'ID' in self.token[idx]:
                idx_tab = self.get_idx_tab(self.lexeme[idx][:35])
            else:
                idx_tab = " - "
        
            print(self.lexeme[idx], self.token[idx], idx_tab)
            arq.write('{}, {}, {}\n'.format(self.lexeme[idx][:35], self.token[idx], idx_tab))

        print('\n\n\n')