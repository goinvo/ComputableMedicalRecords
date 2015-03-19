import os
import shutil

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


# ------------------------- SCHEMA SERVER BUILD --------------------------- #
SCHEMA_BUILD_SOURCE = os.path.join(BASE_PATH, 'schema-server')
SCHEMA_BUILD_DEST = os.path.join(BASE_PATH, 'build', 'schema-server')

def prep_schema_files(base_url):
    # TODO: Build in opts to minimize, etc
    for root, dirs, files in os.walk(SCHEMA_BUILD_DEST):
        for filename in files:
            
            if filename == ".DS_Store":
                os.remove(os.path.join(root, filename))
                continue

            with open(os.path.join(root, filename), "r+") as f:
                contents = f.read()
                contents = contents.replace("{{BASE_URL}}", base_url)
                contents = contents.replace("\t", "    ")
                f.seek(0)
                f.truncate()
                f.write(contents)

def build_schema_server(base_url):
    # Wipe the old dir
    if os.path.exists(SCHEMA_BUILD_DEST):
        shutil.rmtree(SCHEMA_BUILD_DEST)

    # Copy files across
    shutil.copytree(SCHEMA_BUILD_SOURCE, SCHEMA_BUILD_DEST)

    # Some basic find and replace
    prep_schema_files(base_url)
# ------------------------- SCHEMA SERVER BUILD --------------------------- #



# ------------------------- DATA SERVER BUILD --------------------------- #
DATA_BUILD_SOURCE = os.path.join(BASE_PATH, 'data-server')
DATA_BUILD_DEST = os.path.join(BASE_PATH, 'build', 'data-server')
            
def build_data_server(base_url):
    # Wipe the old dir
    if os.path.exists(DATA_BUILD_DEST):
        shutil.rmtree(DATA_BUILD_DEST)

    # Copy files across
    shutil.copytree(DATA_BUILD_SOURCE, DATA_BUILD_DEST)
# ------------------------- DATA SERVER BUILD --------------------------- #


# ------------------------- HGRAPH SERVER BUILD --------------------------- #
HGRAPH_BUILD_SOURCE = os.path.join(BASE_PATH, 'demo-apps', 'hgraph')
HGRAPH_BUILD_DEST = os.path.join(BASE_PATH, 'build', 'hgraph-server')
            
def prep_hgraph_files(base_url):
    # TODO: Build in opts to minimize, etc
    for root, dirs, files in os.walk(HGRAPH_BUILD_DEST):
        for filename in files:
            
            if filename == ".DS_Store":
                os.remove(os.path.join(root, filename))
                continue

            with open(os.path.join(root, filename), "r+") as f:
                contents = f.read()
                contents = contents.replace("{{BASE_URL}}", base_url)
                #contents = contents.replace("\t", "    ")
                f.seek(0)
                f.truncate()
                f.write(contents)
            
def build_hgraph_server(base_url):
    # Wipe the old dir
    if os.path.exists(DATA_BUILD_DEST):
        shutil.rmtree(DATA_BUILD_DEST)

    # Copy files across
    shutil.copytree(DATA_BUILD_SOURCE, DATA_BUILD_DEST)
    
    # Some basic find and replace
    prep_hgraph_files(base_url)
# ------------------------- HGRAPH SERVER BUILD --------------------------- #

if __name__=="__main__":
    '''A "build" script for this project.'''
    
    # TODO: Convert to command line opts
    IS_LOCAL = True
    if IS_LOCAL:
        base_server_url = "http://localhost:%d/"
    else:
        base_server_url = "http://23.239.7.31:%d/"


    schema_server_url = base_server_url % 12000
    data_server_url = base_server_url % 12100
    hgraph_server_url = base_server_url % 12200

        

    
    # 1. Build the schema server
    build_schema_server(schema_server_url)
    
    # 2. Build the data server
    build_data_server(data_server_url)
    
    # 3. Build the apps
    build_graph_server(hgraph_server_url)
    
    



