import csv

def limpar(texto):
    # tira espacos, coloca em minusculo e troca - por _
    return texto.strip().lower().replace(" ", "_").replace("-", "_")


with open("data/f1_2023.csv", encoding="utf-8") as f:
    linhas = list(csv.DictReader(f))

with open("base.pl", "w", encoding="utf-8") as saida:
    saida.write("% Base de conhecimento - F1 2023\n")
    saida.write("% Gerada pelo etl.py\n\n")

    # fatos
    for l in linhas:
        gp = limpar(l["gp"])
        piloto = limpar(l["piloto"])
        equipe = limpar(l["equipe"])
        grid = l["grid"]
        pos = l["posicao"]
        pontos = l["pontos"]
        vmr = l["volta_mais_rapida"]
        saida.write(
            f"resultado({gp}, {piloto}, {equipe}, {grid}, {pos}, {pontos}, {vmr}).\n"
        )

    # regras
    saida.write("""
% ---------- Regras ----------

piloto(P) :- resultado(_, P, _, _, _, _, _).
equipe(E) :- resultado(_, _, E, _, _, _, _).

vitoria(Piloto, GP) :- resultado(GP, Piloto, _, _, 1, _, _).

podio(Piloto, GP) :-
    resultado(GP, Piloto, _, _, Pos, _, _),
    Pos =< 3.

total_pontos(Piloto, Total) :-
    piloto(Piloto),
    findall(P, resultado(_, Piloto, _, _, _, P, _), Lista),
    sum_list(Lista, Total).

pontos_equipe(Equipe, Total) :-
    equipe(Equipe),
    findall(P, resultado(_, _, Equipe, _, _, P, _), Lista),
    sum_list(Lista, Total).

total_vitorias(Piloto, N) :-
    piloto(Piloto),
    findall(1, vitoria(Piloto, _), L),
    length(L, N).

classificacao_pilotos(Tabela) :-
    setof(Pontos-Piloto, total_pontos(Piloto, Pontos), L),
    reverse(L, Tabela).

classificacao_construtores(Tabela) :-
    setof(Pontos-Equipe, pontos_equipe(Equipe, Pontos), L),
    reverse(L, Tabela).

maior_recuperacao(Piloto, GP, N) :-
    findall(G-P-Corrida,
            (resultado(Corrida, P, _, Grid, Pos, _, _), G is Grid - Pos),
            L),
    max_member(N-Piloto-GP, L).
""")

print(f"{len(linhas)} fatos gerados em base.pl")
