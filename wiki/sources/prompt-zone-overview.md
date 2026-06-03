---
created: 2026-06-03
updated: 2026-06-03
type: source
title: "Prompt Zone — Team LLM Overview"
status: summarized
source_path: "03-prompt-zone/PROMPT-ZONE-OVERVIEW.md"
hash: "e80f289b6fe2376755f47e5afb3b2260"
ingested: 2026-05-16
tags: [source, orchestration, team-llm]
---

# Prompt Zone — Team LLM Overview

> [!key-insight] One-line
> The operating manual for KTG's multi-model orchestration: Claude as spine, Gemini for research, Codex for mechanical execution, Jules for async. Source upstream: NotebookLM "The Prompt Zone: Team LLM Production Bible".

## Core purpose

Encode proven orchestration patterns, routing logic, and prompt templates so [[Team LLM Orchestration Roster|Team LLM]] operates systematically rather than ad hoc.

## Roster

| Agent | Model | Role | Strengths |
|---|---|---|---|
| Claude (spine) | Claude Sonnet/Opus | Strategy, synthesis, final output | Precision, instruction following |
| Gemini | Gemini | Research, long context, verification | Web-grounded, analytical |
| Codex | Codex CLI | Mechanical execution | Bulk edits, literal compliance |
| Jules | Jules CLI | Async background | GitHub-native, background queue |

See [[Team LLM Orchestration Roster]] for the doctrine page (when to use which agent for what).

## Content pipeline

- Battle of the Bots (Reddit/Medium — 20K+ views historical)
- Prompt engineering posts
- ArXiv publication pipeline

## Related projects (sister vaults / repos)

- LEGIO/ — framework
- Recursive-Council/ — multi-agent reasoning

## Cross-references

- [[team-llm-production-bible]] — the animated series powered by this orchestration
- [[user-voice]] — voice doctrine for written content
- [[Team LLM Orchestration Roster]]
