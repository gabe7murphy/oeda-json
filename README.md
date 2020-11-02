# Updating Actor Dictionaries 

 Instructions on how to add new actors, codes, and aliases to the JSON converted actor dictionaries. 

## Software Tools
 Editing the dictionaries is best done in a text editor such as Vim. 
 
 To install Vim on Ubuntu: `sudo apt install vim` 
 
 For Windows: 'http://www.vim.org/download.php' 
 

## Demo Task: Sample Actor Addition (Adding Trump to Dictionary)
  _A new actor "Donald Trump" needs to needs to be added to the dictionary._ 

### Step 1. Use search tool in the editor (Crtl-f) to find the actor's predecessor or if none, find category to which the actor belongs 

```C++
{
        "name": "BARACK_OBAMA_ ",
        "alias": [
            "+MR_OBAMA_",
            "+MR._OBAMA_",
            "+PRESIDENT_OBAMA_",
            "+OBAMA",
            "+PRESIDENT_BARACK_OBAMA",
            "+US_PRESIDENT_BARACK_OBAMA",
            "+AMERICAN_PRESIDENT_BARACK_OBAMA",
            "+SENATOR_OBAMA",
            "+UNITED_STATES_PRESIDENT_BARACK_OBAMA",
            "+BARACK_HUSSEIN_OBAMA",
            "+BARACK_H._OBAMA",
            "+PRESIDENT-ELECT_OBAMA",
            "+PRESIDENT-ELECT_BARACK_OBAMA",
            "+THE_OBAMA_ADMINISTRATION",
            "+OBAMA_ADMINISTRATION"
        ],
        "codes": [
            "[USAELI 780101-000101]",
            "[USAGOV 090120-170120]",
            "[USAELI]"
        ],
        "comments": []
    },
### START NEW ACTOR HERE 
```

### Step 2. Creating the "name" key value pair

```C++
{ ### open bracket to start new object
        "name": "DONALD_TRUMP_ ",  ### tab over twice and use the following format "name": "FIRST_LAST_ ",
        ### START ALIAS KEY
```
### Step 3. Creating the "alias" key value pair

