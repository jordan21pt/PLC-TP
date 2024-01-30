
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'Diferente Divisao E Enquanto Escrever Faz Fim Igual Inicio Ler Maior MaiorIgual Menor MenorIgual Multiplicacao Negar Num OU ParCurvoDir ParCurvoEsq ParRetoDir ParRetoEsq Para PontoVirgula Se Senao Soma String Subtracao Tipo Vale Var\n\tPrograma : Inicio Corpo Fim\n\t\n\tCorpo : Declaracoes Instrucoes\n\t\n\tDeclaracoes : Declaracoes Declaracao\n\t\n\tDeclaracoes : \n\t\n\tDeclaracao : Tipo Var PontoVirgula\n\t\n\tDeclaracao : Tipo Var  Expressao ParRetoDir PontoVirgula\n\t\n\tDeclaracao : Tipo Var ParRetoEsq Expressao ParRetoDir ParRetoEsq Expressao ParRetoDir PontoVirgula\n\t\n\tInstrucoes : Instrucoes Instrucao\n\t\n\tInstrucoes : \n\t\n\tInstrucao : Atribuicao\n\t\t| Leitura\n\t\t| Escrita\n\t\t| Selecao\n\t\t| Repeticao\n\t\n\tAtribuicao : Var Vale Expressao PontoVirgula\n\t\n\tAtribuicao : Var ParRetoEsq Expressao ParRetoDir Vale Expressao PontoVirgula\n\t\n\tAtribuicao : Var ParRetoEsq Expressao ParRetoDir ParRetoEsq Expressao ParRetoDir Vale Expressao PontoVirgula\n\t\n\tCondicao : Expressao\n\t\n    Condicao : Expressao Igual Expressao\n        | Expressao Diferente Expressao\n        | Expressao MenorIgual Expressao\n        | Expressao MaiorIgual Expressao\n        | Expressao Menor Expressao\n        | Expressao Maior Expressao\n    \n\tExpressao : Termo\n\t\n\tExpressao : Expressao Soma Termo\n\t\t| Expressao Subtracao Termo\n\t\t| Expressao OU Termo\n\t\n\tTermo : Fator\n\t\n\tTermo : Termo Multiplicacao Fator\n\t\t| Termo Divisao Fator\n\t\t| Termo E Fator\n\t\n\tFator : Frase\n\t\n\tFator : Var ParRetoEsq Expressao ParRetoDir\n\t\n\tFator : Var ParRetoEsq Expressao ParRetoDir ParRetoEsq Expressao ParRetoDir \n\t\n\tFator : ParCurvoEsq Condicao ParCurvoDir\n\t\n\tFator : Negar Fator\n\t\n\tLeitura : Ler PontoVirgula\n\t\n\tEscrita : Escrever ParCurvoEsq Expressao ParCurvoDir PontoVirgula\n\t\n\tSelecao : Se ParCurvoEsq Condicao ParCurvoDir Faz Instrucoes PontoVirgula\n\t\n\tSelecao : Se ParCurvoEsq Condicao ParCurvoDir Faz Instrucoes Senao Instrucoes PontoVirgula\n\t\n\tRepeticao : Enquanto ParCurvoEsq Condicao ParCurvoDir Faz Instrucoes PontoVirgula\n\t\n\tRepeticao : Para ParCurvoEsq Atribuicao PontoVirgula Condicao PontoVirgula Atribuicao ParCurvoDir Faz Instrucoes PontoVirgula\n\t\n\tFrase : String\n\t\n\tFrase : Lista_Palavras\n\t\n\tLista_Palavras : Palavra\n\t\n\tLista_Palavras : Lista_Palavras Palavra\t\n\t\n\tPalavra : Var\n\t\n\tPalavra : Num\n\t'
    
