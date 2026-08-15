"use strict";

const { Plugin } = require("siyuan");

const ROOT_CLASS = "ying-kami-markdown-enabled";

class YingKamiMarkdownPlugin extends Plugin {
  onload() {
    document.documentElement.classList.add(ROOT_CLASS);
  }

  onunload() {
    document.documentElement.classList.remove(ROOT_CLASS);
  }
}

module.exports = YingKamiMarkdownPlugin;
