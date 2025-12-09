from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os

# Folder containing the input sequences; here we use the current directory
INPUT_FOLDER = "."
OUTPUT_FILE = "translated_proteins.fasta"

def clean_dna(seq):
    """Retain only A, C, G, T, N characters; remove whitespace, gaps, or other symbols."""
    s = str(seq).upper()
    cleaned = "".join([b for b in s if b in "ACGTN"])
    return Seq(cleaned)

def find_best_orf(dna_seq, table=2, min_aa_length=30):
    """
    Identify the longest ORF among the three forward reading frames.
    Translation uses mitochondrial genetic code table 2.
    
    If the longest ORF is still short (< min_aa_length),
    the function falls back to a simple translation using frame 0
    until the first stop codon.
    """
    best_prot = None
    best_len = 0

    for frame in range(3):
        # Translate starting from each reading frame
        coding = dna_seq[frame:]
        # Translate the entire sequence (without stopping at the first stop),
        # allowing us to search for ORFs separated by '*'
        prot = coding.translate(table=table)

        # Split by '*' to obtain individual ORFs
        for orf in str(prot).split("*"):
            aa_seq = orf.replace("X", "")  # Remove ambiguous amino acids
            length = len(aa_seq)
            if length > best_len:
                best_len = length
                best_prot = aa_seq

    # If a sufficiently long ORF was found, return it
    if best_prot and best_len >= min_aa_length:
        return Seq(best_prot)

    # Otherwise, fall back to simple frame-0 translation until first stop codon
    return dna_seq.translate(table=table, to_stop=True)

records = []

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".fasta") or filename.endswith(".fa") or filename.endswith(".fna"):
        path = os.path.join(INPUT_FOLDER, filename)
        for record in SeqIO.parse(path, "fasta"):
            dna = clean_dna(record.seq)

            if len(dna) < 30:
                # Skip sequences that are too short
                continue

            protein = find_best_orf(dna, table=2, min_aa_length=30)

            if len(protein) == 0:
                continue

            new_record = SeqRecord(
                protein,
                id=record.id,
                description="best_orf_mito_table2"
            )
            records.append(new_record)

# Write all translated protein sequences to a FASTA file
SeqIO.write(records, OUTPUT_FILE, "fasta")
print(f"Translation completed. {len(records)} protein sequences written to {OUTPUT_FILE}.")
