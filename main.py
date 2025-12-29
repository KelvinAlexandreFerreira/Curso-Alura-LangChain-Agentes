import sys
import os
import warnings

# Suprime avisos técnicos que poluem o console (Pydantic V1, Google Deprecation, etc)
warnings.filterwarnings("ignore")

# Adiciona o diretório atual ao path
sys.path.append(os.getcwd())

from src.app.agentes import Agente

# Ponto de entrada da aplicação
if __name__ == "__main__":
    
    # 1. Instanciação da classe Agente (abstraindo a complexidade de criação)
    agente = Agente()
    
    # Pergunta de teste
    pergunta = "Quais os dados da Ana?"
    pergunta = "Quais os dados da Bianca?"
    pergunta = "Quais os dados da Ana e da Bianca?"
    pergunta = "Crie um perfil acadêmico para a Ana!"
    pergunta = "Compare o perfil acadêmico da Ana e da Bianca!"
    pergunta = "Tenho sentido Ana desanimada com cursos de matemática. Seria uma boa parear ela com a Bianca?"
    pergunta = "Tenho sentido Ana desanimada com cursos de matemática. Seria uma boa parear ela com o Marcos?"
    pergunta = "Quais os dados da USP?"
    pergunta = "Quais os dados da uNiCAmP?"
    pergunta = "Quais os dados da uNi CAmP?"
    pergunta = "Quais os dados da uNiComP?"
    pergunta = "Entre USP e UFRJ, qual você recomenda para a acadêmica Ana?"
    pergunta = "Entre uni camp e USP, qual você recomenda para a Ana?"
    pergunta = "Quais as faculdades com melhores chances para a Ana?"
    pergunta = "Dentre todas as faculdades existentes, quais Ana possui mais chances de entrar?"
    pergunta = "Além das faculdades que a Ana já conhece, quais Ana possui mais chances de entrar?"

    print(f"\n🤖 Pergunta: {pergunta}")
    print("⏳ Processando...")
    
    # 2. Execução através do método público
    resultado = agente.run(pergunta)
    
    # 3. Exibição do resultado final
    print(f"\n✅ Resultado Final:\n{resultado.get('output')}")