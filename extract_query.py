import argparse 
import csv
from clef_dataloader import load_queries

def lists_to_tsv(doc_ids, documents, output_file):
    # zip으로 두 리스트를 묶고, tsv 파일로 저장
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        
        # zip을 사용하여 doc_ids와 documents를 하나로 묶어서 iteration
        for doc_id, document in zip(doc_ids, documents):
            writer.writerow([doc_id, document])


def main(args):
    (q_ids, queries) = load_queries(args.language, args.year, include_desc=False)
    print(f"{len(q_ids)} queries loaded")
    # Sanity check
    print(q_ids[14])
    print(queries[14])
    lists_to_tsv(q_ids, queries, args.output_path)
    print(f"Saved to {args.output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load a document from a given path")
    parser.add_argument("--language", type=str, help="Path to the document")
    parser.add_argument("--year", type=str, help="Path to the document")

    parser.add_argument("--output_path", type=str, help="Path to the output file")
    args = parser.parse_args()
    main(args)