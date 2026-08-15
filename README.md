# YING Kami Markdown

This plugin adapts the local Typora `kami-work-notes.css` directly to SiYuan's WYSIWYG Markdown DOM. The source CSS is preserved unchanged at `assets/kami-work-notes.typora.css` with SHA-256 `d66237ba0ef1aadbd1d0fb5a07dc822ffe6915145e074d3b3ac63461e2c5674c`.

The main paper background changes from Kami's `#fff8ed` to white. Typography, hierarchy, editorial marks and the macOS code window retain the local Kami definitions. The adapter also removes SiYuan's inherited second blockquote bar, uses white/neutral table surfaces, and intentionally omits the red-circle annotation mapping. SiYuan's official daylight shell is not restyled.

The writing surface uses a responsive column capped at 1180px, with safe gutters on narrower windows. Inline code is rendered as a flat, shadow-free label.
