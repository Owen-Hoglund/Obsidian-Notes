UPDATE changes the values in a column to a given value. It can be further specified to values in that column where the row has a particular value by using a WHERE statement

The statement below updates the record with an `id` value of `4` to have the `twitter_handle` `@taylorswift13`.

```SQL
UPDATE celebs  
SET twitter_handle = '@taylorswift13'  
WHERE id = 4;
```


