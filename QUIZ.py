#==================================================================
#INSTITUIÇÃO:Colégio Estadual Jardim Oriente(CEJO)/SENAI
#CURSO:Técnico em desenvolvimento de Sistema
#ESTUDANTE:Italo Brian Vieira Tavares
#TURMA:1ºA(Matutino)/1ºB(Vespertino)
#DATA:06/10/2026
#UC:Lógica de programação |/Programação de app|
#DESCRIÇÃO:MINI QUIZ DE TECNOLOGIA
#==================================================================
#================================================
#DESAFIOS DEV: MINI QUIZ DE TECNOLOGIA
#================================================

print("=== BEM-VINDO AO QUIZ TECH CEJO/SENAI ===")
nome = input("Digite seu nome: ")
print(f"\nOlá, {nome}!Responda as perguntas com A, B OU C:\n")

pontuacao = 0
# === PERGUNTAS 1 ===
print("1) Qual linguagem estamos aprendendo nesta aula?")
print("A)HTML")
print("B)Python")
print("C)C++")
resposta1 = input("Sua resposta: ").upper()
if resposta1 == "B":
    print("✅ Resposta correta +1 ponto./n")
    pontuacao = pontuacao +1
else:
# === PERGUNTAS 2 ===
print("2)O que significa a sigla SGBD em Banco de Dados?")
print("A)Sistema de Gerenciamento de Banco de Dados")
print("B)Sistema Geral de Busca Digital")
print("C)Software de Gravação de Baixo Desempenho")
resposta2 = input("Sua resposta: ").upper()
if resposta2 == "A":
    print("✅ Resposta correta +1 ponto./n")
    pontuacao = pontuacao +1
else:
    print("❌Resposta Incorreta. A certa era A\n")
# === PERGUNTAS 3 ===
print("1)Qual comando em Python é usado para exibir mensagens na tela?")
print("A)Impud()")
print("B)print()")
print("C)import()")
resposta3 = input("Sua resposta: ").upper()
if resposta3 == "B":
    print("✅ Resposta correta +1 ponto./n")
    pontuacao = pontuacao +1
else:
    print("❌Resposta Incorreta. A certa era B (print).\n")
# === RESULTADO FINAL ===
print("===============================================================")
print(|"Fim do Quiz, {nome}!")
primt(|"Sua pontuação final foi:(pontuacao) do 3 pontos.")
if pontuacao == 3:
    print("🏆 Excelente! Você acertou tudo!")
elif pontuacao >= 1:
    print("👍 Bom trabalho! Dá para melhorar revisando o conteúdo.")
else
    print("😅 Precisa estudar mais um pouquinho!")
print("===============================================================")

