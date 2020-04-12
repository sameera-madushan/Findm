import hashlib
import sys
import os

banner = r'''

          ,'""`.
         / _  _ \           
         |(@)(@)|    FINDM - Duplicate Files Finder    
         )  __  (            by [sameera madushan]
        /,'))((`.\
       (( ((  )) ))      
        `\ `)(' /'


'''

print(banner) 

path = input("Select a directory to begin scan - ")

if not os.path.isdir(path):
    print("Oops!! Directory not found!")
else:

    '''Get absolute file paths of all the files in the given directory  
       and add them to the file_path list.
    '''
    file_path = []
    for root, dir, files in os.walk(path):
        for f in files:
            filepath = os.path.join(root, f)
            file_path.append(filepath)

    '''Get file size of every file inside the file_path list
       and add them to the file_size dict where filesize is the key.
    '''
    file_size = {}
    for filenames in file_path:
        size = os.path.getsize(filenames)

        if size in file_size.keys():
            file_size[size].append(filenames)
        else:
            file_size[size] = []
            file_size[size].append(filenames)
            
    ''' Checking if there are any simillar file sizes in file_size dict,
        if any, add them to the same_file_size dict where filesize is the key.
    '''
    same_file_size = {}
    for size in file_size:
        x = file_size[size]
        if (len(x) > 1):
            same_file_size[size] = x

    # Function to create a MD5 hash of the first 1024 bytes of a file.
    def half_md5(x):
        md5Hash = hashlib.md5()
        with open(x, 'rb') as f:
            chunk_size = 1024
            data = f.read(chunk_size)
            md5Hash.update(data)
            return md5Hash.hexdigest()

    '''Create MD5 hashes of the first 1024 bytes for the files in
       same_file_size dict.
    '''
    hash_list = {}
    for size in same_file_size:
        path = same_file_size[size]
        for i in path:
            l = half_md5(i)
            if l in hash_list.keys():
                hash_list[l].append(i)
            else:
                hash_list[l] = []
                hash_list[l].append(i)

    '''Checking if the hash_list dict is empty or not.
       Empty dictionaries evaluate to False in Python.
    '''
    empty = bool(hash_list)

    if empty is True:

        '''Looping through the hash_list dict and finding duplicate files with 
        simillar hashes. If any, add them to duplicate_files dict.
        '''
        duplicate_files = {}
        for y in hash_list:
            File = hash_list[y]
            if (len(File) > 1):
                duplicate_files[y] = File

        # Function to create a full MD5 Hash of a file. 
        def hash_file(filename):
            h = hashlib.md5()
            with open(filename,'rb') as file:
                chunk = 0
                while chunk != b'':
                    chunk = file.read(1024)
                    h.update(chunk)
            return h.hexdigest()
        
        '''Looping through the files in duplicate_files dict and creating full MD5 hash of 
        each and every file and adding them to full_file_hash dict.
        '''
        full_file_hash = {}
        for i in duplicate_files:
            file_paths = duplicate_files[i]
            for k in file_paths:
                full_md5 = hash_file(k)
                if full_md5 in full_file_hash.keys():
                    full_file_hash[full_md5].append(k)
                else:
                    full_file_hash[full_md5] = []
                    full_file_hash[full_md5].append(k)

        k = bool(full_file_hash)
        if k is True:
            length = len(full_file_hash)
            x = "file" if length == 1  else "files"
            print("\n" + str(length) + " duplicate " + x + " found.")
            print("\n[x] Duplicates files [x]")
        else:
            print('\nNo duplicate files found.')

        for k,v in full_file_hash.items():
            print("\nMD5 hash of the duplicate files: " + k + "\n")
            for files in v:
                print(files)
    else:
        print("\nNo duplicate files found.")
        


