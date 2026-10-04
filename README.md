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
Cli
```
cd client
python app.py
```
# Run Tests
```
python -m pytest
```

# Operations
### GET  

index  
```
'''end point'''
'/' #home page  
```
inventory
```
'''endpoint'''  
'/inventory' #get inventory items   
'''cli access'''  
python app.py get
```
inventory item
```
'''endpoint'''  
'/inventory/<id>' #get inventory tem by id  
'''cli access'''
python app.py get-item <id>
```
### POST
inventory
```
'''endpoint'''
'/inventory' # add inventory items  
'''cli access'''
python app.py add --n <name> (optional: --q <quantity> --b <brand1> <brand2> <...>) 
```
### PATCH
inventory
```
'''endpoint'''
'/inventory/<id>' # update inventory items
'''cli access'''
python app.py edit <id> (optional:--n <name> --q <quantity> --b <brand1> )
```
### DELETE
inventory
```
'''endpoint'''
'/inventory/<id>' # delete inventory items
'''cli access'''
python app.py delete <id>
```