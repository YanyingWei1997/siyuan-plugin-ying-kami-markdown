# YING Kami Markdown

This plugin adapts the local Typora `kami-work-notes.css` directly to SiYuan's WYSIWYG Markdown DOM. The source CSS is preserved unchanged at `assets/kami-work-notes.typora.css` with SHA-256 `d66237ba0ef1aadbd1d0fb5a07dc822ffe6915145e074d3b3ac63461e2c5674c`.

The main paper background changes from Kami's `#fff8ed` to white. Scoped non-code Markdown text uses LXGW WenKai, while hierarchy, editorial marks and the macOS code window retain the adapted Kami structure. The adapter also removes SiYuan's inherited second blockquote bar, uses white/neutral table surfaces, and intentionally omits the red-circle annotation mapping. SiYuan's official daylight shell is not restyled.

The writing surface uses a responsive column capped at 1180px, with safe gutters on narrower windows. Inline code is rendered as a flat, shadow-free label.

All headings use LXGW WenKai and the established level-two blue. Fourth-level headings retain a stronger weight, level-five headings are slightly larger than body text, and level-six headings remain equal to body text. The editor canvas and print output are fixed to pure white.

Fenced code retains its macOS window treatment while using larger, heavier monospace text and the purple, blue, green and orange code-panel palette from Esther Design System.
