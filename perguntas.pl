% Perguntas para rodar no SWISH (https://swish.swi-prolog.org/)
% Cole o base.pl na aba Program e cada consulta abaixo na aba Query.


% Pergunta 1 - Classificacao do Mundial de Pilotos
% (agregacao por piloto + ordenacao)

?- classificacao_pilotos(Tabela).


% Pergunta 2 - Classificacao do Mundial de Construtores
% (agregacao por equipe + ordenacao)

?- classificacao_construtores(Tabela).


% Pergunta 3 - Em qual corrida teve a maior recuperacao
% do grid ate a chegada, e quem foi o piloto?

?- maior_recuperacao(Piloto, GP, N).


% Pergunta 4 - Ranking dos pilotos que venceram pelo menos uma corrida

?- setof(N-P, (piloto(P), total_vitorias(P, N), N > 0), L),
   reverse(L, Ranking).


% Perguntas simples:

% Quem venceu o GP da Espanha?
?- vitoria(Piloto, espanha).

% Todos os podios da Ferrari:
?- resultado(GP, Piloto, ferrari, _, Pos, _, _), Pos =< 3.
