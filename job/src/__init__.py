import process_file 
if __name__ == '__main__':
    path_origin = './files'
    path_dest = '/tmp'
    files = process_file.getFiles(path_origin,'.zip')
    print ('Get zip files')
    print(files)
    for file in files:
        process_file.uncompresFile(path_origin+'/'+file,path_dest)
    files = process_file.getFiles(path_dest,'')
    print ('Get XML files')
    print(files)
    for file in files:
        process_file.process_file(path_dest+'/'+file)
    
