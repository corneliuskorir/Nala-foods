# Nala Foods
A Flask webserver accessible using CLI meant to manage product inventory for a food business

## Set Up
```
git clone project
pipenv install
pipenv shell
```
Start the webserver:  
```
cd server
python run.py
```
# Run Tests
```
python -m pytest
```

# End Points
### GET  

index  
```
'/' #home page
```
inventory
```
'/inventory' #get inventory itemss
```
inventory item
```
'/inventory/<id>' #get inventory tem by id
```
### POST
inventory
```
'/inventory' # add inventory items
```
### POST
inventory
```
'/inventory/<id>' # update inventory items
```
### DELETE
inventory
```
'/inventory/<id>' # delete inventory items
```