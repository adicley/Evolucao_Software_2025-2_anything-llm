# Evolucao_Software_2025-2_anything-llm

## Objetivo

A atividade 1 consiste em extrair os comentários das 100 pull requests consecutivas de um projeto bem-sucedidos do github, no caso da equipe 3, o projeto escolhido foi [anything-llm](https://github.com/Mintplex-Labs/anything-llm), e, com os dados colatados na extração das pull requests, realizar a análise de sentimentos de todos os comentários utilizandos três LLM's de classificação de texto disponibilizados no portal [Hugging Face](https://huggingface.co/models?language=en&sort=trending&search=sentiment).

## Requisitos de Hardware

O projeto foi executado no ambiente de núvem do Google Colab com:
- GPU: T4 15GB VRAM
- RAM do sistema: 12.77GB
- Disco: 112GB

## Instruções para execução da atividade

1. Clone o repositório e instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
1. Inclua seu token do Github no script `extract_github_pr_comments.py` para extração das 100 pull requests consecutivas:
   ```ini
   GITHUB_TOKEN = my_github_token
   ```
3. Salve as alterações e execute o script:
   ```bash
   python extract_github_pr_comments.py
   ```
4. Após finalizar a execução, os comentários extraídos ficarão salvos no arquivo `pr_comments.json` na pasta `extractions/`.
5. A partir disso, basta abrir o notebook `main.ipynb` disponibilizado no repositório e executar as células, em ordem, para a criação do arquivo de classificação dos comentários das PR's e geração dos gráficos no notebook contendo os resumos da análise de sentimentos de cada modelo.
6. Ao final, os comentários classificados estarão salvos no arquivo `pr_comments_classified.json` na pasta `classifications/`.

## Modelo Utilizados

1. O primeiro modelo de classificação de texto escolhido foi o [clapAI/modernBERT-large-multilingual-sentiment](https://huggingface.co/clapAI/modernBERT-large-multilingual-sentiment), um modelo large com 400M de parâmetros, janela de contexto de 8.192K de tokens, o qual passou por um ajuste fino utilizando o dataset [clapAI/MultiLingualSentiment](https://huggingface.co/datasets/clapAI/MultiLingualSentiment).
2. O segundo modelo foi o [lxyuan/distilbert-base-multilingual-cased-sentiments-student](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student), um modelo base com 100M de parâmetros, janela de contexto de 512 tokens que passou por um ajuste fino ao ser treinado com o dataset [tyqiangz/multilingual-sentiments](https://huggingface.co/datasets/tyqiangz/multilingual-sentiments).
3. O terceiro modelo foi o [clapAI/roberta-large-multilingual-sentiment](https://huggingface.co/clapAI/roberta-large-multilingual-sentiment), um modelo large com 600M de parâmetros, janela de contexto de 514 tokens que passou por um ajuste fino utilizando o mesmo dataset do primeiro modelo desta lista.
