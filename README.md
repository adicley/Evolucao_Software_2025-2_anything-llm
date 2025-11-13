# Evolucao_Software_2025-2_anything-llm

## Objetivos

A atividade 1 consiste em extrair os comentários das 100 pull requests consecutivas de um projeto bem-sucedidos do github, no caso da equipe 3, o projeto escolhido foi [anything-llm](https://github.com/Mintplex-Labs/anything-llm), e, com os dados colatados na extração das pull requests, realizar a análise de sentimentos de todos os comentários utilizandos três LLM's de classificação de texto disponibilizados no portal [Hugging Face](https://huggingface.co/models?language=en&sort=trending&search=sentiment).

## Instruções para execução da atividade

1. Instale a dependência:
   ```bash
   pip install requests
   ```
1. Inclua seu token do Github no script `extract_github_pr_comments.py` disponibilizado na pasta `script/` no campo:
   ```bash
   GITHUB_TOKEN = my_github_token
   ```
3. Após isso, execute o script:
   ```bash
   python extract_github_pr_comments.py
   ```
4. Após isso, os comentários extraído ficarão salvos no arquivo `pr_comments.json` na mesma pasta que o script foi executado.
5. A partir disso, basta abrir o notebook `main.ipynb` disponibilizado no repositório e execultar as células em ordem para que seja gerado o arquivo de classificação e geração dos gráficos.
6. Ao final, os comentários classificados ficarão salvos no arquivo `pr_comments_classified.json` e os gráficos contendos os dados resumidos das classificações pelos modelos no próprio notebook disponibilizado.

## Modelos utilizados na atividade
- [clapAI/modernBERT-large-multilingual-sentiment](https://huggingface.co/clapAI/modernBERT-large-multilingual-sentiment)
- [lxyuan/distilbert-base-multilingual-cased-sentiments-student](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student)
- [clapAI/roberta-large-multilingual-sentiment](https://huggingface.co/clapAI/roberta-large-multilingual-sentiment)
