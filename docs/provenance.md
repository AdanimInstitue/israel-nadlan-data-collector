# Provenance Design

The public collector emits a manifest for each bundle. The manifest records:

- source inventory limited to public-safe sources
- build timestamp
- collector version
- bundle file paths relative to the repository
- file hashes, sizes, and row counts
- source summary and provenance references safe for public publication

The public bundle intentionally avoids:

- absolute workstation paths
- sibling-repository references
- secret names
- internal batch identifiers
