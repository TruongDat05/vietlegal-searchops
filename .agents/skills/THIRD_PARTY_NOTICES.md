# Third-party guidance and notices

The VietLegal skills are project-specific adaptations prepared on 2026-11-27.
They reuse selected workflow ideas rather than requiring the original skill
packages to be installed. The applicable MIT notices are retained below.

| Source | Adapted guidance | Local destination |
| --- | --- | --- |
| [Ponytail](https://github.com/dietrichgebert/ponytail) | Reuse existing code, prefer standard tools, avoid speculative complexity | vietlegal-dev |
| [Matt Pocock skills](https://github.com/mattpocock/skills) | Small interfaces, behavior-oriented tests, reproducible debugging and requirements/quality review | vietlegal-dev, vietlegal-debug, vietlegal-review |
| [Superpowers](https://github.com/obra/superpowers) | Cause-driven debugging and verification before completion claims | vietlegal-debug, vietlegal-review |
| [Lazygit](https://github.com/jesseduffield/lazygit) | Optional interactive staging of hunks and lines | vietlegal-git/references/lazygit.md |

Lazygit is referenced as an optional tool; no Lazygit code or assets are bundled.
The Git commit grouping rules are the user's project policy. Generic rules
requiring an issue tracker, mandatory sub-agents, repeated approval of agreed
interfaces, deletion of existing implementation for TDD, or a fixed terse
response format were not imported into these skills.

## Source identity

The installed source skills were inspected locally. The values below are
installer folder hashes, not upstream Git commit SHAs:

- ponytail: cb6e53477eaf04e6daeca22feacb85f9ce20d40c
- codebase-design: 344e3efc88ee60663b2e989555c2efdb548fbd42
- diagnosing-bugs: 99bd56983e42bc752c52da67f1112e4121781cd1
- tdd: 79288be15c67b849f22b6572056601090fd20913
- code-review: d8e341cee7980127dddda05159bedf25dc853615

The inspected Superpowers checkout was at commit 22f0b46.
Ponytail and Matt Pocock MIT license texts were retrieved from their
upstream repositories on the preparation date; the Superpowers notice
was preserved from the inspected checkout.

## Ponytail

Source: https://github.com/dietrichgebert/ponytail

```text
MIT License

Copyright (c) 2026 DietrichGebert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Matt Pocock skills

Source: https://github.com/mattpocock/skills

```text
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Superpowers

Source: https://github.com/obra/superpowers

```text
MIT License

Copyright (c) 2025 Jesse Vincent

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
