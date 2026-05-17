# 💧 HydratePlus (CLI)

## 📌 Descrição do Projeto

O **HydratePlus** é uma aplicação simples em linha de comando (CLI) desenvolvida em Python com o objetivo de ajudar usuários a monitorar e melhorar seus hábitos de hidratação diária.

A aplicação permite registrar o consumo de água, definir metas diárias e acompanhar o progresso de forma prática e rápida.

---

## 🎯 Problema Real

Muitas pessoas esquecem de beber água ao longo do dia, especialmente estudantes e profissionais que passam longos períodos focados em atividades no computador. Isso pode causar desidratação, fadiga e queda de desempenho.

---

## 💡 Solução Proposta

O HydratePlus oferece uma forma simples de:

* registrar o consumo de água 💧
* definir metas diárias
* acompanhar o progresso em tempo real

Tudo isso por meio de uma interface leve e acessível via terminal.

---

## 🌤️ Integração com API Pública

O projeto agora possui integração com a API pública **Open-Meteo**, permitindo consultar a temperatura atual em tempo real.

Com base nas condições climáticas, o sistema fornece recomendações adicionais de hidratação para o usuário, tornando a aplicação mais dinâmica e contextualizada.

Exemplo:

* Dias muito quentes → reforço na hidratação 🔥
* Temperaturas amenas → manutenção da meta diária 💧

---

## 👥 Público-Alvo

* Estudantes
* Profissionais que trabalham em frente ao computador
* Pessoas que desejam melhorar hábitos de saúde

---

## ⚙️ Funcionalidades

* ✅ Adicionar consumo de água (em ml)
* ✅ Definir meta diária
* ✅ Visualizar progresso atual
* ✅ Validação de entradas inválidas
* ✅ Consulta de temperatura em tempo real via API pública
* ✅ Recomendação de hidratação baseada no clima
* ✅ Testes automatizados de integração

---

## 🛠️ Tecnologias Utilizadas

* Python 3.11
* Pytest (testes automatizados)
* Ruff (linting/análise estática)
* Requests (consumo de API HTTP)
* Open-Meteo API
* Git e GitHub
* GitHub Actions (CI)

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/lucasfrigato4/HYDRATEPLUS.git
cd HydratePlus
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Execução da Aplicação

```bash
python -m src.app
```

---

## 🧪 Executar Testes

```bash
python -m pytest
```

Os testes automatizados incluem:

* Testes unitários
* Teste de integração com mock da API Open-Meteo

---

## 🧹 Executar Lint

```bash
python -m ruff check .
```

---

## 🔢 Versionamento

Este projeto segue versionamento semântico:

**Versão atual:** `1.0.0`

---

## 📁 Estrutura do Projeto

```text
HydratePlus/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── app.py
│   ├── storage.py
│   └── weather.py
├── tests/
│   ├── test_app.py
│   └── test_weather.py
├── .gitignore
├── data.json
├── README.md
├── requirements.txt
├── VERSION
```

---

## 👨‍💻 Autor

Lucas Frigato

---

## 🔗 Repositório

https://github.com/lucasfrigato4/HYDRATEPLUS.git
---
