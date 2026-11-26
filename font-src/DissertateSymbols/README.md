# Dissertate Symbols prototype

This experimental font adds U+21E5 (RIGHTWARDS ARROW TO BAR) and U+291E (RIGHTWARDS ARROW WITH TAIL WITH BLACK DIAMOND), plus a normal space for fontspec compatibility. It is separately named Dissertate Symbols. No template loads it, and no historical font file is modified. Final visual review and PDF Unicode checks remain pending.

`arrowright.json` records the outline from `SFD/EBGaramond12-Regular.sfdir/arrowright.glyph` at upstream revision `d04d0f9da5adad27ff0e5947807b80cfe13dc477`. Its source-file SHA-256 is recorded alongside the path commands. The builder preserves that arrow and adds a terminal bar or black diamond. It does not execute upstream build code. The upstream source is at https://github.com/georgd/EB-Garamond/tree/d04d0f9da5adad27ff0e5947807b80cfe13dc477 .

The outline and resulting font are licensed under SIL Open Font License 1.1; see `OFL.txt`. The original copyright notice is retained. The new family name does not claim to be an upstream EB Garamond release. Source-to-binary correspondence with the historical bundled fonts remains unproved.

The dedicated CI workflow installs FontTools 4.61.1 on its runner. It builds the font twice, compares the bytes, verifies the two Unicode mappings and family name, and uploads a temporary review artifact. It creates no release or tag. To build in an environment with that dependency, run `python scripts/build-symbol-font /path/to/new/DissertateSymbols-Regular.otf`. The output directory must exist, and the output file must be new. A failed build may retain a partial output file.
