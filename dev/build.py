import os
import shutil

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


# ------------------------- SCHEMA SERVER BUILD --------------------------- #
SCHEMA_BUILD_SOURCE = os.path.join(BASE_PATH, 'schema-server')
SCHEMA_BUILD_DEST = os.path.join(BASE_PATH, 'build', 'schema-server')

def prep_schema_files(replacements):
    # TODO: Build in opts to minimize, etc
    for root, dirs, files in os.walk(SCHEMA_BUILD_DEST):
        for filename in files:
            
            filepath = os.path.join(root, filename)
            
            if filename == ".DS_Store":
                os.remove(filepath)
                continue

            with open(filepath, "r+") as f:
                contents = f.read()
                contents = contents.replace("{{BASE_URL}}", replacements['schema_url'])
                contents = contents.replace("\t", "    ")
                f.seek(0)
                f.truncate()
                f.write(contents)

def build_schema_server(replacements):
    # Wipe the old dir
    if os.path.exists(SCHEMA_BUILD_DEST):
        shutil.rmtree(SCHEMA_BUILD_DEST)

    # Copy files across
    shutil.copytree(SCHEMA_BUILD_SOURCE, SCHEMA_BUILD_DEST)

    # Some basic find and replace
    prep_schema_files(replacements)
# ------------------------- SCHEMA SERVER BUILD --------------------------- #



# ------------------------- DATA SERVER BUILD --------------------------- #
DATA_BUILD_SOURCE = os.path.join(BASE_PATH, 'data-server')
DATA_BUILD_DEST = os.path.join(BASE_PATH, 'build', 'data-server')
            
def build_data_server(replacements):
    # Wipe the old dir
    if os.path.exists(DATA_BUILD_DEST):
        shutil.rmtree(DATA_BUILD_DEST)

    # Copy files across
    shutil.copytree(DATA_BUILD_SOURCE, DATA_BUILD_DEST)
# ------------------------- DATA SERVER BUILD --------------------------- #


# ------------------------- HGRAPH SERVER BUILD --------------------------- #
HGRAPH_BUILD_SOURCE = os.path.join(BASE_PATH, 'demo-apps', 'hgraph')
HGRAPH_BUILD_DEST = os.path.join(BASE_PATH, 'build', 'hgraph-server')
HGRAPH_IGNORE_PATTERNS = ['bower_components/', 'bower.json', 'css/']
            
def prep_hgraph_files(replacements):
    # TODO: Build in opts to minimize, etc
    for root, dirs, files in os.walk(HGRAPH_BUILD_DEST):
        for filename in files:
            
            filepath = os.path.join(root, filename)
            
            # TODO: Fix this madness!
            matched = False
            for pattern in HGRAPH_IGNORE_PATTERNS:
                if filepath.find(pattern) > -1:
                    matched = True
                    continue
            if matched:
                continue
                
            
            if filename == ".DS_Store":
                os.remove(filepath)
                continue
                
            with open(filepath, "r+") as f:
                contents = f.read()
                contents = contents.replace("{{BASE_URL}}", replacements['hgraph_url'])
                contents = contents.replace("{{DATA_URL}}", replacements['data_url'])
                contents = contents.replace("{{SCHEMA_URL}}", replacements['schema_url'])
                
                #contents = contents.replace("\t", "    ")
                f.seek(0)
                f.truncate()
                f.write(contents)
            
def build_hgraph_server(replacements):
    # Wipe the old dir
    if os.path.exists(HGRAPH_BUILD_DEST):
        shutil.rmtree(HGRAPH_BUILD_DEST)

    # Copy files across
    shutil.copytree(HGRAPH_BUILD_SOURCE, HGRAPH_BUILD_DEST)
    
    # Some basic find and replace
    prep_hgraph_files(replacements)
# ------------------------- HGRAPH SERVER BUILD --------------------------- #

# ------------------------- ALL SERVER SCRIPTS --------------------------- #
ALL_BUILD_DEST = os.path.join(BASE_PATH, 'build')

def build_server_scripts(replacements):
    # TODO: Build in opts to minimize, etc
    for root, dirs, files in os.walk(ALL_BUILD_DEST):
        for filename in files:
            
            filepath = os.path.join(root, filename)
            
            if filepath.endswith('server.py'):                
                with open(filepath, "r+") as f:
                    contents = f.read()
                    contents = contents.replace("{{SERVER_HOST}}", replacements['server_host'])
                    contents = contents.replace("{{DEBUG}}", replacements['debug'])
                    f.seek(0)
                    f.truncate()
                    f.write(contents)
                    


# ------------------------- ALL SERVER SCRIPTS --------------------------- #

if __name__=="__main__":
    '''A "build" script for this project.'''
    
    # TODO: Convert to command line opts
    IS_LOCAL = True
    if IS_LOCAL:
        base_server_url = "http://localhost:%d/"
        server_host = "127.0.0.1"
        debug = True
    else:
        base_server_url = "http://23.239.7.31:%d/"
        server_host = "0.0.0.0"
        debug = False


    replacements = {
        'schema_url': base_server_url % 12000,
        'data_url': base_server_url % 12100,
        'hgraph_url': base_server_url % 12200,
        'server_host': server_host,
        'debug': str(debug),
    }
        

    
    # 1. Build the schema server
    build_schema_server(replacements)
    
    # 2. Build the data server
    build_data_server(replacements)
    
    # 3. Build the apps
    build_hgraph_server(replacements)
    
    # 4. Handle server scripts
    build_server_scripts(replacements)
    
    



