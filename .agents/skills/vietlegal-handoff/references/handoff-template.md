# Handoff record template

Use only fields relevant to the actual handoff. Put the record in the current
response, existing task/PR or requested document; a new report is not mandatory.
Replace example markers with real values. Write `not available` for missing
evidence instead of inventing a hash, command result or completion status.

```text
Task / handoff: <task ID and H01-H09 if applicable>
Producer / receiver: <owner> -> <consumer>
Status: ready | partial | blocked by a named missing input
Receiver acceptance: pending | <actual acknowledgement and reviewed version>

Delivered behavior:
- <observable interface or capability>

Code / contract:
- <branch and commit if one exists; otherwise identify the working-tree version>
- <entry point, schema version, required inputs and returned outputs>
- <compatibility, profile change or migration requirement>

Artifacts / example:
- <explicit path, release ID, manifest/profile hash if available>
- <small fixture/example and expected behavior>
- <required access/environment without secret values>

Verification:
- <exact command, observed result and evidence level>
- <code/configuration/artifact version covered by the check>

Limits / next action:
- <missing input, known limitation and its effect>
- <the receiver's next concrete action>
- <decision still needed and its responsible owner, if any>
```

Preserve restricted gold custody. Link to a permitted artifact/interface rather
than pasting secrets or held-out labels into a shared handoff. A fixture-only
handoff states that limitation explicitly; it is not a completed real-data run.
