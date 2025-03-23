import os
import sys
import argparse
import hashlib
import time
from datetime import datetime

def log_message(log_file_path, message):
    timestamp = datetime.now().strftime('%Y_%m_%d---%H:%M')
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f'{timestamp} - {message}\n')

def process_file(file_path):
    complete_path = os.path.abspath(file_path)
    file_size = os.path.getsize(complete_path)
    modified_date = int(os.path.getmtime(complete_path))
    creation_date = int(os.path.getctime(complete_path))
    file_name_ext = os.path.basename(complete_path)
    
    hash_string = f"{complete_path}\t{file_size}\t{modified_date}"
    file_hash = hashlib.sha256(hash_string.encode()).hexdigest()
    
    return (complete_path, file_size, modified_date, file_hash, 
            file_name_ext, creation_date)

def scan_folders(input_file_path, output_file_path, sleep_value=None, 
                files_sleep=None):
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    log_file_path = os.path.join(script_dir, 'file_scanner.log')
    
    log_message(log_file_path, 'start')
    log_message(log_file_path, 'received command line')
    
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            folders = [line.strip() for line in input_file if line.strip()]
    except Exception as e:
        log_message(log_file_path, f'error reading input file: {str(e)}')
        return
    
    try:
        output_file = open(output_file_path, 'w', encoding='utf-8')
    except Exception as e:
        log_message(log_file_path, f'error opening output file: {str(e)}')
        return
    
    files_processed = 0
    sleep_seconds = sleep_value / 1000.0 if sleep_value else None
    
    try:
        for folder in folders:
            try:
                for root, _, files in os.walk(folder):
                    for file_name in files:
                        try:
                            file_path = os.path.join(root, file_name)
                            file_data = process_file(file_path)
                            output_line = '\t'.join(str(x) for x in file_data)
                            output_file.write(output_line + '\n')
                            output_file.flush()
                            
                            files_processed += 1
                            if files_processed % 1000 == 0:
                                log_message(log_file_path, 
                                          f'scanned {files_processed} files')
                            
                            if (sleep_seconds and files_sleep and 
                                files_processed % files_sleep == 0):
                                time.sleep(sleep_seconds)
                                
                        except Exception as e:
                            log_message(log_file_path, 
                                      f'error processing file {file_path}: {str(e)}')
                            continue
                            
            except Exception as e:
                log_message(log_file_path, 
                          f'error opening the folder {folder}: {str(e)}')
                continue
                
    finally:
        output_file.close()
        log_message(log_file_path, 'finish')

def main():
    parser = argparse.ArgumentParser(description='File Scanner')
    parser.add_argument('input_file', help='Path to input file with folders list')
    parser.add_argument('--sleep_value', type=int, 
                       help='Sleep time in milliseconds')
    parser.add_argument('--files_sleep', type=int, 
                       help='Number of files after which to sleep')
    parser.add_argument('output_file', help='Path to output file')
    
    args = parser.parse_args()
    
    scan_folders(args.input_file, args.output_file, 
                args.sleep_value, args.files_sleep)

if __name__ == '__main__':
    main() 
