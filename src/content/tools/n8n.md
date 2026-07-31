---
title: "n8n"
description: "A flexible workflow automation platform for teams that need more control over logic, data and technical setup."
category: "Automation platform"
pricing: "Free self-hosted / paid cloud plans"
website: "https://n8n.io/"
verdict: "Best when control and custom logic matter enough to justify a more technical operating model."
featured: false
bestFor:
  - "Custom integrations and workflows with non-standard logic"
  - "Technical teams that want more control over their automation layer"
  - "Processes where data handling and deployment choices matter"
watchOutFor: "Flexibility creates responsibility. Self-hosting, credentials, monitoring, backups and security need a real owner; do not choose n8n only because it looks cheaper than a managed tool."
---

## The short version

n8n is for the point where a simple app connection is no longer enough. It gives a technical team more room to shape data, add custom logic and decide how the workflow is operated.

That makes it powerful, but it is not automatically the right first choice. Use it when control is a requirement — not as a hobby project for an otherwise simple process.

## Where it earns its place

Use n8n when you need to:

- combine standard app integrations with custom API calls or code;
- control how automation credentials and data are handled;
- build a workflow around business-specific rules that templates cannot express well;
- give a developer or technical operator a maintainable automation layer;
- avoid forcing an unusual process into a rigid app-to-app template.

## A practical starting setup

Pick one workflow with a clear technical reason to exist: perhaps normalising lead data from several sources, applying your own routing logic and then creating one consistent CRM record.

1. Name the business owner and technical owner before building it.
2. Keep secrets outside the workflow definition and restrict their access.
3. Add logs, alerts and a safe retry path before making it business-critical.
4. Document the input, output, failure behaviour and human fallback.

## The H² rule

Control is useful only when somebody owns it.

n8n is a good long-term choice for a team that will maintain the system. For a simple, low-risk handoff, use the smallest tool that reliably does the job.
