# Sobre o Conjunto de Dados

## Informações sobre o Conjunto de Dados
Este conjunto de dados é da Open Source Mental Illness (OSMI) e usa dados de pesquisas realizadas nos anos de 2014, 2016, 2017, 2018 e 2019. Cada pesquisa mede as atitudes em relação à saúde mental e a frequência de transtornos mentais no ambiente de trabalho da tecnologia.

Os dados brutos foram processados utilizando Python, SQL e Excel para limpeza e manipulação.

### Etapas envolvidas na limpeza dos dados:
- Perguntas similares foram agrupadas.
- Os valores das respostas foram tornados consistentes (ex: 1 == 1.0).
- Correção de erros ortográficos.

## Conteúdo
O banco de dados SQLite contém 3 tabelas: **Survey**, **Question**, e **Answer**.

### Tabelas:
- **Survey**
  - **SurveyID** (Chave Primária INT): Representa o ano da pesquisa (ex: 2014, 2016, 2017, 2018, 2019).
  - **Description** (TEXT): Descrição da pesquisa.
  
- **Question**
  - **QuestionID** (Chave Primária INT): ID da pergunta.
  - **QuestionText** (TEXT): Texto da pergunta.

- **Answer**
  - **SurveyID** (Chave Primária/Chave Estrangeira INT): Relacionado com a tabela Survey.
  - **UserID** (Chave Primária INT): ID do usuário.
  - **QuestionID** (Chave Primária/Chave Estrangeira INT): Relacionado com a tabela Question.
  - **AnswerText** (TEXT): Texto da resposta.

### Observações:
- **SurveyID** corresponde ao ano da pesquisa, como 2014, 2016, 2017, 2018, 2019.
- A mesma pergunta pode ser utilizada em múltiplas pesquisas.
- A tabela **Answer** é uma tabela composta, com múltiplas chaves primárias. **SurveyID** e **QuestionID** são chaves estrangeiras.
- Algumas perguntas podem ter múltiplas respostas, portanto o mesmo usuário pode aparecer mais de uma vez para o mesmo **QuestionID**.
