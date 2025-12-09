#!/bin/bash

# Usage:
#   ./fastq_parts_to_fasta.sh sampleA
#
# This script assumes the current directory contains files such as:
#   sampleA_part1.FASTQ, sampleA_part2.FASTQ, sampleA_part3.FASTQ, ...

if [ $# -ne 1 ]; then
    echo "Usage: $0 SAMPLE_PREFIX"
    echo "Example: $0 sampleA"
    exit 1
fi

SAMPLE=$1
OUT="${SAMPLE}.fasta"

# Initialize the final concatenated sequence as empty
full_seq=""

# Loop through all part files for the given sample in numeric order
# Note: the shell automatically expands sorted filenames such as:
# sampleA_part1.FASTQ, sampleA_part2.FASTQ, sampleA_part3.FASTQ, ...
for f in ${SAMPLE}_part*.FASTQ; do
    echo "Processing $f ..."

    # Extract the nucleotide sequence from each FASTQ file:
    # read lines after the header (@) until the '+' line is encountered.
    part_seq=$(awk '
        # Skip empty lines
        /^[ \t]*$/ { next }

        # When encountering a header line (starting with @),
        # start reading the sequence but skip the header itself
        /^@/ { in_seq=1; next }

        # When encountering a "+" line, the sequence section ends,
        # and the quality section begins — stop reading
        /^\+/ { in_seq=0; exit }

        # While in sequence-reading mode, append nucleotide lines
        in_seq==1 {
            # Remove any non-nucleotide characters (e.g., whitespace)
            gsub(/[^ACGTNacgtn]/, "", $0)
            seq = seq $0
        }

        END {
            print seq
        }
    ' "$f")

    # Append this part’s sequence to the full concatenated sequence
    full_seq="${full_seq}${part_seq}"
done

# Write the final FASTA file: one header and one full concatenated sequence
echo ">${SAMPLE}" > "$OUT"
echo "$full_seq" >> "$OUT"

echo "Written FASTA: $OUT"
