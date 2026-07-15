# Tolveris Launchpad

Tolveris Launchpad is a financial-safety platform that helps senior citizens and financially vulnerable Filipinos use digital banking with confidence. It combines approachable banking workflows, **Ipon** savings goals, bite-sized financial-literacy lessons, and explainable scam-risk guidance before money is transferred.

> Blockchain is simulated for this hackathon starter. The architecture keeps it behind a ledger port so it can be replaced by Stellar wallets, ledger APIs, Soroban contracts, and anchors later.

## What is included

- Accessible wallet dashboard with large, clear actions
- Ipon goal tracking and deposits
- Financial-literacy modules and verifiable badge issuance
- Explainable transaction risk analysis: unfamiliar recipient, unusually large amount, and high transfer frequency
- Simulated append-only ledger, isolated behind a replaceable adapter
- FastAPI + SQLite development API and a Next.js + Tailwind web client

## Architecture

```text
apps/web             Next.js user experience
services/api         FastAPI delivery layer and use cases
  app/domain         Banking, learning, ledger, and risk business concepts
  app/infrastructure SQLite repositories and simulated ledger adapter
  app/api            HTTP request/response routes
```

The domain layer depends on interfaces (ports), rather than the database or blockchain simulation. A Stellar adapter can implement the same `LedgerPort` later.

## Quick start

### API

```bash
cd services/api
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000/docs` for the interactive API documentation.

### Web app

```bash
cd apps/web
npm install
npm run dev
```

Open `http://localhost:3000`.

Set `NEXT_PUBLIC_API_URL` in `apps/web/.env.local` if the API is hosted somewhere other than `http://localhost:8000`.

## Demo journey

1. Complete a short phishing or OTP lesson and receive a literacy badge.
2. Create an Ipon goal such as a Medicine Fund and deposit into it.
3. Start a transfer to a new recipient.
4. Review the clear risk explanation before deciding to proceed.
5. Confirming records the transfer in the simulated ledger.

## Roadmap

- Replace `SimulatedLedger` with a Stellar implementation.
- Add authentication, trusted contacts, and account recovery.
- Support USDC and SEP-6/SEP-24 anchor flows.
- Add multilingual and voice-assisted navigation.
- Publish privacy-preserving research exports.

## Team

- Dawn Andrei Pamesa - Project Lead & System Architect
- John Andrew Balbarosa - Blockchain & Infrastructure Engineer
- Colin James Daradar - Backend & Full-Stack Developer
- Mark Diaz - Security & AI Systems Engineer

Built for the Payment & Consumer Applications hackathon track.
