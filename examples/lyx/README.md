# Experimental Generic LyX export

This prototype tests export from LyX to a Generic Dissertate project. It is not included in school ZIPs. GUI editing, PDF preview inside LyX, bibliography editing, back matter, and complete dissertations remain unverified.

The custom `dissertate.layout` inherits the standard book layout and maps its class to `Dissertate.cls`. The example uses native document format 643 and layout format 111. The inspected LyX 2.5.3 source defines those formats. The CI prototype targets Ubuntu 26.10 packages `lyx` and `lyx-common` at version `2.5.2-1`; compatibility must be established by the run.

Text fonts remain at their paired defaults, math is `auto`, and non-TeX fonts are enabled. The layout declares that the class provides fontspec. These settings are intended to preserve the class-selected fonts without requesting unicode-math. The exported preamble is checked before compilation.

The CI check creates a fresh LyX user directory and copies the custom layout into its `layouts/` directory before configuration. A packaged Generic project is available through `TEXINPUTS`. LyX exports to an explicit TeX path; XeLaTeX then compiles from the project root. The example calls the existing front-matter hook and retains its external author resources. Its colophon is disabled. It adds one chapter and a short formula; it does not call the back-matter hook.

The exporter adds English language setup through polyglossia. The inspected PDF retained EB Garamond for the chapter title and body paragraph. The class requests Palatino for its large chapter numeral; its unavailable bold shape falls back to Latin Modern. This class-level font limitation remains. Math symbols may use Computer Modern.

No LyX executable is installed on the laptop by this workflow. The runtime version, executable hash, class-discovery record, export log, generated TeX, paragraph-level font mapping, and PDF are retained as temporary CI artifacts. Inspect those artifacts before claiming support for a configuration.