```C++
{ 
        "name": "DONALD_TRUMP_ ",  
        "alias": [                ### on the same tab, start new key "alias": [  and list aliases that the sentence scraper will recognize in the news 
            "+MR_TRUMP_",         ### using the format shown: "+PREFIX_NAME_ ". *list as many as possible and then close the bracket ]  
            "+MR._TRUMP_",
            "+PRESIDENT_DONALD_TRUMP",
            "+US_PRESIDENT_DONALD_TRUMP",
            "+AMERICAN_PRESIDENT_DONALD_TRUMP",
            "+UNITED_STATES_PRESIDENT_DONALD_TRUMP",
            "+DONALD_J_TRUMP",
            "+DONALD_J._TRUMP",
            "+PRESIDENT-ELECT_TRUMP",
            "+PRESIDENT-ELECT_DONALD_TRUMP",
            "+THE_TRUMP_ADMINISTRATION",
            "+TRUMP_ADMINISTRATION"  
        ],  
        ### START CODE KEY 
```
### Step 4. Creating the "code" key value pair
To designate proper codes, use the CAMEO Actor Codebook starting at Chapter 3, page 80 (page 96 of pdf)
[CAMEO CODEBOOK](http://data.gdeltproject.org/documentation/CAMEO.Manual.1.1b3.pdf)

Use YYMMDD format for the years in which the actor filled the role

```C++
{
        "name": "DONALD_TRUMP_ ",  
        "alias": [                
            "+MR_TRUMP_",          
            "+MR._TRUMP_",
            "+PRESIDENT_DONALD_TRUMP",
            "+US_PRESIDENT_DONALD_TRUMP",
            "+AMERICAN_PRESIDENT_DONALD_TRUMP",
            "+UNITED_STATES_PRESIDENT_DONALD_TRUMP",
            "+DONALD_J_TRUMP",
            "+DONALD_J._TRUMP",
            "+PRESIDENT-ELECT_TRUMP",
            "+PRESIDENT-ELECT_DONALD_TRUMP",
            "+THE_TRUMP_ADMINISTRATION",
            "+TRUMP_ADMINISTRATION"  
        ],  
        "codes": [                     ### create code key pair in the same way as "alias": [ in the previous step
            "[USAELI 160120-170120]",  ### designate the country and role code as a connected pair "[USAELI]"
            "[USAGOV >170120]"         ### use a YYMMDD format to indicate when the actor filled the role
        ],
        ### START COMMENT KEY
```
### Step 5. Creating the "comments" key value pair
Some Actors have comments with special information that goes with each actor name or alias that cannot be displayed in the previous key pairs 


```C++
{ ### open bracket to start new object
        "name": "DONALD_TRUMP_ ",  
        "alias": [                
            "+MR_TRUMP_",          
            "+MR._TRUMP_",
            "+PRESIDENT_DONALD_TRUMP",
            "+US_PRESIDENT_DONALD_TRUMP",
            "+AMERICAN_PRESIDENT_DONALD_TRUMP",
            "+UNITED_STATES_PRESIDENT_DONALD_TRUMP",
            "+DONALD_J_TRUMP",
            "+DONALD_J._TRUMP",
            "+PRESIDENT-ELECT_TRUMP",
            "+PRESIDENT-ELECT_DONALD_TRUMP",
            "+THE_TRUMP_ADMINISTRATION",
            "+TRUMP_ADMINISTRATION"  
        ],  
        "codes": [                     
            "[USAELI 160120-170120]",  
            "[USAGOV >170120]"    
        ],
        "comments": [      ### For this actor there are no comments but the following format should be as follows:
                           ### "+ALIAS_NAME_ # Insert comment here"
        ]
    },                     ### End brackets 

```           
### Completed Actor Code with context

```C++
{
        "name": "BARACK_OBAMA_ ",
        "alias": [
            "+MR_OBAMA_",
            "+MR._OBAMA_",
            "+PRESIDENT_OBAMA_",
            "+OBAMA",
            "+PRESIDENT_BARACK_OBAMA",
            "+US_PRESIDENT_BARACK_OBAMA",
            "+AMERICAN_PRESIDENT_BARACK_OBAMA",
            "+SENATOR_OBAMA",
            "+UNITED_STATES_PRESIDENT_BARACK_OBAMA",
            "+BARACK_HUSSEIN_OBAMA",
            "+BARACK_H._OBAMA",
            "+PRESIDENT-ELECT_OBAMA",
            "+PRESIDENT-ELECT_BARACK_OBAMA",
            "+THE_OBAMA_ADMINISTRATION",
            "+OBAMA_ADMINISTRATION"
        ],
        "codes": [
            "[USAELI 780101-000101]",
            "[USAGOV 090120-170120]",
            "[USAELI]"
        ],
        "comments": []
    },
    {
        "name": "DONALD_TRUMP_ ",
        "alias": [
            "+MR_TRUMP_",
            "+MR._TRUMP_",
            "+PRESIDENT_DONALD_TRUMP",
            "+US_PRESIDENT_DONALD_TRUMP",
            "+AMERICAN_PRESIDENT_DONALD_TRUMP",
            "+UNITED_STATES_PRESIDENT_DONALD_TRUMP",
            "+DONALD_J_TRUMP",
            "+DONALD_J._TRUMP",
            "+PRESIDENT-ELECT_TRUMP",
            "+PRESIDENT-ELECT_DONALD_TRUMP",
            "+THE_TRUMP_ADMINISTRATION",
            "+TRUMP_ADMINISTRATION"
        ],
        "codes": [
            "[USAELI 160120-170120]",
            "[USAGOV >170120]"
        ],
        "comments": []
    },

