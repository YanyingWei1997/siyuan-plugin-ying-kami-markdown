# YING Kami Markdown 0.1.0

## Goal

Use SiYuan's official daylight interface and directly migrate the user's local Typora Kami Markdown design. Change only the main paper background to white.

## Scope

- Preserve the original Typora CSS as a checksummed source asset.
- Map Typora selectors to SiYuan Protyle selectors without changing visual tokens.
- Cover title hierarchy, prose, links, lists, tasks, quotations, math, tables, marks, proofing decorations, images, footnotes and code.
- Add no application-shell selectors.

## Acceptance

1. Official daylight remains active.
2. Enabling the plugin changes Markdown content only.
3. Original source checksum matches the installed Typora file.
4. Paper is white; all other Kami tokens remain source-faithful.
5. Disabling removes the root class and restores defaults.
