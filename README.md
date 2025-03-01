<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->







<!-- PROJECT LOGO --> <br /> <div align="center"> <a href="https://github.com/your_username/repo_name"> <img src="images/logo.png" alt="Logo" width="80" height="80"> </a> <h3 align="center">Transcrição de Áudio/Vídeo com Segmentação de Falantes</h3> <p align="center"> Uma aplicação de transcrição de áudio/vídeo com segmentação de falantes, usando uma arquitetura de microserviços com Streamlit, FastAPI, Whisper, Pyannote e Docker. <br /> <a href="https://github.com/your_username/repo_name"><strong>Explore the docs »</strong></a> <br /> <br /> <a href="https://github.com/your_username/repo_name">View Demo</a> · <a href="https://github.com/your_username/repo_name/issues">Report Bug</a> · <a href="https://github.com/your_username/repo_name/issues">Request Feature</a> </p> </div> <!-- TABLE OF CONTENTS --> <details> <summary>Table of Contents</summary> <ol> <li> <a href="#about-the-project">About The Project</a> <ul> <li><a href="#built-with">Built With</a></li> </ul> </li> <li> <a href="#getting-started">Getting Started</a> <ul> <li><a href="#prerequisites">Prerequisites</a></li> <li><a href="#installation">Installation</a></li> </ul> </li> <li><a href="#usage">Usage</a></li> <li><a href="#roadmap">Roadmap</a></li> <li><a href="#contributing">Contributing</a></li> <li><a href="#license">License</a></li> <li><a href="#contact">Contact</a></li> <li><a href="#acknowledgments">Acknowledgments</a></li> </ol> </details> <!-- ABOUT THE PROJECT -->
About The Project


Esta aplicação permite aos usuários fazer upload de arquivos de áudio ou vídeo, convertê-los para o formato .wav, transcrevê-los usando o modelo Whisper da OpenAI e, opcionalmente, segmentar os falantes usando o Pyannote. Construída com uma arquitetura de microserviços, ela separa a lógica de transcrição e diarização em serviços distintos, utilizando FastAPI para os endpoints e Streamlit para uma interface de usuário intuitiva. O Docker é usado para conteinerização, garantindo facilidade de deployment e escalabilidade.

Por que este projeto?

Fornece uma solução modular e escalável para transcrição de áudio/vídeo com segmentação de falantes.
Facilita a integração de novas funcionalidades graças à arquitetura de microserviços.
Oferece uma interface simples e acessível para usuários finais.
Este projeto é ideal para quem busca uma ferramenta robusta para transcrição e análise de áudio/vídeo, com suporte a múltiplos falantes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
Built With
Aqui estão as principais tecnologias utilizadas no projeto:

- Interface de usuário interativa.
- Backend para serviços de transcrição e diarização.
- Modelo de transcrição de áudio da OpenAI.
- Segmentação de falantes.
- Conteinerização e deployment.
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- GETTING STARTED -->
Getting Started
Siga estas instruções para configurar o projeto localmente e começar a usá-lo.

Prerequisites
Você precisará dos seguintes itens instalados:

Docker: Necessário para construir e executar os containers. Baixe aqui.
Conta no Hugging Face: Para acessar o modelo Pyannote, crie uma conta e gere um token de API em Hugging Face.
Installation
Clone o repositório
sh
Encapsular
Copiar
git clone https://github.com/your_username/repo_name.git
Navegue até o diretório do projeto
sh
Encapsular
Copiar
cd repo_name
Configure o token do Hugging Face
Crie um arquivo .env na raiz do projeto.
Adicione o seguinte conteúdo, substituindo seu_token_aqui pelo seu token da Hugging Face:
text
Encapsular
Copiar
HF_TOKEN=seu_token_aqui
Construa e inicie os containers
sh
Encapsular
Copiar
docker-compose up --build
Acesse a interface
Abra seu navegador e vá para http://localhost:8501.
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- USAGE EXAMPLES -->
Usage
Para usar a aplicação:

Faça upload de um arquivo de áudio (.mp3, .wav) ou vídeo (.mp4) diretamente na interface Streamlit.
Marque a opção "Incluir segmentação de falantes" se desejar identificar quem fala e quando.
Visualize a transcrição resultante na tela.
Exemplo de saída com segmentação de falantes:

text
Encapsular
Copiar
Speaker 1 (0.0s - 5.0s): Olá, como você está?
Speaker 2 (5.0s - 10.0s): Estou bem, obrigado!
Para mais detalhes, consulte a documentação do projeto.

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- ROADMAP -->
Roadmap
 Implementar transcrição com Whisper.
 Adicionar segmentação de falantes com Pyannote.
 Suporte a mais formatos de arquivo (.ogg, .flac).
 Opção para baixar a transcrição em um arquivo de texto.
 Melhorias na interface, como suporte a múltiplos idiomas.
Veja as issues abertas para uma lista completa de funcionalidades propostas e problemas conhecidos.

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- CONTRIBUTING -->
Contributing
Contribuições são o que tornam a comunidade open source um lugar incrível para aprender, inspirar e criar. Qualquer contribuição é muito bem-vinda.

Se você tem uma sugestão para melhorar o projeto:

Faça um fork do repositório.
Crie um branch para sua feature (git checkout -b feature/SuporteAudioOgg).
Commit suas alterações (git commit -m 'Adiciona suporte a arquivos .ogg').
Push para o branch (git push origin feature/SuporteAudioOgg).
Abra um Pull Request.
Não se esqueça de dar uma estrela ao projeto! Obrigado!

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- LICENSE -->
License
Distribuído sob a licença MIT. Veja LICENSE.txt para mais informações.

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- CONTACT -->
Contact
Nome do Desenvolvedor - @your_twitter - email@example.com

Link do Projeto: https://github.com/your_username/repo_name

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- ACKNOWLEDGMENTS -->
Acknowledgments
Aqui estão alguns recursos e ferramentas que ajudaram a tornar este projeto possível:

Streamlit
FastAPI
Whisper
Pyannote
Docker
Choose an Open Source License
GitHub Emoji Cheat Sheet
Img Shields
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- MARKDOWN LINKS & IMAGES -->
Notas
Substitua your_username e repo_name pelos valores reais do seu repositório GitHub.
Adicione uma imagem da interface Streamlit em images/screenshot.png para exibir um screenshot funcional.
Atualize as informações de contato na seção "Contact" com seu nome, Twitter, email e perfil do LinkedIn, se aplicável.
Certifique-se de que o arquivo LICENSE.txt esteja no repositório com a licença MIT.