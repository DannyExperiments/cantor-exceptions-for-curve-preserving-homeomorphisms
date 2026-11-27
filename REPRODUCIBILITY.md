# Reproducing the checks

Use Python 3 with its standard library for both checks. Run the commands in the repository root.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The first checks every public file against the manifest and SHA-256 ledger and scans plain text for private markers. The second uses exact rational arithmetic to check the finite geometry for levels 1 through 16, including separation of the vertical probe from both children and the alternating cumulative scalar. The expected output is in verification/logs/replay.txt. The analytic proofs of existence, continuity of tangent directions and almost-everywhere differentiability are in the paper.

The offline explorer requires a modern web browser. The prebuilt GIF can be regenerated with Pillow. For source builds of the PDF, see [paper/BUILD.md](paper/BUILD.md).
