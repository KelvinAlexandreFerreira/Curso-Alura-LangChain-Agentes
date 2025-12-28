from src.app.agentes import Agente

# Ponto de entrada da aplicação
if __name__ == "__main__":
    
    # 1. Instanciação da classe Agente (abstraindo a complexidade de criação)
    agente = Agente()
    
    # Pergunta de teste
    pergunta = "Quais os dados da Ana?"
    pergunta = "Quais os dados da Bianca?"
    pergunta = "Quais os dados da Ana e da Bianca?"
    
    print(f"\n🤖 Pergunta: {pergunta}")
    print("⏳ Processando...")
    
    # 2. Execução através do método público
    resultado = agente.run(pergunta)
    
    # 3. Exibição do resultado final
    print(f"\n✅ Resultado Final:\n{resultado.get('output')}")