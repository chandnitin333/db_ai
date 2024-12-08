
# Database import / export


## Database backeup 
        ai_icad.zip
            1. Extract this fiolder and execute below exporting command 

## Export  Mongo DB 

    mongodump --host=localhost --port=27017 --db=ai_icad --out=/Users/nitinchandekar/Documents/db



## Import Mongo DB
  
     mongorestore --host=localhost --port=27017 --db=ai_icad /Users/nitinchandekar/Documents/db/ai_icad 