_lr_action_items = {'Inicio':([0,],[2,]),'$end':([1,5,],[0,-1,]),'Tipo':([2,4,7,30,75,117,],[-4,8,-3,-5,-6,-7,]),'Var':([2,4,6,7,8,9,10,11,12,13,14,21,22,23,24,25,26,27,28,29,30,32,36,37,39,40,41,49,51,52,53,55,56,57,60,61,62,66,67,68,69,70,71,73,75,84,85,86,87,94,97,100,101,102,103,106,107,108,109,113,114,117,119,120,121,122,123,],[-4,-9,15,-3,21,-8,-10,-11,-12,-13,-14,29,29,29,-38,29,29,29,15,-48,-5,29,29,29,61,-46,-49,29,29,29,29,29,29,29,-47,-48,-15,29,29,29,29,29,29,29,-6,29,29,-39,-9,-9,29,15,15,15,29,-16,-40,-9,-42,29,15,-7,-41,-9,-17,15,-43,]),'Ler':([2,4,6,7,9,10,11,12,13,14,24,30,62,75,86,87,94,100,101,106,107,108,109,114,117,119,120,121,122,123,],[-4,-9,16,-3,-8,-10,-11,-12,-13,-14,-38,-5,-15,-6,-39,-9,-9,16,16,-16,-40,-9,-42,16,-7,-41,-9,-17,16,-43,]),'Escrever':([2,4,6,7,9,10,11,12,13,14,24,30,62,75,86,87,94,100,101,106,107,108,109,114,117,119,120,121,122,123,],[-4,-9,17,-3,-8,-10,-11,-12,-13,-14,-38,-5,-15,-6,-39,-9,-9,17,17,-16,-40,-9,-42,17,-7,-41,-9,-17,17,-43,]),'Se':([2,4,6,7,9,10,11,12,13,14,24,30,62,75,86,87,94,100,101,106,107,108,109,114,117,119,120,121,122,123,],[-4,-9,18,-3,-8,-10,-11,-12,-13,-14,-38,-5,-15,-6,-39,-9,-9,18,18,-16,-40,-9,-42,18,-7,-41,-9,-17,18,-43,]),'Enquanto':([2,4,6,7,9,10,11,12,13,14,24,30,62,75,86,87,94,100,101,106,107,108,109,114,117,119,120,121,122,123,],[-4,-9,19,-3,-8,-10,-11,-12,-13,-14,-38,-5,-15,-6,-39,-9,-9,19,19,-16,-40,-9,-42,19,-7,-41,-9,-17,19,-43,]),'Para':([2,4,6,7,9,10,11,12,13,14,24,30,62,75,86,87,94,100,101,106,107,108,109,114,117,119,120,121,122,123,],[-4,-9,20,-3,-8,-10,-11,-12,-13,-14,-38,-5,-15,-6,-39,-9,-9,20,20,-16,-40,-9,-42,20,-7,-41,-9,-17,20,-43,]),'Fim':([2,3,4,6,7,9,10,11,12,13,14,24,30,62,75,86,106,107,109,117,119,121,123,],[-4,5,-9,-2,-3,-8,-10,-11,-12,-13,-14,-38,-5,-15,-6,-39,-16,-40,-42,-7,-41,-17,-43,]),'PontoVirgula':([9,10,11,12,13,14,16,21,24,29,33,34,35,38,39,40,41,42,46,48,50,59,60,61,62,64,76,77,78,80,81,82,83,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,112,114,116,118,119,120,121,122,123,],[-8,-10,-11,-12,-13,-14,24,30,-38,-48,-25,-29,-33,-44,-45,-46,-49,62,-18,73,75,-37,-47,-48,-15,86,-26,-27,-28,-30,-31,-32,-36,-39,-9,-19,-20,-21,-22,-23,-24,-9,102,-34,106,107,109,-16,-40,-9,-42,117,119,-35,121,-41,-9,-17,123,-43,]),'Senao':([9,10,11,12,13,14,24,62,86,87,100,106,107,109,119,121,123,],[-8,-10,-11,-12,-13,-14,-38,-15,-39,-9,108,-16,-40,-42,-41,-17,-43,]),'Vale':([15,63,105,],[22,85,113,]),'ParRetoEsq':([15,21,29,63,79,96,],[23,32,49,84,97,103,]),'ParCurvoEsq':([17,18,19,20,21,22,23,25,26,27,32,36,37,49,51,52,53,55,56,57,66,67,68,69,70,71,73,84,85,97,103,113,],[25,26,27,28,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'Negar':([21,22,23,25,26,27,32,36,37,49,51,52,53,55,56,57,66,67,68,69,70,71,73,84,85,97,103,113,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'String':([21,22,23,25,26,27,32,36,37,49,51,52,53,55,56,57,66,67,68,69,70,71,73,84,85,97,103,113,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'Num':([21,22,23,25,26,27,29,32,36,37,39,40,41,49,51,52,53,55,56,57,60,61,66,67,68,69,70,71,73,84,85,97,103,113,],[41,41,41,41,41,41,-48,41,41,41,41,-46,-49,41,41,41,41,41,41,41,-47,-48,41,41,41,41,41,41,41,41,41,41,41,41,]),'Multiplicacao':([29,33,34,35,38,39,40,41,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,55,-29,-33,-44,-45,-46,-49,-37,-47,-48,55,55,55,-30,-31,-32,-36,-34,-35,]),'Divisao':([29,33,34,35,38,39,40,41,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,56,-29,-33,-44,-45,-46,-49,-37,-47,-48,56,56,56,-30,-31,-32,-36,-34,-35,]),'E':([29,33,34,35,38,39,40,41,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,57,-29,-33,-44,-45,-46,-49,-37,-47,-48,57,57,57,-30,-31,-32,-36,-34,-35,]),'ParRetoDir':([29,31,33,34,35,38,39,40,41,43,54,59,60,61,74,76,77,78,80,81,82,83,96,98,104,111,116,],[-48,50,-25,-29,-33,-44,-45,-46,-49,63,79,-37,-47,-48,96,-26,-27,-28,-30,-31,-32,-36,-34,105,112,116,-35,]),'Soma':([29,31,33,34,35,38,39,40,41,42,43,44,46,54,59,60,61,74,76,77,78,80,81,82,83,88,89,90,91,92,93,96,98,99,104,111,116,118,],[-48,51,-25,-29,-33,-44,-45,-46,-49,51,51,51,51,51,-37,-47,-48,51,-26,-27,-28,-30,-31,-32,-36,51,51,51,51,51,51,-34,51,51,51,51,-35,51,]),'Subtracao':([29,31,33,34,35,38,39,40,41,42,43,44,46,54,59,60,61,74,76,77,78,80,81,82,83,88,89,90,91,92,93,96,98,99,104,111,116,118,],[-48,52,-25,-29,-33,-44,-45,-46,-49,52,52,52,52,52,-37,-47,-48,52,-26,-27,-28,-30,-31,-32,-36,52,52,52,52,52,52,-34,52,52,52,52,-35,52,]),'OU':([29,31,33,34,35,38,39,40,41,42,43,44,46,54,59,60,61,74,76,77,78,80,81,82,83,88,89,90,91,92,93,96,98,99,104,111,116,118,],[-48,53,-25,-29,-33,-44,-45,-46,-49,53,53,53,53,53,-37,-47,-48,53,-26,-27,-28,-30,-31,-32,-36,53,53,53,53,53,53,-34,53,53,53,53,-35,53,]),'ParCurvoDir':([29,33,34,35,38,39,40,41,44,45,46,47,58,59,60,61,62,76,77,78,80,81,82,83,88,89,90,91,92,93,96,106,110,116,121,],[-48,-25,-29,-33,-44,-45,-46,-49,64,65,-18,72,83,-37,-47,-48,-15,-26,-27,-28,-30,-31,-32,-36,-19,-20,-21,-22,-23,-24,-34,-16,115,-35,-17,]),'Igual':([29,33,34,35,38,39,40,41,46,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,-25,-29,-33,-44,-45,-46,-49,66,-37,-47,-48,-26,-27,-28,-30,-31,-32,-36,-34,-35,]),'Diferente':([29,33,34,35,38,39,40,41,46,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,-25,-29,-33,-44,-45,-46,-49,67,-37,-47,-48,-26,-27,-28,-30,-31,-32,-36,-34,-35,]),'MenorIgual':([29,33,34,35,38,39,40,41,46,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,-25,-29,-33,-44,-45,-46,-49,68,-37,-47,-48,-26,-27,-28,-30,-31,-32,-36,-34,-35,]),'MaiorIgual':([29,33,34,35,38,39,40,41,46,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,-25,-29,-33,-44,-45,-46,-49,69,-37,-47,-48,-26,-27,-28,-30,-31,-32,-36,-34,-35,]),'Menor':([29,33,34,35,38,39,40,41,46,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,-25,-29,-33,-44,-45,-46,-49,70,-37,-47,-48,-26,-27,-28,-30,-31,-32,-36,-34,-35,]),'Maior':([29,33,34,35,38,39,40,41,46,59,60,61,76,77,78,80,81,82,83,96,116,],[-48,-25,-29,-33,-44,-45,-46,-49,71,-37,-47,-48,-26,-27,-28,-30,-31,-32,-36,-34,-35,]),'Faz':([65,72,115,],[87,94,120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Corpo':([2,],[3,]),'Declaracoes':([2,],[4,]),'Instrucoes':([4,87,94,108,120,],[6,100,101,114,122,]),'Declaracao':([4,],[7,]),'Instrucao':([6,100,101,114,122,],[9,9,9,9,9,]),'Atribuicao':([6,28,100,101,102,114,122,],[10,48,10,10,110,10,10,]),'Leitura':([6,100,101,114,122,],[11,11,11,11,11,]),'Escrita':([6,100,101,114,122,],[12,12,12,12,12,]),'Selecao':([6,100,101,114,122,],[13,13,13,13,13,]),'Repeticao':([6,100,101,114,122,],[14,14,14,14,14,]),'Expressao':([21,22,23,25,26,27,32,36,49,66,67,68,69,70,71,73,84,85,97,103,113,],[31,42,43,44,46,46,54,46,74,88,89,90,91,92,93,46,98,99,104,111,118,]),'Termo':([21,22,23,25,26,27,32,36,49,51,52,53,66,67,68,69,70,71,73,84,85,97,103,113,],[33,33,33,33,33,33,33,33,33,76,77,78,33,33,33,33,33,33,33,33,33,33,33,33,]),'Fator':([21,22,23,25,26,27,32,36,37,49,51,52,53,55,56,57,66,67,68,69,70,71,73,84,85,97,103,113,],[34,34,34,34,34,34,34,34,59,34,34,34,34,80,81,82,34,34,34,34,34,34,34,34,34,34,34,34,]),'Frase':([21,22,23,25,26,27,32,36,37,49,51,52,53,55,56,57,66,67,68,69,70,71,73,84,85,97,103,113,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'Lista_Palavras':([21,22,23,25,26,27,32,36,37,49,51,52,53,55,56,57,66,67,68,69,70,71,73,84,85,97,103,113,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'Palavra':([21,22,23,25,26,27,32,36,37,39,49,51,52,53,55,56,57,66,67,68,69,70,71,73,84,85,97,103,113,],[40,40,40,40,40,40,40,40,40,60,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'Condicao':([26,27,36,73,],[45,47,58,95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Inicio Corpo Fim','Programa',3,'p_Programa','pa.py',11),
  ('Corpo -> Declaracoes Instrucoes','Corpo',2,'p_Corpo','pa.py',18),
  ('Declaracoes -> Declaracoes Declaracao','Declaracoes',2,'p_Declaracoes','pa.py',24),
  ('Declaracoes -> <empty>','Declaracoes',0,'p_Declaracoes_Vazia','pa.py',31),
  ('Declaracao -> Tipo Var PontoVirgula','Declaracao',3,'p_Declaracao_Variavel','pa.py',37),
  ('Declaracao -> Tipo Var Expressao ParRetoDir PontoVirgula','Declaracao',5,'p_Declaracao_Array','pa.py',61),
  ('Declaracao -> Tipo Var ParRetoEsq Expressao ParRetoDir ParRetoEsq Expressao ParRetoDir PontoVirgula','Declaracao',9,'p_Declaracao_Matriz','pa.py',95),
  ('Instrucoes -> Instrucoes Instrucao','Instrucoes',2,'p_Instrucoes','pa.py',135),
  ('Instrucoes -> <empty>','Instrucoes',0,'p_Instrucoes_Vazia','pa.py',141),
  ('Instrucao -> Atribuicao','Instrucao',1,'p_Instrucao','pa.py',147),
  ('Instrucao -> Leitura','Instrucao',1,'p_Instrucao','pa.py',148),
  ('Instrucao -> Escrita','Instrucao',1,'p_Instrucao','pa.py',149),
  ('Instrucao -> Selecao','Instrucao',1,'p_Instrucao','pa.py',150),
  ('Instrucao -> Repeticao','Instrucao',1,'p_Instrucao','pa.py',151),
  ('Atribuicao -> Var Vale Expressao PontoVirgula','Atribuicao',4,'p_Atribuicao_Variavel','pa.py',157),
  ('Atribuicao -> Var ParRetoEsq Expressao ParRetoDir Vale Expressao PontoVirgula','Atribuicao',7,'p_Atribuicao_Array','pa.py',171),
  ('Atribuicao -> Var ParRetoEsq Expressao ParRetoDir ParRetoEsq Expressao ParRetoDir Vale Expressao PontoVirgula','Atribuicao',10,'p_Atribuicao_Matriz','pa.py',185),
  ('Condicao -> Expressao','Condicao',1,'p_Condicao_Expressao','pa.py',209),
  ('Condicao -> Expressao Igual Expressao','Condicao',3,'p_Condiao','pa.py',215),
  ('Condicao -> Expressao Diferente Expressao','Condicao',3,'p_Condiao','pa.py',216),
  ('Condicao -> Expressao MenorIgual Expressao','Condicao',3,'p_Condiao','pa.py',217),
  ('Condicao -> Expressao MaiorIgual Expressao','Condicao',3,'p_Condiao','pa.py',218),
  ('Condicao -> Expressao Menor Expressao','Condicao',3,'p_Condiao','pa.py',219),
  ('Condicao -> Expressao Maior Expressao','Condicao',3,'p_Condiao','pa.py',220),
  ('Expressao -> Termo','Expressao',1,'p_Expressao_Termo','pa.py',230),
  ('Expressao -> Expressao Soma Termo','Expressao',3,'p_Expressao_Soma_OU_Subtracao','pa.py',245),
  ('Expressao -> Expressao Subtracao Termo','Expressao',3,'p_Expressao_Soma_OU_Subtracao','pa.py',246),
  ('Expressao -> Expressao OU Termo','Expressao',3,'p_Expressao_Soma_OU_Subtracao','pa.py',247),
  ('Termo -> Fator','Termo',1,'p_Termo_Fator','pa.py',256),
  ('Termo -> Termo Multiplicacao Fator','Termo',3,'p_Termo_Multiplicacao_E_Divisao','pa.py',262),
  ('Termo -> Termo Divisao Fator','Termo',3,'p_Termo_Multiplicacao_E_Divisao','pa.py',263),
  ('Termo -> Termo E Fator','Termo',3,'p_Termo_Multiplicacao_E_Divisao','pa.py',264),
  ('Fator -> Frase','Fator',1,'p_Fator_Frase','pa.py',273),
  ('Fator -> Var ParRetoEsq Expressao ParRetoDir','Fator',4,'p_Fator_Array','pa.py',279),
  ('Fator -> Var ParRetoEsq Expressao ParRetoDir ParRetoEsq Expressao ParRetoDir','Fator',7,'p_Fator_Matriz','pa.py',293),
  ('Fator -> ParCurvoEsq Condicao ParCurvoDir','Fator',3,'p_Fator_Par_Condicao','pa.py',308),
  ('Fator -> Negar Fator','Fator',2,'p_Negar_Fator','pa.py',314),
  ('Leitura -> Ler PontoVirgula','Leitura',2,'p_Leitura','pa.py',320),
  ('Escrita -> Escrever ParCurvoEsq Expressao ParCurvoDir PontoVirgula','Escrita',5,'p_Escrita','pa.py',326),
  ('Selecao -> Se ParCurvoEsq Condicao ParCurvoDir Faz Instrucoes PontoVirgula','Selecao',7,'p_Selecao_Se_Faz','pa.py',338),
  ('Selecao -> Se ParCurvoEsq Condicao ParCurvoDir Faz Instrucoes Senao Instrucoes PontoVirgula','Selecao',9,'p_Selecao_Se_Faz_Senao','pa.py',346),
  ('Repeticao -> Enquanto ParCurvoEsq Condicao ParCurvoDir Faz Instrucoes PontoVirgula','Repeticao',7,'p_Repeticao_Enquanto','pa.py',354),
  ('Repeticao -> Para ParCurvoEsq Atribuicao PontoVirgula Condicao PontoVirgula Atribuicao ParCurvoDir Faz Instrucoes PontoVirgula','Repeticao',11,'p_Repeticao_Para','pa.py',364),
  ('Frase -> String','Frase',1,'p_Frase_String','pa.py',376),
  ('Frase -> Lista_Palavras','Frase',1,'p_Frase_Lista_Palavras','pa.py',382),
  ('Lista_Palavras -> Palavra','Lista_Palavras',1,'p_Lista_Palavras_Palavra','pa.py',388),
  ('Lista_Palavras -> Lista_Palavras Palavra','Lista_Palavras',2,'p_Lista_Palavras','pa.py',394),
  ('Palavra -> Var','Palavra',1,'p_Palavra_Variavel','pa.py',400),
  ('Palavra -> Num','Palavra',1,'p_Palavra_Num','pa.py',409),
]
