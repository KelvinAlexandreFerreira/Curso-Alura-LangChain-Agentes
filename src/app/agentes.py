from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from src.config.gemini_setup import get_gemini_llm
from src.app.ferramentas_estudantes import DadosDeEstudante, PerfilAcademico
from src.app.ferramentas_universidade import DadosDeUniversidade, DadosDasUniversidades
from src.domain.prompts_constants import INSTRUCOES_PERSONA

class Agente:
    def __init__(self):
        """
        Construtor da classe Agente.
        Inicializa o modelo, as ferramentas e o executor.
        """
        print("🤖 Inicializando o Agente Gemini...")
        
        # 1. Instancia o LLM (Gemini)
        self.llm = get_gemini_llm()
        
        # 2. Define as ferramentas disponíveis para o agente
        # Aqui podemos adicionar mais ferramentas no futuro (ex: DadosDeUniversidade)
        self.tools = [DadosDeEstudante(), 
                      PerfilAcademico(), 
                      DadosDeUniversidade(), 
                      DadosDasUniversidades()]
        
        # 3. Puxa o prompt padrão de ReAct da comunidade LangChain
        # Este prompt ensina o modelo a "Pensar, Agir, Observar"
        self.prompt = hub.pull("hwchase17/react")

        # Usamos a constante importada de src.domain.prompts_constants
        self.prompt.template = INSTRUCOES_PERSONA + self.prompt.template
        
        # 4. Cria a estrutura do agente ReAct
        self.agente = create_react_agent(self.llm, self.tools, self.prompt)
        
        # 5. Cria o executor (quem efetivamente roda o loop de raciocínio)
        self.executor = AgentExecutor(
            agent=self.agente, 
            tools=self.tools, 
            verbose=True,            # Mostra o "pensamento" no console (Log)
            handle_parsing_errors=True # Tenta corrigir erros se a LLM formatar mal a resposta
        )

    def run(self, pergunta: str):
        """
        Método público para interagir com o agente.
        Recebe uma pergunta e retorna a resposta processada.
        """
        # O invoke dispara o processo do agente
        return self.executor.invoke({"input": pergunta})