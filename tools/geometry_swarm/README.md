# Bounded local geometry swarm

A standard-library Python runner for exact construction checks and proposal/critique requests to **existing local model services**. It does not prove RH, score novelty, execute generated code, admit research rows, or run continuously.

The September 29 pilot and its mathematical corrections are in [the audit](../../audits/geometric-swarm-2026-09-29-v1/README.md). Three Codex construction agents worked separately from the nine local-model inference requests. Neither model agreement nor a valid JSON reply is a mathematical gate pass.

## Exact checks

From the repository root:

```sh
python3 -m tools.geometry_swarm check --workers 2 --out .local-runs/exact-example-1
```

This replays 165 deterministic calibration fixtures: local graded orbit weights in 4D/6D/8D, composite/duplicate primitive controls, collapsed elliptic deck maps, and a failed independent passive Euler-factor architecture. All arithmetic comparisons use integers and fractions. The cases are repetitions of a few known distinctions, not 165 research ideas. A `test_passed` result means the expected admission/rejection behavior was reproduced; it does not mean the candidate condition is true.

These are CPU tasks. Increasing GPU count will not accelerate the current exact checker. Add only reviewed, bounded checks with a stated decision and matched control. General symbolic identities and arbitrary AI-generated programs are not executable inputs.

## Existing local LLM services

Set these shell variables to an existing OpenAI-compatible service and a model it already serves. The values below are placeholders, not configured infrastructure:

```sh
export RH_MODEL_URL='http://<private-address>:<port>/v1'
export RH_MODEL_NAME='<served-model-name>'
python3 -m tools.geometry_swarm discover --url "$RH_MODEL_URL"
python3 -m tools.geometry_swarm swarm \
  --url "$RH_MODEL_URL" --model "$RH_MODEL_NAME" \
  --workers 1 --copies 1 --tokens 1200 --timeout 60 \
  --out .local-runs/proposal-example-1
```

Discovery currently supports an endpoint that does not require authentication. For inference requiring a key, put the key in an environment variable and pass its **name** with `--api-key-env`; never write a key into a command argument, report, or repository file. The public example intentionally contains no host-specific address.

Use `--review-url` and `--review-model` for a separate critic model. `--review-api-key-env` is separate; the proposal key is inherited only when the reviewer uses the same endpoint. `--disable-thinking` and `--review-disable-thinking` explicitly send `chat_template_kwargs.enable_thinking=false`; use them only with a service that supports that option. No thinking option is sent by default.

There are three construction briefs: contact assembly, adelic intersection geometry, and a completed canonical system. Each call produces one proposal per brief per copy, then critiques replies that meet the minimal format check. The post-pilot briefs were revised to reduce template copying. **Their effectiveness has not yet been tested by another inference batch.**

## Limits and records

- CLI: 1–4 copies, 1–4 workers, at most 12 proposals plus 12 critiques, at most 4,096 requested output tokens per call, and a request timeout up to 90 seconds. The timeout starts after DNS resolution; it is not an end-to-end DNS deadline. Inference servers may continue work after a client timeout.
- HTTP-level success and proposal schema compliance are recorded separately. Critic JSON is retained as text rather than semantically validated. All proposals require subsequent source and mathematical review; there is no automatic admission.
- Fresh output directories are required. Failed outputs are retained, with no automatic retry. `.local-runs/` is gitignored; raw records include the supplied endpoint. Deliberately sanitized copies can be published with the audit.
- Only loopback/private/Tailscale addresses are allowed. Resolved addresses are pinned for the connection, public DNS answers are rejected, redirects and environment proxies are disabled. A short hostname may fail validation; use an independently verified private address, not a weaker guard.
- No model download, service restart, remote installation, GPU allocation, background scheduler, shell execution of model replies, or automatic proof/certificate promotion is implemented.
- The client uses standard-library HTTP handling; exact checks use `Fraction`. No new package dependencies are needed.

## Validation and maintenance

```sh
python3 -m unittest discover -s tests -p 'test_geometry_swarm*.py' -v
pyright tools/geometry_swarm tests/test_geometry_swarm_checks.py \
  tests/test_geometry_swarm_models.py tests/test_geometry_swarm_pipeline.py
```

The HTTP regression tests bind temporary local servers. Run from the repository root so pyright uses its configured environment. Before a new RH-directed candidate, refresh the repository conclusions and apply `PROPOSAL_TEMPLATE.md`, the wall check, the dependency-edge requirement, and the actual matched control. A successful local construction fixture does not waive that gate.
