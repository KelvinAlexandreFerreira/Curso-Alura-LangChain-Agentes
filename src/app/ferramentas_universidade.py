import pandas as pd
import os
from langchain.tools import BaseTool
from src.config.gemini_setup import get_gemini_llm
from src.services.fabrica_prompts import criar_prompt_analise_universidade

class DadosDeUniversidade(BaseTool):
    name: str = "DadosDeUniversidade"
    description: str = """Esta ferramenta busca informações detalhadas sobre UMA universidade específica (critérios, cursos, perfil).
    Útil para saber o que uma faculdade exige ou oferece.
    Se precisar comparar universidades, chame esta ferramenta uma vez para cada instituição."""

    def _run(self, input: str) -> str:
        # 1. Configuração
        llm = get_gemini_llm()
        prompt, parser = criar_prompt_analise_universidade()
        chain = prompt | llm | parser

        # 2. Executa a extração do nome da universidade
        try:
            resposta_json = chain.invoke({"input": input})
            nome_universidade = resposta_json.get("universidade")
            
            if not nome_universidade:
                return "Não consegui identificar o nome da universidade na sua pergunta."
                
        except Exception as e:
            return f"Erro ao processar o nome da universidade com a IA: {e}"

        # 3. Busca os dados no CSV
        try:
            caminho_csv = os.path.join("documentos", "universidades.csv")
            
            df = pd.read_csv(caminho_csv)
            
            # Busca flexível (contém o texto), ignorando maiúsculas/minúsculas
            # A coluna no CSV é 'NOME_FACULDADE'
            dados = df[df['NOME_FACULDADE'].str.lower().str.contains(nome_universidade.lower(), na=False)]

            if dados.empty:
                return f"A universidade '{nome_universidade}' não foi encontrada na base de dados."
            
            return dados.to_json(orient="records", force_ascii=False)

        except FileNotFoundError:
            return f"Erro crítico: O arquivo {caminho_csv} não foi encontrado."
        except Exception as e:
            return f"Erro ao ler o CSV de universidades: {e}"
        
class DadosDasUniversidades(BaseTool):
    name: str = "DadosDasUniversidades"
    description: str = """Esta ferramenta retorna a lista de TODAS as universidades disponíveis no banco de dados.
    Use esta ferramenta quando a pergunta for genérica, como 'Quais universidades estão disponíveis?' ou 'Quais universidades oferecem curso de Medicina?' sem especificar um nome."""

    def _run(self, input: str) -> str:
        try:
            caminho_csv = os.path.join("documentos", "universidades.csv")
            df = pd.read_csv(caminho_csv)
            
            # Retorna apenas as colunas essenciais para não estourar o contexto se a lista for grande
            # Mas como o CSV é pequeno, podemos retornar tudo ou filtrar
            # Aqui vou retornar tudo para facilitar a análise do agente
            return df.to_json(orient="records", force_ascii=False)

        except FileNotFoundError:
            return f"Erro crítico: O arquivo {caminho_csv} não foi encontrado."
        except Exception as e:
            return f"Erro ao ler o CSV de universidades: {e}"