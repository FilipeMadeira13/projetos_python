import requests as rq

url = input('Escreva a URL do site: ').strip()

try:
    response = rq.get(url)
    response.raise_for_status()  # Verifica se houve erro na requisição
    html_content = response.text

    start_title = '<title>'
    end_title = '</title>'
    
    start_index = html_content.find(start_title)
    if start_index != -1:
        end_index = html_content.find(end_title, start_index)
        title = html_content[start_index + len(start_title):end_index]
        print(f'Título da página: {title.strip()}')  # Remove espaços extras
    else:
        print('Nenhum título encontrado no HTML da página.')

except rq.exceptions.RequestException as e:
    print(f'Erro ao acessar o site: {e}')
