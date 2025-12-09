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
After generating the merged sample sequence (sampleA.fasta) the file was submitted to the NCBI BLASTn server (https://blast.ncbi.nlm.nih.gov/) to identify the closest matching mitochondrial sequences.
The accession numbers of the selected reference sequences are documented in the /data/reference_sequences.fasta file.

（3）Translation of DNA sequences into mitochondrial protein sequences
The cleaned sample sequence (sampleA.fasta) and the downloaded reference mitochondrial sequences were translated into protein sequences using the mitochondrial genetic code (NCBI translation table 2).
A custom Python script (translate_sequences.py) was used to:
Clean each DNA sequence (removing non-ACGTN characters)
Identify the best open reading frame (longest ORF across the three forward frames)
Translate DNA into amino acids using Biopython
Output all protein sequences into a single FASTA file (translated_proteins.fasta)

（4）Multiple Sequence Alignment (MSA) & Phylogenetic Tree Construction
After obtaining the translated protein sequences (Step 3), all sequences (sample + references) were aligned using Clustal Omega on the EBI web server:https://www.ebi.ac.uk/Tools/msa/clustalo/

Multiple Sequence Alignment (MSA)
Clustal Omega generated:
A multiple sequence alignment (in Clustal format)
A visual alignment map showing conserved positions (*, :, .)
A downloadable aligned FASTA file
The alignment was inspected to identify:
Highly conserved regions,Regions with gaps or variation,Sample sequence completeness and quality
A representative aligned region was selected and used in the report (saved as A MSA.png.....).

Guide Tree

Clustal Omega also produced:
A guide tree (Newick format .dnd)
These were exported and saved as:(A.tree.....)

