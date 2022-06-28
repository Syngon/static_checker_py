import re

class LexicalAnalyzer:
    lin_num = 1

    def tokenize(self, code):
        rules = [
            ("PR09", r"BEGIN"),     
            ("PR01", r"BOOL"),
            ("PR14", r"INT"),       # int
            ("PR13", r"FLOAT"),     # float
            ("PR07", r"IF"),        # if
            ("PR15", r"ELSE"),      # else
            ("PR02", r"WHILE"),     # while
            ("PR03", r"BREAK"),
            ("PR05", r"CHAR"),
            ("PR06", r"TRUE"),
            ("PR11", r"FALSE"),
            ("PR08", r"STRING"),
            ("PR12", r"PROGRAM"),
            ("PR16", r"END"),
            ("PR10", r"RETURN"),
            ("PR04", r"VOID"),
            ("ID06", r"\d(\d)*\.\d(\d)*|e\+\d(\d)*|e-\d(\d)*|e\d(\d)*"),  # FLOAT
            ("SR03", r"\("),  # (
            ("SR04", r"\)"),  # )
            ("SR07", r"\{"),  # {
            ("SR06", r"\["),
            ("SR17", r"\]"),
            ("SR19", r"\}"),  # }
            ("SR08", r","),  # ,
            ("SR05", r";"),  # ;
            ("SR02", r"&"),
            ("SR13", r"%"),
            ("SR21", r"=="),  # ==
            ("SR01", r"!=|#"),  # !=
            # ('SR71', r'\#'),
            ("SR12", r"!"),
            ("SR09", r"<="),  # <=
            ("SR11", r">="),  # >=
            ("SR10", r"\="),  # =
            ("SR20", r"\<"),  # <
            ("SR22", r"\>"),  # >
            ("SR16", r"\+"),  # +
            ("SR23", r"\-"),  # -
            ("SR15", r"\*"),  # *
            ("SR14", r"\/"),  # /
            ("SR18", r"\|"),
            ("ID01", r"[a-zA-Z]\w*"),  # IDENTIFIERS

            ("ID03", r"\d(\d)*"),  # INT
            ("NOVALINHA", r"\n"),  # NOVA LINHA
            ("PULAR", r"[ |\t]+"),  # SPACE E TAB
            ("OUTROCHAR", r"."),  # OUTRO CARACTERE QUE NAO ESTA NA LINGUAGEM
        ]

        tokens_join = "|".join("(?P<%s>%s)" % x for x in rules)
        lin_start = 0

        # Lista de saidas
        token = []
        lexeme = []
        row = []
        column = []

        # Analisa o codigo e acha o lexeme e o token respectivo
        for m in re.finditer(tokens_join, code.upper()):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == "NOVALINHA":
                lin_start = m.end()
                self.lin_num += 1
            elif token_type == "PULAR":
                continue
            elif token_type == "OUTROCHAR":
                print("%r nao esperado na linha %d" % (token_lexeme, self.lin_num))
            else:
                col = m.start() - lin_start
                column.append(col)
                token.append(token_type)
                lexeme.append(token_lexeme)
                row.append(self.lin_num)

                # Printa as informacoes
                #print(
                #    "Token = {0}, Lexeme = '{1}', Linha = {2}, Coluna = {3}".format(
                #        token_type, token_lexeme, self.lin_num, col
                #    )
                #)

        print('\n\n\n')

        return token, lexeme, row, column
