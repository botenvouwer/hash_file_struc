from pathlib import Path

from lib import hash_file_structure

geopackage_path = Path("/Users/williamloosman/pdok/rioned/stedelijkwater.gpkg")
geopackage_path2 = Path("/Users/williamloosman/pdok/rioned/stedelijkwater_v2_33264536.gpkg")

file_hash = hash_file_structure(geopackage_path)
file_hash2 = hash_file_structure(geopackage_path2)

print(geopackage_path.name)
print(file_hash)

print(geopackage_path2.name)
print(file_hash2)

hash_name_map = {
    "e8dd8599a29c1daf3c23efb908b922ab": "stedelijkwater.gpkg",
}

file_name = hash_name_map[file_hash2]

print(f"{geopackage_path2.name} -> {file_name}")
