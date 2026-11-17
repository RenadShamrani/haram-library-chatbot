# Haram Library Chatbot

> Academic / COOP prototype. Additional setup and local model training are required to run locally. This repository is not a production deployment.

An Arabic-English FAQ chatbot co-developed during COOP training at Haram Library. The project combines Rasa dialogue handling, custom FAQ actions, and a FastAPI web interface.

## Project overview

- Bilingual FAQ responses about library services.
- A lightweight web interface with response notifications.
- A Rasa training workflow built around 28 visitor FAQs.
- Python, Rasa, FastAPI, spaCy, aiohttp, and Uvicorn.

The repository presents a training project, not an official live library service. FAQ content reflects the project material and should not be treated as verified current library policy.

## My Contribution

My work during COOP training included:

- Co-developing the Arabic-English chatbot using Python, Rasa, and FastAPI.
- Training the chatbot on 28 visitor FAQs and refining intents, entities, and dialogue flows with domain experts.
- Integrating the chatbot backend with a lightweight web interface, including response display and sound notifications.

This was collaborative work. Both project authors are credited below.

## Architecture

```text
Browser -> FastAPI web app (:8000)
        -> Rasa REST webhook (:5005)
        -> Custom actions server (:5055)
```

All three services must run for the complete local FAQ workflow. The action endpoint is configured in `endpoints.yml`; the web app calls the Rasa REST webhook from `app.py`.

## Local setup

The project targets Python 3.10.18 and Rasa 3.6.21. Use a separate environment and run commands from the repository root.

Install the repository dependencies:

```bash
pip install -r requirements.txt
python -m spacy download xx_ent_wiki_sm
```

Train the local Rasa model:

```bash
rasa train
```

After training, keep the following commands running in three separate terminals, using the same environment and repository root.

### Rasa server

```bash
rasa run --port 5005
```

### Custom actions server

```bash
rasa run actions --port 5055
```

### FastAPI web interface

```bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

Open [the local web interface](http://localhost:8000).

These instructions describe the intended source-based workflow, not a clean-environment, end-to-end reproducibility guarantee. No trained Rasa model is bundled in this checkout, and dependency compatibility still needs validation in the target environment.

## Repository guide

| Path | Purpose |
| :--- | :--- |
| `app.py` | FastAPI routes and browser interface |
| `actions/actions.py` | Bilingual custom FAQ actions |
| `config.yml` | Rasa pipeline and policies |
| `domain.yml` | Intents and registered actions |
| `data/` | NLU examples, rules, and dialogue stories |
| `endpoints.yml` | Custom actions endpoint |
| `credentials.yml` | Rasa channel configuration |
| `static/` | Logo and notification audio |
| `tests/` | Existing conversation test files |

## Scope and limitations

This prototype is intended for isolated local demonstration and learning, not public production deployment. Further testing and security hardening are required before multi-user use.

No fully validated deployment or independently verified chatbot accuracy score is claimed.

## Authors

- Renad Alshamrani
- Sarah Alshamrani

## Acknowledgment

Thanks to Haram Library for the support, guidance, and project material provided during COOP training.
