# Week 6 Skill Notes: Research Pipeline

## Skill Path

```text
.github/skills/research-pipeline/SKILL.md
```

## Skill Contents

```markdown
---
name: research-pipeline
description: Drafts literature-grounded research sections using Zotero and NotebookLM via MCP. Use when asked to draft an introduction, literature review, or identify research gaps.
---

You are helping write a section of a math research paper.
You have access to two tools:
- Zotero MCP: search the user's Zotero reference library for papers, metadata, and citations
- NotebookLM skill: query the user's NotebookLM notebooks for full-text synthesis (use the notebooklm skill to ask questions and retrieve grounded answers)

Task: {{input}}

Follow these steps:
1. Search Zotero for papers relevant to the task
2. Query NotebookLM for themes, methods, and open questions across the uploaded papers
3. Draft the requested section using evidence from both sources
4. Include citations as (Author, Year) inline
5. End with a list of open questions or gaps you identified
```

## Slash Command Test

### Exact test command

```text
/research-pipeline identify the main open problems in my research area of PINNs for incompressible Navier-Stokes fluid simulation
```

### Expected behavior

The skill should:

1. search the Zotero collection for the PINN papers in `week6/references.bib`;
2. query the NotebookLM notebook for cross-paper themes and open questions;
3. synthesize the evidence into a literature-grounded research summary;
4. cite papers inline using `(Author, Year)` format;
5. end with a list of open problems or gaps.

### Saved test response summary

The test task identifies three main open-problem clusters:

- rigorous error certification and fair benchmarking against classical CFD
  methods;
- separating approximation, optimization, and discretization error in hybrid
  PINN-CFD solvers;
- handling boundary singularities, pressure-velocity coupling, high-Reynolds
  flows, and long-time stability.

The response should cite at least five papers, such as (Wang, Yu, and
Perdikaris, 2022), (Wang, Sankaran, Wang, and Perdikaris, 2023), (Wang, Li,
Chen, and Perdikaris, 2024), (Roy, Duerr, Bueck, and Sundar, 2024),
(Sheikholeslami, 2025), (Chiu et al., 2026), and (Wei et al., 2026).
