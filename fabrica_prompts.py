from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


from modelos import ExtratorDeEstudante
from prompts_constants import TEMPLATE_ANALISE_NOME

def criar_prompt_analise_nome():
    
    # 1. Instancia o parser baseada no modelo Pydantic
    parser = JsonOutputParser(pydantic_object=ExtratorDeEstudante)

    # 2. Injeta as instruções do parser dentro do template
    prompt = PromptTemplate(
        input_variables=["input"], 
        partial_variables={"formato_saida": parser.get_format_instructions()},
        template=TEMPLATE_ANALISE_NOME
    )

    return prompt, parser