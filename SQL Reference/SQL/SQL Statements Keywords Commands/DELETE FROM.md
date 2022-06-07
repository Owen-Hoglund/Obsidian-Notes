The statement below deletes all records in the `celeb` table with no `twitter_handle`:

DELETE FROM celebs  
WHERE twitter_handle IS NULL;