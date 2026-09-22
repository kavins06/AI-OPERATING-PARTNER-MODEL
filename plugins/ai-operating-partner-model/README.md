# AI Operating Partner

Use this plugin to identify worthwhile AI opportunities, map real workflows, assess readiness, and create an implementation decision and operating plan.

## Start

Install the plugin in a supported ChatGPT Work or Codex environment. Start a new conversation, select AI Operating Partner, and say:

> Help me find the best AI opportunity in my business.

Or provide process notes and ask:

> Map this workflow and assess whether it is ready for AI.

The assistant asks a few business questions, chooses the relevant method, and produces useful drafts with evidence gaps and next actions. No external account or API key is required to begin. File creation and scoring depend on the tools enabled in your environment.

## What is included

27 skills: a starting point, the existing discovery orchestrator and 16 helpers, and the implementation/AgentOps orchestrator and eight helpers. Templates, schemas, rubrics, examples, scoring helpers, and method references travel with the plugin.

Discovery preserves Step 0-18 and its five client touchpoints. Implementation remains a separate authorized phase. The plugin does not supply production hosting, live connectors, or unattended monitoring.

Draft artifacts are not approvals. Missing evidence stays missing; failed hard gates override scores. Keep each client's work separate. Resume another conversation with the latest checkpoint and its referenced evidence.

## Data and source handling

The package has no MCP server, telemetry endpoint, credential store, or automatic network hook. User material is processed by the host and any separately authorized tools under their settings. Use approved, minimized examples. The original source-document corpus and source-page images are excluded. Generated method references are secondary material, not proof that the original sources were inspected.

## Install from the GitHub marketplace

In a ChatGPT Work or Codex surface with **Add from marketplace**, paste:

https://github.com/kavins06/AI-OPERATING-PARTNER-MODEL

Choose **AI Operating Partner** from **Quoin Operating Partner** and install it. Start a new conversation and use one of the prompts above. No repository cloning, manual skill copying, or API key is needed for this installation route.

CLI equivalent:

```sh
codex plugin marketplace add https://github.com/kavins06/AI-OPERATING-PARTNER-MODEL.git
codex plugin add ai-operating-partner-model@quoin-operating-partner
```

If the host does not expose GitHub marketplace imports, use a supported desktop surface or ask the workspace administrator to import the GitHub marketplace. A GitHub URL does not override workspace policy or enable a feature unavailable on an account. This distribution does not require public-directory submission.

The repository's `.agents/plugins/marketplace.json` points to the self-contained `plugins/ai-operating-partner-model/` package. Maintainers edit the source skills first and run `python scripts/build-plugin.py` before publishing updates. Then refresh the marketplace and reinstall/update the plugin as supported by the host; start a new conversation.

Platform references checked September 21, 2026:
- [Packaging and distribution](https://developers.openai.com/plugins/build/plugins)
- [Workspace sharing](https://help.openai.com/en/articles/20001256/)
