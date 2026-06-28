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
