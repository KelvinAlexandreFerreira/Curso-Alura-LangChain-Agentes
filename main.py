import pandas as pd
from langchain.tools import BaseTool
from gemini_setup import get_gemini_llm
from fabrica_prompts import criar_prompt_analise_nome

class DadosDeEstudante(BaseTool):
    name: str = "DadosDeEstudante"
    description: str = "Esta ferramenta extrai o histórico e preferências de um estudante de acordo com o seu histórico"

    def _run(self, input: str) -> str:
        """
        Método interno de execução da ferramenta.
        O LangChain chama este método quando o agente decide usar a ferramenta.
        """
        
        # 1. Configuração (Pega as peças da fábrica)
        llm = get_gemini_llm()
        prompt, parser = criar_prompt_analise_nome()

        # 2. Monta a Chain (LCEL - LangChain Expression Language)
        # É como um Pipe: Prompt -> LLM -> Parser
        chain = prompt | llm | parser

        # 3. Executa a extração do nome
        try:
            # O invoke processa a pergunta (input) e retorna o JSON estruturado
            resposta_json = chain.invoke({"input": input})
            nome_estudante = resposta_json.get("estudante")
            
            if not nome_estudante:
                return "Não consegui identificar o nome do estudante na sua pergunta."
                
        except Exception as e:
            return f"Erro ao processar o nome com a IA: {e}"

        # 4. Busca os dados no CSV (Simulando uma consulta SQL)
        try:
            # Ajuste o caminho se necessário (ex: 'documentos/estudantes.csv')
            caminho_csv = "documentos/estudantes.csv" 
            
            df = pd.read_csv(caminho_csv)
            
            # Converte para minúsculo para garantir o match (ana == ana)
            # Supondo que a coluna no CSV seja 'USUARIO'
            dados = df[df['USUARIO'].str.lower() == nome_estudante.lower()]

            if dados.empty:
                return f"O estudante '{nome_estudante}' não foi encontrado na base de dados."
            
            # Retorna os dados encontrados em formato de texto/json
            return dados.to_json(orient="records", force_ascii=False)

        except FileNotFoundError:
            return f"Erro crítico: O arquivo {caminho_csv} não foi encontrado."
        except Exception as e:
            return f"Erro ao ler o CSV: {e}"

# --- Bloco de Teste Rápido (Igual ao 'project1.dpr') ---
if __name__ == "__main__":
    ferramenta = DadosDeEstudante()
    pergunta = "Quais os dados da Ana?"
    
    print(f"🤖 Pergunta: {pergunta}")
    print("⏳ Processando...")
    
    resultado = ferramenta.run(pergunta)
    
    print(f"✅ Resultado:\n{resultado}")