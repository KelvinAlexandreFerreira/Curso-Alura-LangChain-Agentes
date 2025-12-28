# --- Template para análise de nome ---
TEMPLATE_ANALISE_NOME = """Você deve analisar a {input} e extrair o nome de usuário informado.
Formato de saída:
{formato_saida}"""

TEMPLATE_PERFIL_ACADEMICO = """- Fotmate o estudante para seu perfil acadêmico
- Com os dados, identifique as opções de universidades sugeridas e cursos compatíveis com o interesse do aluno
- Destaque o perfil do aluno dando ênfase  principalmente naquilo que faz sentido para as instituições de interesse do aluno

Persona: Você é uma consultora de carreira e precisa indicar com detalhes, riqueza , mas direta ao ponto para o estudante e consequências possíveis.
Informações atuais:

{dados_do_estudante}
{formato_saida}
"""