import os
import requests as rq
import json as js
import threading as th

#Quantidades de pull requests que serao requisitadas;
PR_SIZE = 100
#Auth token do git;
GITHUB_TOKEN = "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"
#Quantidade de cores logicos disponiveis para realizar requisicoes http em paralelo;
LOGIC_CORES = os.cpu_count()

def get_comments(id, list_comments, request_url, headers):
    comment_json = list_comments[id]
    pr_comments = get_request(request_url, headers)

    for i in range(len(pr_comments)):
        pr_comment = pr_comments[i]
        comment_template = { 
            'login': pr_comment['user']['login'],
            'author_association': pr_comment['author_association'], 
            'comment': pr_comment['body'] 
        }
        comment_json['comments'].append(comment_template)

def get_request(request_url, headers):
    try:
        request_resp = rq.get(request_url, headers=headers)
        request_resp.raise_for_status()
        return request_resp.json()
    except rq.exceptions.RequestException as ex:
        print(f"Request Exception: {ex}")
        return []
    
def get_pull_requests(owner, repo_name, headers, query):
    request_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls?{query}"
    return get_request(request_url, headers)

def get_pr_comments(pr_numbers, owner, repo_name, headers):
    threads = []
    list_comments = []
    pr_len = len(pr_numbers)
    
    #Cria o vetor com o template para os comentarios;
    for i in range(pr_len):
        pr_number = pr_numbers[i]['number']
        comment_json = {'pr_id': pr_number, 'comments': []}
        list_comments.append(comment_json)

    #Realiza as requests para resgatar os comentarios das ultimas pull requests do repositorio;
    for i in range(pr_len):
        request_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{list_comments[i]['pr_id']}/comments"
        thread = th.Thread(target=get_comments, args=(i, list_comments, request_url, headers))
        threads.append(thread)
        thread.start()

        #Impede que sejam geradas mais threads que a capacidade total de nucleos na maquina evitando, assim, gargalos
        #E impede que gere sucessivas requests que passem do limite maximo, evitando bloqueios por parte da API Rest;
        if i % LOGIC_CORES == 0:
            for j in range(i, len(threads)):
                threads[j].join()

    #Espera ate que todas as threads estejam finalizadas;
    for thread in threads:
        thread.join()

    return list_comments

if __name__ == "__main__":
    headers = {"Authorization" : f"token {GITHUB_TOKEN}"}
    query = f"state=closed&per_page={PR_SIZE}"
    owner = "Mintplex-Labs"
    repo_name = "anything-llm"

    pull_requests = get_pull_requests(owner, repo_name, headers, query)
    list_comments = get_pr_comments(pull_requests, owner, repo_name, headers)

    with open('pr_comments.json', 'w') as f:
        js.dump(list_comments, f, indent=4)