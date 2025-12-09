# mitochondrial-sequence-identification
Analysis pipeline for mitochondrial sequence assembly, translation, multiple sequence alignment, and phylogenetic inference. Includes all scripts, data, and reproducible steps matching the submitted report.
1.Requirements
This project uses:
Python 3.8+
Biopython
Clustal Omega (EBI web server)
2.Repository Contents
data/            # Input + output sequences
scripts/         # Python scripts used in analysis
results/         # Final alignment region and phylogram images
README.md        # This file
3.Workflow Overview
（1）Merge FASTQ parts into a single fasta file
Script:fastq_parts_to_fasta.sh
Input:sampleA_part1.FASTQ  sampleA_part2.FASTQ  sampleA_part3.FASTQ  sampleB_part1.FASTQ......
Output:sampleA.fasta sampleB.fasta sampleC.fasta.....
（2）Database Search (NCBI BLAST)
After generating the merged sample sequence (sampleA.fasta) the file was submitted to the NCBI BLASTn server (https://blast.ncbi.nlm.nih.gov/
) to identify the closest matching mitochondrial sequences.
The accession numbers of the selected reference sequences are documented in the /data/reference_sequences.fasta file.
