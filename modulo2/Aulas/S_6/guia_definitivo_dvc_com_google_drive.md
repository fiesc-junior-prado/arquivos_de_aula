# Guia Definitivo: Versionamento de Dados com DVC e Google Drive

Em projetos de Visão Computacional e MLOps em Python, o Git é excelente para versionar código, mas falha ao lidar com grandes volumes de imagens ou modelos pesados. A solução é usar o **DVC (Data Version Control)**.

Este guia detalha como configurar o DVC para armazenar seus dados no Google Drive, contornando bloqueios de segurança e erros de dependência.

## Passo 1: Instalação e Preparação do Ambiente

Antes de começar, certifique-se de estar com o seu ambiente virtual Python (`.venv`) ativado e de já ter rodado `git init` no seu repositório.

1. **Instale o DVC e o plugin do Google Drive:**

   ```
   pip install dvc "dvc[gdrive]"
   
   ```

2. **Prevenção de Erro (Conflito de Criptografia):**
   Para evitar o erro `module 'lib' has no attribute 'GEN_EMAIL'` (muito comum em distribuições recentes ao usar a API do Google), force a instalação de uma versão estável do `pyOpenSSL`:

   ```
   pip install "pyOpenSSL==24.2.1"
   
   ```

3. **Inicialize o DVC:**
   Na raiz do seu repositório Git, execute:

   ```
   dvc init
   git commit -m "Inicializa o DVC na raiz do projeto"
   
   ```

## Passo 2: Criando Credenciais no Google Cloud

Para evitar que o Google bloqueie o DVC com a tela *"Este app está bloqueado"*, você precisa criar suas próprias credenciais de acesso gratuitas.

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/) e crie um **Novo Projeto**.

2. No menu lateral, acesse **APIs e Serviços > Biblioteca**.

3. Pesquise por **Google Drive API** e clique em **Ativar**.

4. Acesse **APIs e Serviços > Tela de consentimento OAuth** (ou *Público-alvo*):

   * Escolha o tipo de usuário **Externo** e clique em Criar.

   * Preencha o nome do App (ex: `Meu DVC`) e seus e-mails de suporte.

   * **⚠️ PASSO CRUCIAL:** Na seção **Usuários de teste**, adicione o **seu próprio e-mail do Gmail**. Isso garante sua autorização de acesso. Salve e continue.

5. Acesse **APIs e Serviços > Credenciais** (ou *Clientes*):

   * Clique em **+ Criar Credenciais > ID do cliente OAuth**.

   * Tipo de aplicativo: Selecione **App para computador** (Desktop app).

   * Clique em Criar.

6. Copie o **ID do Cliente** e a **Chave Secreta** que aparecerão na tela.

## Passo 3: Configuração do Remote no DVC

Agora vamos conectar o DVC ao seu Google Drive usando as credenciais que você acabou de gerar.

1. No seu Google Drive, crie uma pasta para o projeto e copie o ID dela (o código longo que fica no final da URL do navegador).

2. Configure essa pasta como o armazenamento remoto padrão no terminal:

   ```
   dvc remote add -d gdrive_aulas gdrive://SEU_ID_DA_PASTA
   
   ```

3. Insira suas credenciais exclusivas geradas no Passo 2:

   ```
   dvc remote modify gdrive_aulas gdrive_client_id SEU_ID_DO_CLIENTE
   dvc remote modify gdrive_aulas gdrive_client_secret SUA_CHAVE_SECRETA
   
   ```

4. Salve essa configuração no Git:
   *(O DVC protege sua chave secreta automaticamente em um arquivo `config.local` que não vai para o GitHub).*

   ```
   git add .dvc/config
   git commit -m "Configura GDrive como remoto padrão com credenciais próprias"
   
   ```

## Passo 4: O Fluxo de Trabalho (O Dia a Dia)

Toda vez que você adicionar, processar ou deletar imagens do seu dataset, você deverá seguir este ciclo exato para manter Código (Git) e Dados (DVC) sincronizados.

**1. Avise o DVC sobre os novos dados:**

```
dvc add caminho/para/sua/pasta_de_imagens

```

*Isso fará o DVC ler as imagens, criar um arquivo `.dvc` (ponteiro) e atualizar o `.gitignore`.*

**2. Salve o ponteiro e o código no Git:**

```
git add caminho/para/sua/pasta_de_imagens.dvc
git add caminho/para/sua/pasta_de_imagens/.gitignore
git add seu_script_de_codigo.ipynb
git commit -m "Adiciona novas imagens e atualiza o notebook"

```

**3. Envie tudo para a nuvem (O "Push Duplo"):**

```
# Envia o código e os ponteiros para o GitHub
git push 

# Envia as imagens físicas para o Google Drive
dvc push

```

*Na primeira vez que rodar o `dvc push`, o terminal pausará e exibirá um link. Clique nele, faça login com a conta do Gmail que você cadastrou como testadora, copie o código de verificação e cole no terminal.*

## Resumo Rápido de Comandos

| **Situação** | **Comando** | 
| Adicionar novos dados | `dvc add <pasta/arquivo>` | 
| Enviar imagens pro Drive | `dvc push` | 
| Baixar imagens do Drive | `dvc pull` | 
| Sincronizar após um `git checkout` | `dvc checkout` | 
| Limpar imagens velhas do cache local | `dvc gc -w` | 
